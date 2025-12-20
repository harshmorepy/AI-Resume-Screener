🧠 AI Resume Screener (Python)
An AI-powered resume screening tool built using Python that extracts technical skills from resumes (PDF/DOCX) to help automate the initial resume shortlisting process.
This project demonstrates text extraction, cleaning, and keyword-based skill matching, making it suitable for ATS-style screening systems.

🚀 Features:
📄 Supports PDF resumes
🧹 Cleans raw resume text automatically
🧠 Extracts technical skills like:
Python, Java, Git, GitHub
Django, Flask
MySQL, MongoDB
AWS, etc.

🧪 Includes a sample resume for demo/testing
⚙️ Easy to extend with NLP or ML models

📁 Project Structure:
AI-RESUME-SCREENER/
│
├── app/
│   ├── resume_parser.py     # Core logic for text + skill extraction
│
├── Samples/
│   └── Sample_resume.pdf    # Sample resume for testing
│
├── test_parser.py           # Script to run and test the parser
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore

🛠️ Tech Stack
Python 3
pdfplumber
python-docx
re (Regular Expressions)

⚙️ Installation & Setup

1️⃣ Clone the repository:
git clone https://github.com/<your-username>/AI-Resume-Screener.git
cd AI-Resume-Screener

2️⃣ Create virtual environment:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies:
pip install -r requirements.txt

▶️ How to Run the Project
1.Place a resume inside the Samples/ folder
  (A sample PDF is already provided)
2.Run the test script:
  python3 test_parser.py

✅ Sample Output:
===== EXTRACTED SKILLS =====
- python
- java
- git
- github
- django
- flask
- mysql
- mongodb
- aws

📌 Use Case
This project can be used as:
A base for ATS (Applicant Tracking Systems)
Resume shortlisting tools
HR automation systems
NLP/ML resume ranking systems (future scope)

🔮 Future Improvements
Add NLP-based skill extraction using spaCy
Resume–Job Description matching
Skill scoring & ranking
Web interface using Flask or Django
CSV/JSON export of extracted data

👨‍💻 Author
Harsh More
🎓 B.Tech Student
🐍 Python Enthusiast
💡 Interested in AI, Automation & Backend Development

⭐ If you like this project
Give it a ⭐ on GitHub — it motivates me to build more!