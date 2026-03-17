import spacy
import PyPDF2

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# === PERCEIVE ===
def read_resume(file_path):
    text = ""

    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    else:
        with open(file_path, "r") as file:
            text = file.read()

    return text


# === DECIDE ===
def extract_skills(text):
    doc = nlp(text.lower())

    skills_db = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript",
    "react", "c++", "excel", "statistics",
    "apis", "databases", "linux", "networking",
    "security", "aws", "docker", "kubernetes",
    "mongodb", "flask", "c#"
    ]

    found_skills = []

    for skill in skills_db:
        if skill in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))


# === DECISION: CAREER LOGIC ===
def recommend_career(skills):
    if "python" in skills and "machine learning" in skills:
        return "Machine Learning Engineer"
    elif "python" in skills and "sql" in skills:
        return "Data Analyst"
    elif "html" in skills and "css" in skills:
        return "Web Developer"
    elif "java" in skills:
        return "Software Developer"
    else:
        return "General IT Role"


# === NEW: SKILL GAP ANALYSIS ===
def skill_gap_analysis(career, skills):
    career_requirements = {
        "Data Analyst": ["python", "sql", "data analysis", "excel", "statistics"],
        "Machine Learning Engineer": ["python", "machine learning", "statistics", "deep learning"],
        "Backend Developer": ["java", "sql", "apis", "databases"],
        "Web Developer": ["html", "css", "javascript", "react"],
        "Cybersecurity Analyst": ["networking", "security", "linux", "python"],
        "Mobile App Developer": ["java", "kotlin", "flutter", "android", "flask"],
        "Cloud Engineer": ["aws", "docker", "kubernetes", "linux", "azure"]
    }

    required = career_requirements.get(career, [])
    missing = [skill for skill in required if skill not in skills]

    return missing


# === ACT ===
def display_results(skills, career, gaps):
    print("\n[Agent Output]\n")
    print("Detected Skills:", skills)
    print("Recommended Career:", career)
    print("Skill Gaps:", gaps)


# === MAIN AGENT LOOP ===
def agent_loop(file_path):
    print("\n[Agent Started]\n")

    # Perceive
    resume_text = read_resume(file_path)

    # Decide
    skills = extract_skills(resume_text)
    career = recommend_career(skills)
    gaps = skill_gap_analysis(career, skills)

    # Act
    display_results(skills, career, gaps)


if __name__ == "__main__":
    agent_loop("data/sample_resume.pdf")