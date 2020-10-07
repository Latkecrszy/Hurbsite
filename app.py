from flask import make_response, jsonify, Flask


app = Flask(__name__)

@app.route('/todo')

def todo():
	data = [{"key1": "value1"}, {"key2": "value2"}]
	res = make_response(jsonify(data))
	res.mimetype = "application/json"
	return res


if __name__ == '__main__':
	app.run()

	
