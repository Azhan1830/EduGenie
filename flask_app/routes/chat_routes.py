from flask import (
    Blueprint,
    render_template,
    request,
    current_app,
    flash
)

from utils.qa_pipeline import answer_question

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["GET", "POST"])
def chat():

    answer = None
    question = ""
    context = None

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if not question:

            flash("Please enter a question.", "warning")

        else:

            try:

                result = answer_question(
                    question=question,
                    vector_db_path=current_app.config["VECTOR_DB_FOLDER"]
                )

                answer = result["answer"]
                context = result["context"]

            except Exception as e:

                flash(f"Error: {str(e)}", "danger")

    return render_template(
        "chat.html",
        question=question,
        answer=answer,
        context=context
    )