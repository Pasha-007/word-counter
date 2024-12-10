from PyPDF2 import PdfReader  # Updated import

def count_words_in_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        total_words = 0
        for page in reader.pages:
            text = page.extract_text()
            if text:
                words = text.split()
                total_words += len(words)
        return total_words
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
pdf_file = "/Users/muntahaakhan/My Works/Pre-Qualification Internship/Brain_Tumor Article_v2.pdf"  # Replace with the path to your PDF file
word_count = count_words_in_pdf(pdf_file)
print(f"Total word count in the PDF: {word_count}")
