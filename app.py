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
            light=float(payload['light']),
        )
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Expected numeric temperature, humidity, and light'}), 400

    readings.append(reading)
    return jsonify({'reading': asdict(reading), 'count': len(readings)}), 201


if __name__ == '__main__':
    app.run(debug=True)
