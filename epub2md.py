import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    text_content = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text_content.append(soup.get_text())

    return '\n'.join(text_content)

# Replace with the actual EPUB file name once uploaded
epub_file = "Data Engineering Design Patterns.epub.epub"

# Extract text from the EPUB file
text = extract_text_from_epub(epub_file)

# Save as plain text
with open('output.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(text)

# Save as markdown (basic conversion)
with open('output.md', 'w', encoding='utf-8') as md_file:
    md_file.write(text)

print("EPUB content has been extracted and saved as 'output.txt' and 'output.md'.")

