# generator/generate_questions.py
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from docx import Document

# Ensure SentencePiece is installed
try:
    import sentencepiece
except ImportError:
    print("SentencePiece is not installed. Installing now...")
    import os
    os.system('pip install sentencepiece')

# Load the model and tokenizer
model_name = "ramsrigouthamg/t5_squad_v1"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to read text from a .docx file
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Function to generate questions
def generate_questions(context, num_questions=5, question_type="short", max_length=50):
    num_beams = max(5, num_questions)  # Ensure num_beams is at least 5
    input_text = f"generate {question_type} questions: {context} </s>"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    outputs = model.generate(input_ids, max_length=max_length, num_return_sequences=num_questions, num_beams=num_beams, early_stopping=True)

    questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return questions
