import os
import logging
from uuid import uuid4
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.document_parser.dispatcher import DocumentParser
from app.core.document_parser.normalizer import TextNormalizer
from app.core.document_parser.preprocessor import Preprocessor
import app.schema.document_schemas as schemas , app.models, app.crud.document_crud as crud , app.database as database

# Set up logger
logger = logging.getLogger("document_api")
logging.basicConfig(level=logging.INFO)

# Initialize FastAPI router
router = APIRouter()
UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize document parser and preprocessor
parser = DocumentParser(
    poppler_path=r"C:\Users\atalb\AppData\Local\poppler-24.08.0\Library\bin",
    tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
preprocessor = Preprocessor()

# Upload and process a new document
@router.post("/upload-document", response_model=schemas.DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),  # Receive file from client
    db: AsyncSession = Depends(database.get_db)  # Dependency-injected DB session
):
    """
    Upload a document, parse its contents, store metadata in DB, return preview and document ID.
    """
    # Extract and validate file extension
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["pdf", "docx", "txt"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # Generate a unique ID and construct local save path
    file_id = str(uuid4())
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}.{ext}")

    try:
        # Save the uploaded file to disk
        with open(save_path, "wb") as f:
            f.write(await file.read())
        logger.info(f"Saved file to {save_path}")

        # Parse document content using selected parser
        raw_text = parser.parse(save_path, ext)
        # Normalize whitespace, punctuation etc.
        normalized = TextNormalizer.normalize(raw_text)
        # Further preprocess (cleaning, sentence filter etc.)
        processed = preprocessor.process(normalized)

        # Create document metadata schema instance
        doc_data = schemas.Document(
            document_id=file_id,
            filename=file.filename,
            file_type=ext,
            file_path=save_path,
            file_size=os.path.getsize(save_path)
        )
        # Save document metadata to DB
        await crud.save_details(db, doc_data)

    except Exception as e:
        logger.exception("Upload/parse failure")
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")

    # Return preview and ID
    return schemas.DocumentResponse(
        document_id=file_id,
        file_type=ext,
        original_filename=file.filename,
        text_preview=processed[:500]
    )


# Return parsed content of a previously uploaded document
@router.get("/document/{doc_id}", response_model=schemas.DocumentTextResponse)
async def get_parsed_document(doc_id: str, db: AsyncSession = Depends(database.get_db)):
    """
    Retrieve parsed document text using the document ID stored in DB.
    """
    try:
        # Fetch metadata for document from DB
        doc_entry = await crud.get_details_by_id(db, doc_id)
        if not doc_entry:
            raise HTTPException(status_code=404, detail="Document metadata not found")

        # Parse and preprocess from saved file path
        ext = doc_entry.file_type
        file_path = doc_entry.file_path

        raw_text = parser.parse(file_path, ext)
        normalized = TextNormalizer.normalize(raw_text)
        processed = preprocessor.process(normalized)

        logger.info(f"Fetched parsed text for {doc_id}")
        return schemas.DocumentTextResponse(
            document_id=doc_id,
            text=processed
        )

    except Exception as e:
        logger.exception("Failed to retrieve parsed document")
        raise HTTPException(status_code=500, detail=f"Failed to fetch document text: {str(e)}")


# Return only metadata (no text) for a given document
@router.get("/document/{doc_id}/metadata", response_model=schemas.DocumentMeta)
async def get_document_metadata(doc_id: str, db: AsyncSession = Depends(database.get_db)):
    """
    Return metadata only (filename, type, path, size) for a document.
    """
    try:
        doc_entry = await crud.get_details_by_id(db, doc_id)
        if not doc_entry:
            raise HTTPException(status_code=404, detail="Document metadata not found")
        return doc_entry
    except Exception as e:
        logger.exception("Failed to fetch metadata")
        raise HTTPException(status_code=500, detail=f"Error fetching document metadata: {str(e)}")


# Return metadata for all documents in the database
@router.get("/documents", response_model=List[schemas.DocumentMeta])
async def list_documents(db: AsyncSession = Depends(database.get_db)):
    """
    List metadata for all uploaded documents (no content).
    """
    try:
        documents = await crud.get_all_documents(db)
        return documents
    except Exception as e:
        logger.exception("Failed to list documents")
        raise HTTPException(status_code=500, detail="Error listing documents")


# from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.schema.document_schemas import Document
# import app.schema.document_schemas as schemas , app.models, app.crud.document_crud as crud , app.database as database


# router = APIRouter(prefix="/documents", tags=["documents"])


# @router.post("/document",response_model=Document)
# async def create_data(data:schemas.Document, db:AsyncSession=Depends(database.get_db)):
#     return await crud.save_details(db,data)


