# 📄 AI-Powered README Generator

A FastAPI-based web application that automatically generates high-quality README files for any project using Groq LLMs. Upload your project files/folders and get a structured, professional README instantly.

---

## 🚀 Features

### 🔹 AI-Generated README

Automatically analyzes uploaded code files and generates:

* Project description
* Tech stack
* File and folder structure
* Code-level summaries
* Installation steps
* Usage instructions
* API endpoints (if applicable)

### 🔹 Multi-File & Folder Upload Support

* Upload single files, multiple files, or entire directories
* Preserves internal folder structure
* Supports multiple programming languages: `.py`, `.js`, `.html`, `.css`, `.md`, `.json`, etc.

### 🔹 Live Markdown Preview

* View the generated README instantly
* Copy or download the final Markdown file

### 🔹 FastAPI Backend + Groq LLM

* High-speed inference using Groq
* Clean and minimal REST API
* Handles file parsing, text processing, and summarization

---

## 🛠️ Tech Stack

### Backend

* Python 3.10+
* FastAPI
* Groq API
* Uvicorn
* Python Dotenv

### Frontend

* HTML
* CSS
* JavaScript (Vanilla)

### Other

* File handling with Python `os` and `shutil`
* Markdown generation

---

## 📂 Project Structure

```
Readme-Generator/
│── backend/
│   ├── main.py              # FastAPI backend
│   ├── uploads/             # Uploaded files stored here
│   ├── utils/               # File reading + README generation helpers
│
│── frontend/
│   ├── index.html           # Main UI
│   ├── script.js            # Handles upload + API requests
│   ├── style.css            # UI styles
│
│── .env                     # Groq API Key
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AshwinMadhav10/Readme-Generator.git
cd Readme-Generator
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Backend will start at:
**[http://localhost:8000](http://localhost:8000)**

### 6️⃣ Open the Frontend

Open `index.html` in your browser.

---

## 🧠 How It Works

1. User uploads files/folders
2. Backend extracts and validates files
3. Reads code and generates embeddings/prompts
4. Sends structured prompt to Groq LLM
5. LLM returns Markdown-formatted README
6. Frontend displays live preview
7. User downloads final README.md

---

## 📌 API Endpoints

### POST /generate-readme

Uploads files and generates README.
Returns Markdown text.

### GET /download

Downloads generated README file.

### GET /

Returns frontend HTML page.

---

## 🧪 Supported File Types

| Type       | Extensions |
| ---------- | ---------- |
| Python     | `.py`      |
| JavaScript | `.js`      |
| HTML       | `.html`    |
| CSS        | `.css`     |
| Markdown   | `.md`      |
| JSON       | `.json`    |

---

## 🎯 Future Enhancements (Planned)

* GitHub repo URL → Direct README generation
* Add OpenAI, Gemini, or LLaMA model support
* Dark mode UI
* File tree visualization
* Add Docker support

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to add features, fix bugs, or improve documentation, feel free to contribute.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Ashwin Madhav A**
Master of Computer Applications (MCA)
Developer • ML Beginner • Web Enthusiast
GitHub: [https://github.com/AshwinMadhav10](https://github.com/AshwinMadhav10)
