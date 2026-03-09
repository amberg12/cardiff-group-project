from dataclasses import asdict, dataclass
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@dataclass
class SensorReading:
    temperature: float
    humidity: float
    light: float

readings: list[SensorReading] = []

@app.route('/')
def home() -> str:
    return render_template('index.html', readings=readings)

@app.route('/send-test-data')
def send_test_data() -> str:
    return render_template('send-test-data.html')

@app.post('/api/readings')
def add_reading():
    payload = request.get_json(silent=True) or {}

    try:
        reading = SensorReading(
            temperature=float(payload['temperature']),
            humidity=float(payload['humidity']),
            light=float(payload.get('light', 0)),  # Default to 0 if missing
        )
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({'error': f'Expected numeric values: {str(e)}'}), 400

    readings.append(reading)
    return jsonify({'reading': asdict(reading), 'count': len(readings)}), 201

if __name__ == '__main__':
    # Allow external connections and show the IP
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print("=" * 50)
    print("🌡️  Flask Sensor Server Starting...")
    print(f"📡 Local access: http://127.0.0.1:5000")
    print(f"🌐 Network access: http://{local_ip}:5000")
    print("=" * 50)
    print("Send data to: http://<this-ip>:5000/api/readings")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
