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

        if "pdf" not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["pdf"]

        if file.filename == "":
            flash("Please choose a PDF.", "warning")
            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            filepath = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(filepath)

            try:

                result = process_pdf(
                    upload_folder=current_app.config["UPLOAD_FOLDER"],
                    vector_db_path=current_app.config["VECTOR_DB_FOLDER"]
                )

                flash(result["message"], "success")

                return redirect(url_for("chat.chat"))

            except Exception as e:

                flash(
                    f"Error while processing PDFs: {str(e)}",
                    "danger"
                )

                return redirect(request.url)

        flash("Only PDF files are allowed.", "danger")
        return redirect(request.url)

    pdf_files = sorted(
        [
            file
            for file in os.listdir(current_app.config["UPLOAD_FOLDER"])
            if file.lower().endswith(".pdf")
        ]
    )
    return render_template(
        "upload.html",pdf_files=pdf_files
    )

@upload_bp.route("/delete/<filename>", methods=["POST"])
def delete_pdf(filename):

    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    try:

        # Delete the selected PDF
        if os.path.exists(filepath):
            os.remove(filepath)

        # Rebuild FAISS using remaining PDFs
        process_pdf(
            upload_folder=current_app.config["UPLOAD_FOLDER"],
            vector_db_path=current_app.config["VECTOR_DB_FOLDER"]
        )

        flash(f"{filename} deleted successfully.", "success")

    except Exception as e:

        flash(f"Error deleting PDF: {str(e)}", "danger")

    return redirect(url_for("upload.upload"))