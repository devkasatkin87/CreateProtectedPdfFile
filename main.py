from PyPDF2 import PdfReader, PdfWriter
from getpass import getpass

pdf_writer = PdfWriter()
# загружаем данные pdf через объект библиотеки
pdf = PdfReader('sample.pdf')

# получаем все страницы pdf файла и записываем их в свойство объекта
for page in range(len(pdf.pages)):
    pdf_writer.add_page(pdf.pages[page])
 
# ввод пароля (скрытого при вводе)
password = getpass(prompt='Enter password: ')

# шифруем файл с помощью пароля
pdf_writer.encrypt(password)

# записываем данные в файл
with open('protected.pdf', 'wb') as file:
    pdf_writer.write(file)