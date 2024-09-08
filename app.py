from flask import Flask, request, render_template_string
import lxml.etree as ET

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    message = ""
    if request.method == 'POST':
        xml_data = request.form['message']
        try:
            parser = ET.XMLParser(resolve_entities=True)
            tree = ET.fromstring(xml_data, parser)
            result = ET.tostring(tree, pretty_print=True).decode()
            message = "Your concerns have been submitted and will be addressed."
        except ET.XMLSyntaxError:
            message = "Your concerns will be resolved. Thank you for your submission."

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>University Contact Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
                text-align: center;
            }
            header {
                width: 100%;
                background-color: #007bff;
                padding: 10px 0;
                color: white;
                text-align: center;
            }
            header h1 {
                font-size: 24px;
                margin: 0;
            }
            form {
                display: flex;
                flex-direction: column;
                margin-top: 20px;
            }
            label {
                margin-bottom: 5px;
                color: #555;
            }
            textarea, input[type="submit"] {
                margin-bottom: 20px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            input[type="submit"] {
                background-color: #007bff;
                color: white;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
            .message {
                margin-top: 20px;
                padding: 10px;
                background-color: #dff0d8;
                color: #3c763d;
                border: 1px solid #d6e9c6;
                border-radius: 5px;
            }
            .result {
                margin-top: 20px;
                padding: 10px;
                background-color: #f4f4f4;
                color: #333;
                border: 1px solid #ddd;
                border-radius: 5px;
                white-space: pre-wrap;
                word-wrap: break-word;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>University Contact Form</h1>
        </header>
        <div class="container">
            <form method="POST">
                <label for="message">Your Message:</label>
                <textarea id="message" name="message" rows="10" required></textarea>
                <input type="submit" value="Submit">
            </form>
            {% if message %}
            <div class="message">{{ message }}</div>
            {% endif %}
            {% if result %}
            <div class="result">{{ result }}</div>
            {% endif %}
        </div>
    </body>
    </html>
    ''', message=message, result=result)

if __name__ == '__main__':
    app.run(debug=True)

