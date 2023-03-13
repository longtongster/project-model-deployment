import os
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
import matplotlib.pyplot as plt

app = Flask(__name__)

IMG_FOLDER = os.path.join("static", "IMG")
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
app.config["SECRET_KEY"] = "fdsdfsgs"

print(app.config["UPLOAD_FOLDER"])

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["POST","GET"])
def upload_img():
    print("request data:")
    print(request)
    print(request.files)
    print(request.method)
    print(request.url)
    if request.method == "POST":
        if request.files is None:
            return jsonify({"error":"No file submitted"})
        filename = request.files['file'].filename
        file = request.files["file"]

        print("filename ",filename)
        print("file", file)
        print("URL_FOR" ,url_for('display_img', filename="IMG/" + filename))

        # saving the file
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # if a file is submitted we want to show the image
        # this means we have to provide the image as a parameter
        # return redirect(url_for('display_img'))
        return render_template("ul1.html", filename=filename)

    if request.method == "GET":
        return render_template("ul1.html")

#@app.route('/display_image')
#def display_img():
#    Flask_logo = os.path.join(app.config["UPLOAD_FOLDER"], "flask-logo.png")
#    print(Flask_logo)
#    print(url_for('static', filename='IMG/flask_logo.png'))

#    return render_template("show_image.html", user_image=url_for('static', filename='IMG/flask_logo.png'))

@app.route('/display/<filename>')
def display_img(filename):
    # print('display_image filename: ' + filename)
    print("\nDISPLAY IMAGE")
    print(url_for('static', filename='IMG/' + filename))
    return redirect(url_for('static', filename='IMG/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)