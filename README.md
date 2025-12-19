📄 README.md

# AI Resume Screener 🔍

An ATS-style resume skill extractor built using Python.  
This project parses resumes in PDF format and extracts relevant technical skills using rule-based matching, simulating real Applicant Tracking Systems (ATS).

---

## 🚀 Features

- PDF resume text extraction
- Text cleaning and normalization
- Skill extraction using predefined skill list
- ATS-style rule-based matching
- Clean and readable output

---

## 🛠 Tech Stack

- Python 3
- PyPDF2
- Regular Expressions (Regex)

---

## 📂 Project Structure

AI-Resume-Screener/
│
├── app/
│ ├── resume_parser.py
│ ├── text_cleaner.py
│
├── data/
│ └── skills.txt
│
├── test_parser.py
├── README.md
└── .gitignore


---

## ⚙️ Installation
 
1. Clone the repository:
```bash
git clone https://github.com/your-username/AI-Resume-Screener.git
cd AI-Resume-Screener

2. Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install PyPDF2

▶️ Usage
1. Place your resume PDF in the project root (e.g. Resume.pdf)
2. Run the parser:

python3 test_parser.py

✅ Sample Output:

===== EXTRACTED SKILLS =====
- python
- java
- mongodb
- mysql
- django
- git

🧠 How It Works
Extracts raw text from PDF resumes
Cleans and normalizes text
Matches skills using keyword-based logic
Outputs extracted skills

📌 Use Cases
Resume screening
ATS simulation
Placement projects
NLP learning
HR-tech prototypes

🔮 Future Enhancements
Resume vs Job Description matching
AI-based skill inference
OCR support for scanned resumes
Web interface using FastAPI

👨‍💻 Author
Harsh More
BTech CSE Student
Python & Backend Enthusiast

---

# ✅ STEP 3: Save the File

Make sure:
- File name is `README.md`
- Saved in **project root**

---

# ✅ STEP 4: Commit README to GitHub

Now in Terminal:

```bash
git add README.md
git commit -m "Add project README"
git push
