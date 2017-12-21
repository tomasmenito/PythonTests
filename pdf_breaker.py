import PyPDF2, os

pdfReader = PyPDF2.PdfFileReader(open('file.pdf','rb'))
i=99
while (pdfReader.decrypt(str(i))!=1):
    i=i+1

    
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pageObj=pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('no_password.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
