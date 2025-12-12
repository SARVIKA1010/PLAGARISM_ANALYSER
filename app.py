from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Example corpus (you can expand this)
CORPUS = [
    "This is an example document about NLP.",
    "Machine learning techniques are used in plagiarism detection.",
    "Plagiarism analyzer can detect copied text using NLP.",
    "Natural Language Processing is useful for text analysis."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Add user text to corpus
    documents = CORPUS + [text]

    # TF-IDF and cosine similarity
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity([vectors[-1]], vectors[:-1])
    max_sim = max(cosine_sim[0])
    plagiarism_percentage = round(max_sim * 100, 2)

    # Detailed report
    detailed_report = []
    for idx, score in enumerate(cosine_sim[0]):
        if score > 0.1:
            detailed_report.append({
                'source': f"Document {idx+1}",
                'similarity': f"{round(score*100, 2)}%"
            })

    return jsonify({
        'plagiarismPercentage': plagiarism_percentage,
        'detailedReport': detailed_report
    })

if __name__ == '__main__':
    app.run(debug=True)