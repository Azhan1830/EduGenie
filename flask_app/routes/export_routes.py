from flask import (
    Blueprint,
    session,
    current_app,
    send_file,
    flash,
    redirect,
    url_for
)

import os

from utils.export_utils import export_chat_as_txt

export_bp = Blueprint("export", __name__)


@export_bp.route("/export_chat")
def export_chat():

    chat_history = session.get("chat_history", [])

    if not chat_history:

        flash("No chat history available to export.", "warning")
        return redirect(url_for("chat.chat"))

    export_folder = os.path.join(
        current_app.root_path,
        "exports"
    )

    filepath = export_chat_as_txt(
        chat_history,
        export_folder
    )

    return send_file(
        filepath,
        as_attachment=True,
        download_name=os.path.basename(filepath)
    )