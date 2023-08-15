# ChatGPT Chat Link to PDF Converter

This Python script allows you to convert ChatGPT chat links into PDF files. It fetches the chat content from a provided link, extracts the relevant text, and generates a PDF document containing the chat.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`, `reportlab`

Install the required libraries using the following command:


``pip install requests beautifulsoup4 reportlab``

## Usage

Clone this repository or download the chat_link_to_pdf.py script.

Provide the chat link you want to convert and specify the output PDF filename in the script.

Run the script using the following command:
 
`python chat_link_to_pdf.py`

# Provide the chat link and output PDF filename
chat_link = "https://chat.example.com/chat"
output_pdf_filename = "chat_output.pdf"

chat_link_to_pdf(chat_link, output_pdf_filename)

The script will create a PDF file named chat_output.pdf containing the chat content.

## Notes
The script assumes that the chat content is in a plain text format within the HTML structure. You might need to adapt the script if the HTML structure varies.

The accuracy of text extraction depends on the HTML structure of the chat page. Minor adjustments to the script might be necessary based on the actual content.

## License
- This project is licensed under the MIT License.

## Acknowledgment

This project was inspired by the need to easily convert ChatGPT chat links to PDF files for documentation and archiving purposes. The code in this repository is a simple implementation that aims to provide a starting point for achieving this functionality.

Special thanks to the developers of the `requests`, `beautifulsoup4`, and `reportlab` libraries, which are essential components of this project.

If you find this project helpful or have suggestions for improvements, feel free to contribute, open issues, or provide feedback. Your contributions are greatly appreciated!

## let's connect

 developed by [Anwesha Ghosh](https://github.com/anwe712).

Feel free to connect with me on GitHub!
