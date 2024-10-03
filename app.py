from flask import Flask, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    if not data:
        return {"error": "Data is required"}, 400
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
