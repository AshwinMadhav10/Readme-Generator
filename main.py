from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import os
import shutil
from groq import Groq
from dotenv import load_dotenv

app = FastAPI()

SAVE_DIR = "uploads"
os.makedirs(SAVE_DIR, exist_ok=True)

ALLOWED_EXT = {".py", ".js", ".html", ".css", ".md", ".json"}


@app.get("/")
def htmlpage():
    return FileResponse("index.html")


def read_text_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    return None



def clear_uploads():
    if os.path.exists(SAVE_DIR):
        shutil.rmtree(SAVE_DIR)
    os.makedirs(SAVE_DIR, exist_ok=True)



@app.post("/save")
async def save(files: list[UploadFile] = File(...)):

    clear_uploads() 
    saved_paths = []

    for file in files:
        file_path = os.path.join(SAVE_DIR, file.filename)

        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)

        saved_paths.append(file_path)

    return {"message": "Uploaded", "saved_paths": saved_paths}




@app.get("/get_all_files")
def get_all_files():

    file_list = []

    for root, dirs, files in os.walk(SAVE_DIR):
        for fname in files:
            file_list.append(os.path.join(root, fname))

    return {"total_files": len(file_list), "files": file_list}




@app.post("/model")
def analyze_files():
    load_dotenv()
    APIKEY=os.getenv("APIKEY")

    open("store.txt", "w").close()

    client = Groq(api_key=APIKEY)

    results = {}

    for root, dirs, files in os.walk(SAVE_DIR):
        for fname in files:

            ext = os.path.splitext(fname)[1].lower()
            if ext not in ALLOWED_EXT:
                continue

            path = os.path.join(root, fname)
            content = read_text_file(path)

            if content is None:
                results[fname] = "Cannot read this file."
                continue

            user_message = f"""
FILE: {fname}

CONTENT:
{content}
"""

            system_prompt = """
You are a project file analyzer. For each file, extract:

FILE: <filename>

TECH STACK USED:
- list

WORKING / LOGIC SUMMARY:
- summary

IMPORTANT FUNCTIONS:
- function: description

IMPORTANT CLASSES:
- class: description

ENDPOINTS (if any):
| Method | Route | Description |

NOTES:
- other important points

Do not generate README. Only file-level summary.
"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.1,
                max_completion_tokens=800
            )

            summary = response.choices[0].message.content
            results[fname] = summary

            with open("store.txt", "a", encoding="utf-8") as f:
                f.write(summary + "\n\n------------------------------------\n\n")

    return {"analysis": results}


@app.post("/generate-readme")
def generate_readme():
    load_dotenv()
    APIKEY=os.getenv("APIKEY")

    client = Groq(api_key=APIKEY)

    if not os.path.exists("store.txt"):
        return JSONResponse({"error": "store.txt not found."})

    if os.path.getsize("store.txt") == 0:
        return JSONResponse({"error": "store.txt is empty."})

    with open("store.txt", "r", encoding="utf-8") as f:
        summaries = f.read()

    prompt = f"""
You are an expert technical writer. Generate a perfect README.md using the following project file summaries:

{summaries}

README MUST INCLUDE:

# Project Title
# Description
# Features
# Tech Stack
# Folder Structure
# File Details (from summaries)
# API Endpoints (if any)
# How It Works
# Installation
# Running the project
# Notes
# Conclusion

Return only valid Markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_completion_tokens=1500
    )

    readme_text = response.choices[0].message.content

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_text)

    return FileResponse("README.md", filename="README.md")
