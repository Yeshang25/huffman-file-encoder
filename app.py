from flask import Flask, render_template, request, send_file
from huffmancode import HuffmanCoding
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compress', methods=['POST'])
def compress():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        return 'No file selected', 400

    try:
        huffman = HuffmanCoding()

        # Read file content
        input_text = uploaded_file.read().decode('utf-8')

        # Encode data
        encoded_data, code_map = huffman.compress(input_text)

        # Generate file paths
        compressed_file_path = os.path.join(
            UPLOAD_FOLDER,
            f'compressed_{os.urandom(8).hex()}.bin'
        )

        code_map_path = os.path.join(
            UPLOAD_FOLDER,
            f'codes_{os.urandom(8).hex()}.txt'
        )

        # Save encoded data
        with open(compressed_file_path, 'w') as compressed_file:
            compressed_file.write(encoded_data)

        # Save Huffman codes
        with open(code_map_path, 'w') as code_file:
            for char, code in code_map.items():
                code_file.write(f"{repr(char)}:{code}\n")

        # Send file to user
        response = send_file(
            compressed_file_path,
            as_attachment=True,
            download_name='encoded.bin'
        )

        # Cleanup after sending
        @response.call_on_close
        def cleanup():
            try:
                os.remove(compressed_file_path)
                os.remove(code_map_path)
            except:
                pass

        return response

    except Exception as error:
        return f'Error during encoding: {str(error)}', 500


@app.route('/decompress', methods=['POST'])
def decompress():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        return 'No file selected', 400

    try:
        huffman = HuffmanCoding()

        # Read encoded data
        encoded_data = uploaded_file.read().decode('utf-8')

        # Output file path
        output_file_path = os.path.join(
            UPLOAD_FOLDER,
            f'decoded_{os.urandom(8).hex()}.txt'
        )

        # Find latest code map
        code_files = [
            f for f in os.listdir(UPLOAD_FOLDER)
            if f.startswith('codes_')
        ]

        if not code_files:
            return 'No codes file found for decoding', 400

        latest_code_file = max(
            code_files,
            key=lambda x: os.path.getctime(os.path.join(UPLOAD_FOLDER, x))
        )

        code_map_path = os.path.join(UPLOAD_FOLDER, latest_code_file)

        # Load code map
        with open(code_map_path, 'r') as code_file:
            for line in code_file:
                char, code = line.strip().split(':')
                char = eval(char)  # keep as-is (your logic)
                huffman.reverse_codes[code] = char

        # Decode data
        decoded_text = huffman.decompress(encoded_data)

        # Save decoded output
        with open(output_file_path, 'w') as output_file:
            output_file.write(decoded_text)

        # Send file
        response = send_file(
            output_file_path,
            as_attachment=True,
            download_name='decoded.txt'
        )

        # Cleanup
        @response.call_on_close
        def cleanup():
            try:
                os.remove(output_file_path)
            except:
                pass

        return response

    except Exception as error:
        return f'Error during decoding: {str(error)}', 500


if __name__ == '__main__':
    app.run(debug=True)