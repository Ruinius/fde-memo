import sys
import markdown
from xhtml2pdf import pisa

def export_to_pdf(markdown_path, pdf_path):
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Sanitize text to replace special unicode characters that render as squares in xhtml2pdf
    md_text = md_text.replace('\u2011', '-') # Non-breaking hyphen
    md_text = md_text.replace('\u2012', '-') # Figure dash
    md_text = md_text.replace('\u2013', '-') # En dash
    md_text = md_text.replace('\u2014', '--') # Em dash
    md_text = md_text.replace('\u2018', "'").replace('\u2019', "'") # Smart single quotes
    md_text = md_text.replace('\u201C', '"').replace('\u201D', '"') # Smart double quotes

    # Convert markdown to html
    html_content = markdown.markdown(md_text, extensions=['extra', 'tables'])

    # Wrap tables in a div to help xhtml2pdf handle page-break-inside: avoid
    import re
    html_content = re.sub(r'(<table>.*?</table>)', r'<div class="table-wrapper">\1</div>', html_content, flags=re.DOTALL)

    # Wrap in basic HTML structure and apply beautiful styling
    html_string = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <style>
            @page {{
                size: letter;
                margin: 2cm;
            }}
            body {{
                font-family: Helvetica, Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                font-size: 11pt;
            }}
            h1 {{
                font-size: 20pt;
                color: #2c3e50;
                border-bottom: 1px solid #3498db;
                padding-bottom: 8px;
                margin-bottom: 15px;
                font-weight: normal;
            }}
            h2 {{
                font-size: 14pt;
                color: #2c3e50;
                margin-top: 20px;
                margin-bottom: 10px;
                font-weight: bold;
            }}
            p {{
                margin-bottom: 12px;
                text-align: left;
            }}
            ul {{
                margin-bottom: 12px;
            }}
            li {{
                margin-bottom: 4px;
            }}
            strong {{
                font-weight: bold;
                color: #1a252f;
            }}
            .table-wrapper {{
                page-break-inside: avoid;
                display: block;
                width: 100%;
            }}
            tr {{
                page-break-inside: avoid;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
                margin-bottom: 10px;
                font-size: 9pt;
                page-break-inside: avoid;
            }}
            th {{
                text-align: left;
                padding: 5px;
                border: 1px solid #bdc3c7;
                font-weight: bold;
                color: #333;
                word-wrap: break-word;
                vertical-align: top;
            }}
            td {{
                padding: 5px;
                border: 1px solid #bdc3c7;
                color: #333;
                word-wrap: break-word;
                vertical-align: top;
            }}
            th:first-child, td:first-child {{
                width: 35%;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    with open(pdf_path, "wb") as result_file:
        pisa_status = pisa.CreatePDF(html_string, dest=result_file)

    if pisa_status.err:
        print(f"Error creating PDF: {pisa_status.err}")
        sys.exit(1)
    else:
        print(f"Successfully created {pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_pdf.py <input.md> <output.pdf>")
        sys.exit(1)
    
    export_to_pdf(sys.argv[1], sys.argv[2])
