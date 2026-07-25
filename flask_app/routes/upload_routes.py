from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import os

upload_bp = Blueprint("upload", __name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() == "pdf"


@upload_bp.route("/upload", methods=["GET", "POST"])
def upload():

    from flask import current_app

    if request.method == "POST":

        if "pdf" not in request.files:

            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["pdf"]

        if file.filename == "":

            flash("Please choose a PDF.", "warning")
            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            save_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(save_path)

            flash("PDF uploaded successfully!", "success")

            return redirect("/upload")

        flash("Only PDF files are allowed.", "danger")

    return render_template("upload.html")