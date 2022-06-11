import PyPDF2

reader = PyPDF2.PdfFileReader("./1.pdf")
writer = PyPDF2.PdfFileWriter()

for page_num in range(reader.numPages):
    # 将原文件中的每一页添加到writer对象中去
    writer.addPage((reader.getPage(page_num)))

# 通过encrypt方法加密PDF文件，参数就是设置的密码
writer.encrypt('123456')

with open("./1_加密.pdf", 'wb') as file:
    writer.write(file)
