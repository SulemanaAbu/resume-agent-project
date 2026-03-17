import asyncio
from agents.resume_agent import ResumeAgent
from agents.analysis_agent import AnalysisAgent
from agents.recommendation_agent import RecommendationAgent


async def main():
    # Create agents
    analysis_agent = AnalysisAgent("analysis@localhost", "password")
    recommendation_agent = RecommendationAgent("recommend@localhost", "password")
    resume_agent = ResumeAgent("resume@localhost", "password")

    # Start receiving agents FIRST
    await analysis_agent.start()
    await recommendation_agent.start()

    print("Waiting for agents to initialize...")
    await asyncio.sleep(10)

    # Start sender AFTER
    await resume_agent.start()

    # Let them communicate
    await asyncio.sleep(15)

    # Stop all agents
    await resume_agent.stop()
    await analysis_agent.stop()
    await recommendation_agent.stop()


if __name__ == "__main__":
    asyncio.run(main())