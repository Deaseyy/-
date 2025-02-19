import json
from flask import Flask, make_response

app = Flask(__name__)


@app.route('/download', methods=["GET"])
def download():
	user = {'name':'dewei', 'age':33}
	data = json.dumps(user)

	response = make_response(data)
	response.headers['content-type'] = 'applicantion/octet-stream;charset=utf-8'
	response.headers['content-disposition'] = 'attachment;filename=user.json'
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5005, debug=True)

