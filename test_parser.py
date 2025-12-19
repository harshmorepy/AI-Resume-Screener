from app.resume_parser import extract_text, load_skills, extract_skills

RESUME_PATH = "Resume.pdf"

def main():
    print("🔍 Reading resume...")

    # 1️⃣ Extract resume text
    resume_text = extract_text(RESUME_PATH)

    # 🔎 DEBUG: Check extracted text
    print("\n===== RAW RESUME TEXT (first 500 chars) =====")
    print(resume_text[:500])

    # 2️⃣ Load skills
    skills = load_skills("data/skills.txt")

    # 3️⃣ Extract skills
    found_skills = extract_skills(resume_text, skills)

    print("\n===== EXTRACTED SKILLS =====")

    if found_skills:
        for skill in sorted(found_skills):
            print(f"- {skill}")
    else:
        print("❌ No skills found")

if __name__ == "__main__":
    main()
