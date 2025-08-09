import PyPDF2  # Import the PyPDF2 library to handle PDF files

pdfiles = ["1.pdf", "2.pdf"]  # List of PDF file names to be merged
merger = PyPDF2.PdfMerger()  # Create a new PdfMerger object
for filename in pdfiles:  
    pdfFile = open(filename, 'rb')  # Open the current PDF file in binary read mode
    pdfReader = PyPDF2.PdfReader(pdfFile)  # Create a PdfReader to read the opened file
    merger.append(pdfReader)  # Append the content of the current PDF to the merger
pdfFile.close()  # Close the last opened PDF file
merger.write('merged.pdf')  # Write the merged PDF to a new file called 'merged.pdf'