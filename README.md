# PLAGARISM ANALYSER USING NLP :
      A web-based plagiarism detection tool built using Natural Language Processing (NLP) and TF-IDF cosine similarity. This project helps users analyze text and detect similarities with existing documents using a simple and interactive UI.
---
## PROJECT OVERVIEW :
      The Plagiarism Analyzer identifies how much of the input text is similar to predefined documents using:
        - TF-IDF Vectorization
        - Cosine Similarity
        - Flask Backend
        - Chart.js for visualization
      The tool outputs:
        - Overall plagiarism percentage
        - Detailed similarity report for each document
        - Doughnut chart showing plagiarized vs unique content
---
## DEMO OUPUT :
     Below is a preview of the OUTPUT:
     ![OUTPUT](https://github.com/user-attachments/assets/ad2b0360-e6a5-4aea-b3f9-82f9bf116f08)
---
## FEATURES :
    - Paste text and check plagiarism instantly  
    - F-IDF & cosine similarity-based NLP analysis  
    - Clean & interactive UI with Chart.js visualization  
    - Detailed similarity breakdown  
    - Lightweight Flask API  
    - Easy to extend with more documents
## PROJECT STRUCTURE :
      PLAGARISM_ANALYSER/
      │
      ├── app.py
      ├── requirements.txt
      │
      ├── templates/
      │   └── index.html
      │
      └── static/
          ├── style.css
          └── script.js
---
## HOW IT WORKS :
    1. User enters text  
    2. Text is appended to the existing CORPUS  
    3. TF-IDF vectorization converts all documents into vectors  
    4. Cosine similarity compares user text with each document  
    5. Maximum similarity value becomes the **plagiarism percentage**  
    6. Chart.js visualizes the results  
---
## COMMANDS USED :
    - python -m venv venv
    - venv\Scripts\activate
    - pip install -r requirements.txt
    - python app.py
    - git init
    - git remote add
    - git add <filename>
    - git commit -m "message"
    - git push origin main
---
## FRONTEND TECHNOLOGIES :
    - HTML5
    - CSS3
    - JavaScript
    - Chart.js
---
## BACKEND TECHNOLOGIES :
    - Flask
    - Scikit-Learn (TF-IDF)
    - NumPy
    - NLTK
---
## PROJECT OVERVIEW :
    The Plagarism Analyzer is a web-based application with NLP that compares two pieces of text and calculates how similar they are. It helps identify potential plagiarism by analyzing the text content and generating a similarity percentage.
    The application allows users to:
        - Upload two text files or enter text manually
        - Process both inputs using a Python backend
        - Compare the text using a similarity algorithm
        - Display a clean and easy-to-read plagiarism result on the webpage
    This project demonstrates practical skills in Python, Flask, HTML/CSS, and text-processing algorithms. It also showcases your understanding of file handling, web development, and Git/GitHub project workflow. The tool is simple, fast, and useful for students, teachers, and content creators who want to check how closely two documents match.
---
## PURPOSE OF THE PROJECT :
    The purpose of this project is to build a simple and effective tool that can detect plagiarism by comparing two pieces of text. It aims to help users identify how much content is similar, copied, or rewritten by analyzing text using Python and string similarity techniques.
    This project demonstrates:
      - How text similarity works in real-world applications
      - How to process and compare documents or written content
      - How to build a complete web application using Python + Flask + HTML/CSS
      - How to handle file uploads and backend processing
      - How to present results clearly on a webpage
    Overall, the project is designed to show your ability to combine web development, Python programming, and text analysis, making it a strong mini-project for portfolios, academic submissions, and HR technical evaluations.
---
## CONCLUSION :
    This project successfully analyzes Daily Public Transport Passenger Journeys using Python and time-series forecasting techniques. Through data cleaning, visualization, and model building, we were able to understand travel trends, identify usage patterns across different transport services, and generate future journey predictions.
    The insights gained from this analysis can help transport authorities make data-driven decisions such as optimizing schedules, allocating resources efficiently, and improving overall service quality. 
    Overall, the project demonstrates the practical use of data analysis, visualization, and forecasting models to solve a real-world operational problem and provide meaningful business intelligence for public transport planning.
--- 
## OUTPUT :
    The project generates a plagiarism analysis report based on the text entered by the user. After processing the text, the system displays:
        - Overall plagiarism percentage in a clean and visually appealing donut chart.
        - Color-coded sections showing plagiarized (red) and unique (green) content.
        - Document-wise similarity breakdown, listing how much of the text matches other documents.
        - A clear and interactive web interface that helps users quickly understand the originality of their content.
    This output helps users easily identify copied sections and evaluate the uniqueness of their text.
