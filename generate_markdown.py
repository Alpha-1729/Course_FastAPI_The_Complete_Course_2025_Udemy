import os
import base64
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def read_file_content(file_path):
    """Read and return the content of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def encode_file_to_base64(file_path):
    """Encode a file to Base64."""
    with open(file_path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def should_process_folder(folder_path):
    """Check if a folder should be processed."""
    if os.path.basename(folder_path) == 'config':
        return False
    for root, dirs, files in os.walk(folder_path):
        if 'Resources' in dirs or 'main.py' in files:
            return True
    return False

def generate_html_for_folder(folder_path, html_file):
    """Generate HTML content for a specific folder."""
    for root, dirs, files in os.walk(folder_path):
        if os.path.basename(root) == 'Resources':
            html_file.write(f"<h3>Resources in {os.path.basename(os.path.dirname(root))}</h3>\n")
            for file in files:
                file_path = os.path.join(root, file)
                if file == '.gitkeep':
                    continue
                if file.endswith(('.png', '.jpg', '.jpeg')):
                    base64_data = encode_file_to_base64(file_path)
                    html_file.write(f'<img src="data:image/{file.split(".")[-1]};base64,{base64_data}" alt="{file}" style="max-width: 50%; height: auto;"><br>\n')
                elif file.endswith('.pdf'):
                    html_file.write(f'<a href="{file_path}" download="{file}">Download {file}</a><br>\n')
            html_file.write("<hr>\n")
            continue 
        
        html_file.write(f"<h2>{os.path.basename(root)}</h2>\n")
        for file in files:
            file_path = os.path.join(root, file)
            if file == 'main.py':
                html_file.write(f"<h3>{file}</h3>\n")
                code_content = read_file_content(file_path)
                highlighted_code = highlight(code_content, PythonLexer(), HtmlFormatter())
                html_file.write(f'<pre><code>{highlighted_code}</code></pre>')
            elif file.endswith(('.png', '.jpg', '.jpeg')):
                base64_data = encode_file_to_base64(file_path)
                html_file.write(f'<img src="data:image/{file.split(".")[-1]};base64,{base64_data}" alt="{file}" style="max-width: 50%; height: auto;"><br>\n')
            elif file.endswith('.pdf'):
                html_file.write(f'<a href="{file_path}" download="{file}">Download {file}</a><br>\n')
        html_file.write("<hr>\n")

def generate_html_for_all_folders(base_directory, output_file):
    """Generate HTML content for all folders in the base directory."""
    output_file_path = os.path.join(base_directory, output_file)
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write("<!DOCTYPE html>\n<html>\n<head>\n")
        html_file.write("<title>Combined Documentation</title>\n")
        html_file.write("<style>\n")
        html_file.write("body { font-family: Arial, sans-serif; }\n")
        html_file.write("pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }\n")
        html_file.write("code { font-family: monospace; }\n")
        html_file.write("img { max-width: 50%; height: auto; }\n")
        html_file.write("a { color: #007BFF; text-decoration: none; }\n")
        html_file.write("a:hover { text-decoration: underline; }\n")
        html_file.write(HtmlFormatter().get_style_defs(".highlight"))
        html_file.write("</style>\n")
        html_file.write("</head>\n<body>\n")
        for folder_name in os.listdir(base_directory):
            folder_path = os.path.join(base_directory, folder_name)
            if os.path.isdir(folder_path) and should_process_folder(folder_path):
                generate_html_for_folder(folder_path, html_file)
        html_file.write("</body>\n</html>\n")

if __name__ == "__main__":
    base_directory = "."  # Current directory (root folder)
    output_html_file = "output.html"  # Output file name
    generate_html_for_all_folders(base_directory, output_html_file)
    print(f"HTML file generated: {os.path.join(base_directory, output_html_file)}")
