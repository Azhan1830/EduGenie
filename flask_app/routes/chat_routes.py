from flask import (
    Blueprint,
    render_template,
    request,
    current_app,
    flash,
    session,
    redirect,
    url_for
)

from utils.qa_pipeline import answer_question

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["GET", "POST"])
def chat():

    # Initialize chat history if it doesn't exist
    if "chat_history" not in session:
        session["chat_history"] = []

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

                # Get existing history
                history = session["chat_history"]

                # Add new conversation
                history.append({
                    "question": question,
                    "answer": answer,
                    "context": context
                })

                # Save back to session
                session["chat_history"] = history
                session.modified = True

            except Exception as e:

                flash(f"Error: {str(e)}", "danger")

    return render_template(
        "chat.html",
        chat_history=session.get("chat_history", [])
    )
    
@chat_bp.route("/clear_chat", methods=["POST"])
def clear_chat():

    session.pop("chat_history", None)

    flash("Chat history cleared successfully.", "success")

    return redirect(url_for("chat.chat"))