from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def details():
    return jsonify({
        'time': datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'you are doing great, agora tem que funcionar, é muita coisa rs, mas coisa rs!!!:)'
    })

@app.route('/api/v1/healthz', methods=['GET'])
def healthz():
    return jsonify({'status': 'up and running'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
