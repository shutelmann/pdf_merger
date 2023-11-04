import PyPDF2
import sys

# Здесь принимаем названия pdf файлов в качестве аргументов, количество файлов неограничeно

pdf_files = sys.argv[1:]

# Объявляем функцию, которая будет объединять наши файлы


def pdf_merger(list_of_pdf_files):
    merger = PyPDF2.PdfFileMerger()
    for i in list_of_pdf_files:
        merger.append(i)
    merger.write('merged.pdf')


pdf_merger(pdf_files)
