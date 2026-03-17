from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


# ==============================
# CAREER DATABASE
# ==============================
def get_career_database():
    return {
        "Data Analyst": ["python", "sql", "data analysis", "excel", "statistics"],
        "Machine Learning Engineer": ["python", "machine learning", "statistics", "deep learning"],
        "Backend Developer": ["java", "sql", "apis", "databases"],
        "Web Developer": ["html", "css", "javascript", "react"],
        "Cybersecurity Analyst": ["networking", "security", "linux", "python"],
        "Mobile App Developer": ["java", "kotlin", "flutter", "android", "flask"],
        "Cloud Engineer": ["aws", "docker", "kubernetes", "linux", "azure"]
    }


# ==============================
# ANALYSIS FUNCTION
# ==============================
def analyze_careers(skills):
    skills = [s.strip() for s in skills.split(",")]
    db = get_career_database()

    results = []

    for career, required_skills in db.items():
        matched = [s for s in skills if s in required_skills]
        missing = [s for s in required_skills if s not in skills]

        score = len(matched)

        results.append({
            "career": career,
            "matched": matched,
            "missing": missing,
            "score": score
        })

    # Sort by best match
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:3]  # Top 3 careers


# ==============================
# AGENT CLASS
# ==============================
class RecommendationAgent(Agent):

    class ReceiveBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)
            if msg:
                skills = msg.body
                print("RecommendationAgent received:", skills)

                results = analyze_careers(skills)

                print("\n===== RESUME ANALYSIS REPORT =====\n")
                print(f"Detected Skills: {skills}\n")

                for i, res in enumerate(results, start=1):
                    print(f"Option {i}: {res['career']}")
                    print(f"Matched Skills: {res['matched']}")
                    print(f"Missing Skills: {res['missing']}")
                    print("-" * 40)

                print("\n=================================\n")

    async def setup(self):
        print("RecommendationAgent started")
        self.add_behaviour(self.ReceiveBehaviour())