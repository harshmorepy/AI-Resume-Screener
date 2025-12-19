import re
import PyPDF2
from app.text_cleaner import clean_text


def extract_text(file_path):
    text = ""

    if file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "

    else:
        raise ValueError("Only PDF files are supported for now")

    return text


def load_skills(skills_file="data/skills.txt"):
    with open(skills_file, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]


def extract_skills(text, skills):
    text = clean_text(text)
    found_skills = set()

    for skill in skills:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return list(found_skills)
