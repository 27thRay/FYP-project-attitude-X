from pdfminer.high_level import extract_text

text = extract_text("Resume_5.pdf")
print(text)