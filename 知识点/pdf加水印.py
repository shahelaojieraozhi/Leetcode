import PyPDF2
from PyPDF2.pdf import PageObject

reader = PyPDF2.PdfFileReader("./1.pdf")
reader1 = PyPDF2.PdfFileReader("./2.pdf")
writer = PyPDF2.PdfFileWriter()

# 获取水印页
watermark_page = reader1.getPage(0)
for page_num in range(reader.numPages):
    current_page = reader.getPage(page_num)
    # 将水印页和当前页进行合并
    current_page.mergePage(watermark_page)
    writer.addPage(current_page)
# 将pdf 写入文件
with open("./1-水印.pdf", 'wb') as file:
    writer.write(file)

