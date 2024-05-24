from docx import Document

# Open the document
document = Document('test.docx')
# Text to find in the document
text_to_find = 'This paragraph should be commented.'

for paragraph in document.paragraphs:
    if paragraph.text == text_to_find:
        # Add a comment to the paragraph
        paragraph.add_comment('This is a test comment', 'Contractee')
        break

# Save the document
document.save('test.docx')
