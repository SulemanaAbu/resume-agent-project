from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
import spacy
import PyPDF2

nlp = spacy.load("en_core_web_sm")

def read_resume(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


def extract_skills(text):
    skills_db = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript",
    "react", "c++", "excel", "statistics",
    "api design", "databases", "linux", "networking",
    "security", "aws", "docker", "kubernetes",
    "mongodb", "flask", "c#", "graphql",
     "postgresql", "restapi", "mysql"
]
    found = [skill for skill in skills_db if skill in text.lower()]
    return list(set(found))


class ResumeAgent(Agent):
    class SendSkillsBehaviour(OneShotBehaviour):
        async def run(self):
            text = read_resume("data/sample_resume.pdf")
            skills = extract_skills(text)

            msg = Message(to="analysis@localhost")
            msg.set_metadata("performative", "inform")
            msg.body = ",".join(skills)

            await self.send(msg)
            print("ResumeAgent sent skills:", skills)

    async def setup(self):
        print("ResumeAgent started")
        self.add_behaviour(self.SendSkillsBehaviour())