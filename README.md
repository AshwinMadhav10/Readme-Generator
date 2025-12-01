# Plagiarism Checker
## Description
The Plagiarism Checker is a desktop application designed to compare the similarity between two text files. It utilizes the Term Frequency-Inverse Document Frequency (TF-IDF) approach and calculates the cosine similarity between pairs of documents to identify potential plagiarism.

## Features
* Simple and intuitive GUI for easy file selection and result viewing
* Visual representation of similarity scores using a gauge
* Step-by-step guide for new users
* Supports drag and drop file selection

## Tech Stack
* Python
* Tkinter (for GUI)
* PIL (for image processing)
* Scikit-learn (for text vectorization and similarity calculation)
* Base64 (for encoding and decoding)
* IO (for input/output operations)

## Folder Structure
The project consists of a single Python file `app.py` which contains all the necessary code for the application.

## File Details
The `app.py` file contains the following important functions:
* `vectorize(Text)`: converts text into numerical vectors using TF-IDF vectorizer
* `similarity(doc1, doc2)`: calculates the cosine similarity between two vectors
* `check_plagiarism(file1, file2)`: calculates the similarity score between two text files
* `analyze_plagiarism()`: analyzes the plagiarism between two selected files and displays the results
* `upload_files()`: opens a file dialog for the user to select two text files
* `update_file_display(file_paths)`: updates the file display area with the selected file information

The `app.py` file also contains the following important classes:
* `ModernButton`: a custom button class with a modern design
* `FileDropArea`: a custom file drop area class that allows users to drag and drop files
* `ResultGauge`: a custom gauge class that displays the similarity score visually

## API Endpoints
| Method | Route | Description |
| --- | --- | --- |
| None | None | This is a desktop application and does not have any endpoints |

## How It Works
1. The user selects two text files using the file dialog or by dragging and dropping them into the file drop area.
2. The application converts the text into numerical vectors using the TF-IDF vectorizer.
3. The application calculates the cosine similarity between the two vectors.
4. The application displays the similarity score and a visual representation of the score using a gauge.

## Installation
To run the project, you need to have Python and the required libraries installed. You can install the libraries using pip:
```bash
pip install tk PIL scikit-learn
```

## Running the project
To run the project, simply execute the `app.py` file:
```bash
python app.py
```

## Notes
* The application uses a simple and intuitive GUI to make it easy for users to select files and view the analysis results.
* The application uses a gauge to visually represent the similarity score, making it easy to understand the results at a glance.
* The application provides a step-by-step guide on how to use it, making it easy for new users to get started.
* The application requires the scikit-learn library to be installed.

## Conclusion
The Plagiarism Checker is a useful tool for detecting plagiarism between two text files. Its simple and intuitive GUI makes it easy to use, and its visual representation of similarity scores makes it easy to understand the results. With its step-by-step guide and drag and drop file selection, it is a great tool for anyone looking to detect plagiarism.