import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def chat_link_to_pdf(chat_link, output_pdf_filename):
    response = requests.get(chat_link)
    chat_html = response.text
    
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(chat_html, "html.parser")
    chat_text = soup.get_text()
    
    # Create a PDF file
    c = canvas.Canvas(output_pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    # Write chat content to PDF
    y_position = 700  # Initial y position
    for line in chat_text.splitlines():
        c.drawString(50, y_position, line)
        y_position -= 15  # Adjust for line spacing
    
    c.save()
    print(f"PDF file '{output_pdf_filename}' created.")

# Provide the chat link and output PDF filename
chat_link = input("enter the link:")# Replace with the actual chat link
output_pdf_filename = "chat_output.pdf"

chat_link_to_pdf(chat_link, output_pdf_filename)
