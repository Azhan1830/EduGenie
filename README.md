# 📚 EduGenie - AI Powered PDF Learning Assistant

EduGenie is an AI-powered PDF Question Answering application that allows users to upload one or more PDF documents and interact with them using natural language. The application uses Retrieval-Augmented Generation (RAG) with Google's Gemini AI and FAISS vector search to provide accurate, context-aware answers based only on the uploaded documents.

---

## 🚀 Features

- 📄 Upload one or multiple PDF documents
- 🧠 AI-powered question answering using Google Gemini
- 🔍 FAISS vector database for fast semantic search
- ✂️ Automatic text chunking
- 📌 Context-aware responses using RAG
- 💬 Chat history maintained during the session
- 🗑️ Delete uploaded PDF documents
- 📤 Export chat history as a text file
- 🎨 Modern Bootstrap-based responsive UI
- ⚡ Flask Blueprint architecture

---

# 🏗️ Project Architecture

```
EduGenie/
│
├── flask_app/
│   ├── app.py
│   ├── config.py
│   │
│   ├── routes/
│   │     ├── main_routes.py
│   │     ├── upload_routes.py
│   │     ├── chat_routes.py
│   │     └── export_routes.py
│   │
│   ├── templates/
│   │     ├── base.html
│   │     ├── index.html
│   │     ├── upload.html
│   │     └── chat.html
│   │
│   ├── static/
│   │     ├── css/
│   │     ├── js/
│   │     └── images/
│   │
│   ├── utils/
│   │     ├── pdf_loader.py
│   │     ├── text_splitter.py
│   │     ├── embeddings.py
│   │     ├── vector_store.py
│   │     ├── retriever.py
│   │     ├── rag_pipeline.py
│   │     ├── llm.py
│   │     ├── qa_pipeline.py
│   │     └── export_utils.py
│   │
│   ├── uploads/
│   ├── exports/
│   └── vector_db/
│
├── notebooks/
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

### Backend

- Python
- Flask
- Flask Blueprints

### AI & Machine Learning

- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- FAISS
- Sentence Transformers

### PDF Processing

- PyPDF2
- LangChain Text Splitter

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- JavaScript

---

# ⚙️ How It Works

1. User uploads one or more PDF files.
2. PDFs are processed and converted into plain text.
3. Text is split into smaller chunks.
4. Embeddings are generated.
5. Embeddings are stored in a FAISS vector database.
6. User asks a question.
7. Relevant document chunks are retrieved.
8. Retrieved context is sent to Gemini AI.
9. Gemini generates an answer based on the retrieved context.
10. The answer is displayed and stored in chat history.

---

# 📷 Application Workflow

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
Ask Question
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Gemini AI
      │
      ▼
Display Answer
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/EduGenie.git

cd EduGenie
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside `flask_app/`

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Application

```bash
cd flask_app

python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📖 Usage

### Step 1

Upload one or more PDF files.

### Step 2

Wait until the vector database is created.

### Step 3

Navigate to **AI Chat**.

### Step 4

Ask questions related to the uploaded PDFs.

### Step 5

View AI-generated answers.

### Step 6

Export your chat history if needed.

---

# 📁 Main Modules

| Module | Purpose |
|---------|----------|
| pdf_loader.py | Extracts text from PDFs |
| text_splitter.py | Splits text into chunks |
| embeddings.py | Creates embeddings |
| vector_store.py | Stores vectors in FAISS |
| retriever.py | Retrieves relevant chunks |
| rag_pipeline.py | RAG workflow |
| llm.py | Gemini integration |
| qa_pipeline.py | Generates final responses |
| export_utils.py | Exports chat history |

---

# ✨ Key Features

- Multiple PDF Support
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- FAISS Vector Database
- Gemini AI Integration
- Session Chat History
- Export Chat
- Delete Uploaded PDFs
- Responsive User Interface
- Modular Flask Blueprints

---

# 📌 Future Enhancements

- User Authentication
- Database Integration
- Persistent Chat History
- Voice-based Queries
- Image Extraction from PDFs
- OCR Support
- Multi-language Support
- Citation-Based Answers
- Dark/Light Theme Toggle

---

# 👨‍💻 Author

**Azhan Rizwan**

B.Tech in Artificial Intelligence & Machine Learning

---

# 📜 License

This project is developed for educational and learning purposes.

Feel free to modify and extend it for personal or academic use.

---

# ⭐ Acknowledgements

- Google Gemini AI
- Flask
- FAISS
- LangChain
- Bootstrap
- Python Community