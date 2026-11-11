from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()