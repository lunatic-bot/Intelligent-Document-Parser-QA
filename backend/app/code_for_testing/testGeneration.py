# from docx import Document

# doc = Document()
# doc.add_paragraph("This is a DOCX test file.")
# doc.add_paragraph("It contains two paragraphs.")
# doc.save("sample.docx")

from reportlab.pdfgen import canvas

c = canvas.Canvas("sample.pdf")
c.drawString(100, 750, "This is a test PDF.")
c.drawString(100, 735, "It has two lines of text.")
c.save()
