from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    current_app,
    url_for,
)

from werkzeug.utils import secure_filename
import os

from utils.rag_pipeline import process_pdf

upload_bp = Blueprint("upload", __name__)


def allowed_file(filename):
    """
    Check whether the uploaded file is a PDF.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() == "pdf"


@upload_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        # Check if a file was uploaded
        if "pdf" not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["pdf"]

        # Check if filename is empty
        if file.filename == "":
            flash("Please choose a PDF.", "warning")
            return redirect(request.url)

        # Validate file type
        if file and allowed_file(file.filename):

            # Secure the filename
            filename = secure_filename(file.filename)

            # Full path where the PDF will be saved
            filepath = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )

            # Save uploaded PDF
            file.save(filepath)

            try:
                # Process PDF and create vector database
                result = process_pdf(
                    pdf_path=filepath,
                    vector_db_path=current_app.config["VECTOR_DB_FOLDER"]
                )

                flash(result["message"], "success")

            except Exception as e:
                flash(f"Error while processing PDF: {str(e)}", "danger")

            return redirect(url_for("upload.upload"))

        flash("Only PDF files are allowed.", "danger")
        return redirect(request.url)

    return render_template("upload.html")