# generator/ai_model.py
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import random

# Download necessary NLTK data files (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

def generate_questions_from_text(text_content):
    sentences = sent_tokenize(text_content)

    # Process sentences, extract keywords, generate questions
    questions = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in stopwords.words('english')]

        if len(words) > 5:
            random.shuffle(words)
            question = f"What are the main concepts discussed in the following sentence? {' '.join(words[:5])}..."
            questions.append(question)

    return questions
