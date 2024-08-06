import json
import pdfkit
from flask import Flask, render_template, send_file

# Path to wkhtmltopdf binary
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

app = Flask(__name__)

@app.route('/')
def index():
    # Load data from JSON file
    with open('data.json') as f:
        data = json.load(f)
    return render_template('index.html', data=data)

@app.route('/pdf')
def pdf():
    # Load data from JSON file
    with open('data.json') as f:
        data = json.load(f)
    
    # Render the template to a string with data
    rendered = render_template('index.html', data=data)
    
    # Save the PDF to a temporary file
    pdf = pdfkit.from_string(rendered, False, configuration=config)
    pdf_path = 'output.pdf'
    with open(pdf_path, 'wb') as f:
        f.write(pdf)
    
    # Send the file for download
    return send_file(pdf_path, as_attachment=True, download_name='output.pdf')

if __name__ == '__main__':
    app.run(debug=True)
