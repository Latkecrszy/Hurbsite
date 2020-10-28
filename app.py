from flask import make_response, jsonify, Flask, render_template
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/todo')
def todo():
	data = [{"key": "value"}, {"key": "value"}]
	res = make_response(jsonify(data))
	res.mimetype = "application/json"
	return res


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)

# https://still-castle-12476.herokuapp.com/todo
