def load_skills(file_path="data/skills.txt"):
    with open(file_path, "r") as f:
        skills = [line.strip().lower() for line in f.readlines()]
    return skills


def extract_skills(cleaned_text: str) -> list:
    skills_list = load_skills()
    found_skills = []

    for skill in skills_list:
        if skill in cleaned_text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))
