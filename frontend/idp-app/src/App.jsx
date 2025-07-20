// src/App.jsx
import { useState } from "react";
import FileUpload from "./components/FileUpload/FileUpload";
import ChatBox from "./components/ChatBox/ChatBox";

function App() {
  const [documentId, setDocumentId] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">
        Intelligent Document Processor
      </h1>
      {!documentId ? (
        <FileUpload
          onUploadSuccess={(data) => setDocumentId(data.document_id)}
        />
      ) : (
        <ChatBox documentId={documentId} />
      )}
    </div>
  );
}

export default App;
