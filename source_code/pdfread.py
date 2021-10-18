from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet=io.BytesIO()

can=canvas.Canvas(packet,pagesize=letter)
can.drawString(5,5,"Apress")
can.save()

packet.seek(0)
new_pdf=PdfFileReader(packet)

existing_pdf=PdfFileReader(open('D:\\test.pdf','rb'))
output=PdfFileWriter()

page=existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

outputStream=open('D:\\newfile.pdf','wb')
output.write(outputStream)
outputStream.close()



