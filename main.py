from PyPDF2 import PdfMerger

pdfs = ["MERGE.pdf", "ME.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("MERGE ME.pdf")
merger.close()
