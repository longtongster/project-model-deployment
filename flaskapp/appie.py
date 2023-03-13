import os

from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

IMG_FOLDER = os.path.join("static", "IMG")
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
app.config["SECRET_KEY"] = "fdsdfsgs"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["POST","GET"])
def upload_img():
    if request.method == "POST":
        # if here is no
        if "file" not in request.files:
            flash("No file part")
            return jsonify({"error":"No file submitted"})
        # now we know there is key "file"
        file = request.files["file"]

        # only save the file if it has an allowed extension
        if file and allowed_file(file.filename):
            # saving the file
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("File successfully saved")

            # if a file is submitted we want to show the image
            # this means we have to provide the image as a parameter
            # return redirect(url_for('display_img'))
            return render_template("index.html", filename=filename)
        else:
            flash("only extensions allowed are png, jpg or jpeg")
            return redirect(request.url)

    if request.method == "GET":
        return render_template("index.html")


@app.route('/display/<filename>')
def display_img(filename):
    print('display_image filename: ' + filename)
    print("\nDISPLAY IMAGE")
    #print(url_for('static', filename='IMG/' + filename))
    return redirect(url_for('static', filename='IMG/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)