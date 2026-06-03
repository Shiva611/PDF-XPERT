# backend.py

import os
import pikepdf
import fitz
from pdf2docx import Converter
from docx2pdf import convert


def merge_pdfs(pdf_files, output_file):
    try:
        merged = pikepdf.Pdf.new()
        for file in pdf_files:
            pdf = pikepdf.Pdf.open(file)
            merged.pages.extend(pdf.pages)
        merged.save(output_file)
        return f"PDFs merged successfully!\nSaved at:\n{output_file}"
    except Exception as e:
        return f"Error: {e}"


def split_pdf(input_file):
    try:
        folder = os.path.dirname(input_file)
        pdf = pikepdf.Pdf.open(input_file)

        for i, page in enumerate(pdf.pages):
            new_pdf = pikepdf.Pdf.new()
            new_pdf.pages.append(page)
            new_pdf.save(os.path.join(folder, f"page_{i+1}.pdf"))

        return f"PDF split completed!\nFiles saved in:\n{folder}"
    except Exception as e:
        return f"Error: {e}"


def rotate_pdf(input_file, angle):
    try:
        output = input_file.replace(".pdf", "_rotated.pdf")
        pdf = pikepdf.Pdf.open(input_file)

        for page in pdf.pages:
            current = page.get("/Rotate", 0)
            page.Rotate = current + angle

        pdf.save(output)
        return f"PDF rotated successfully!\nSaved at:\n{output}"
    except Exception as e:
        return f"Error: {e}"


def protect_pdf(input_file, password):
    try:
        pdf = pikepdf.Pdf.open(input_file)

        temp_file = input_file.replace(".pdf", "_temp.pdf")

        pdf.save(
            temp_file,
            encryption=pikepdf.Encryption(
                user=password,
                owner=password
            )
        )

        pdf.close()
        os.remove(input_file)
        os.rename(temp_file, input_file)

        return "PDF protected successfully!"
    except Exception as e:
        return f"Error: {e}"


def unlock_pdf(input_file, password):
    try:
        pdf = pikepdf.Pdf.open(input_file, password=password)

        temp_file = input_file.replace(".pdf", "_temp.pdf")
        pdf.save(temp_file)
        pdf.close()

        os.remove(input_file)
        os.rename(temp_file, input_file)

        return "PDF unlocked successfully!"
    except Exception:
        return "Invalid password! Please try again."

def reverse_pdf(input_file):
    try:
        output = input_file.replace(".pdf", "_reversed.pdf")
        pdf = pikepdf.Pdf.open(input_file)

        pages = list(pdf.pages)[::-1]

        new_pdf = pikepdf.Pdf.new()
        for page in pages:
            new_pdf.pages.append(page)

        new_pdf.save(output)
        return f"PDF pages reversed successfully!\nSaved at:\n{output}"
    except Exception as e:
        return f"Error: {e}"


def delete_pages(input_file, pages_text):
    try:
        output = input_file.replace(".pdf", "_edited.pdf")
        pdf = pikepdf.Pdf.open(input_file)

        pages = [int(x.strip()) for x in pages_text.split(",")]
        pages.sort(reverse=True)

        for p in pages:
            del pdf.pages[p - 1]

        pdf.save(output)
        return f"Selected pages deleted successfully!\nSaved at:\n{output}"
    except Exception as e:
        return f"Error: {e}"


def pdf_to_image(input_file):
    try:
        folder = os.path.dirname(input_file)
        pdf = fitz.open(input_file)

        for i, page in enumerate(pdf):
            img = page.get_pixmap()
            img.save(os.path.join(folder, f"image_{i+1}.jpg"))

        return f"PDF converted to images successfully!\nSaved in:\n{folder}"
    except Exception as e:
        return f"Error: {e}"


def pdf_to_word(input_file):
    try:
        output = input_file.replace(".pdf", ".docx")
        cv = Converter(input_file)
        cv.convert(output)
        cv.close()
        return "PDF converted to Word successfully! Document is ready."
    except Exception as e:
        return f"Error: {e}"


def word_to_pdf(input_file):
    try:
        output = input_file.replace(".docx", ".pdf")
        convert(input_file, output)
        return f"Word converted to PDF successfully!\nSaved at:\n{output}"
    except Exception as e:
        return f"Error: {e}"