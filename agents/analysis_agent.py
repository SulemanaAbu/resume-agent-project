from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message


class AnalysisAgent(Agent):
    class ReceiveAndForwardBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)
            if msg:
                skills = msg.body
                print("AnalysisAgent received skills:", skills)

                # Forward to RecommendationAgent
                new_msg = Message(to="recommend@localhost")
                new_msg.set_metadata("performative", "inform")
                new_msg.body = skills

                await self.send(new_msg)
                print("AnalysisAgent forwarded skills")

    async def setup(self):
        print("AnalysisAgent started")
        self.add_behaviour(self.ReceiveAndForwardBehaviour())