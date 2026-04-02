from flask import Flask, jsonify
import uuid

app = Flask(__name__)

# Mock signed URL generator (replace with AWS S3 or MinIO)
def generate_signed_url(filename):
    fake_url = f"https://storage.example.com/upload/{filename}?token={uuid.uuid4()}"
    return fake_url

@app.route('/api/get-upload-url', methods=['GET'])
def get_upload_url():
    filename = f"image_{uuid.uuid4()}.jpg"
    url = generate_signed_url(filename)

    return jsonify({
        "upload_url": url,
        "filename": filename
    })

if __name__ == '__main__':
    app.run(port=8001)
