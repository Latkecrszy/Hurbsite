from flask import make_response, jsonify, Flask
import os

app = Flask(__name__)


@app.route('/todo')
def todo():
	data = [{"key": "value"}, {"key2": "value2"}]
	res = make_response(jsonify(data))
	res.mimetype = "application/json"
	return res


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)