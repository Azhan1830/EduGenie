"""
export_utils.py

Utility functions for exporting chat history.
"""

import os
from datetime import datetime


def export_chat_as_txt(chat_history, export_folder):
    """
    Export chat history as a text file.
    """

    os.makedirs(export_folder, exist_ok=True)

    filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    filepath = os.path.join(export_folder, filename)

    with open(filepath, "w", encoding="utf-8") as file:

        file.write("EduGenie Chat Export\n")
        file.write("=" * 60)
        file.write("\n\n")

        for index, chat in enumerate(chat_history, start=1):

            file.write(f"Question {index}\n")
            file.write("-" * 40)
            file.write("\n")

            file.write(chat["question"])
            file.write("\n\n")

            file.write("Answer\n")
            file.write("-" * 40)
            file.write("\n")

            file.write(chat["answer"])
            file.write("\n\n")

            file.write("=" * 60)
            file.write("\n\n")

    return filepath