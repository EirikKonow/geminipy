from flask import Flask, flash, request, redirect, url_for, Response, render_template
from sorter import sort
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/main")
def main(my_value=None):
	return render_template("main.html", value=my_value)


@app.route("/handle_main", methods=['GET', 'POST'])
def handle_main():
	infile = request.files["fileToUpload"]
	print(infile)
	filename = secure_filename(infile.filename)
	infile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	my_value = request.form['value']
	sort(my_value, filename)
	return main(my_value), 204


if __name__=="__main__":
	app.secret_key = 'super secret key'
	app.run(debug=True, host="0.0.0.0")