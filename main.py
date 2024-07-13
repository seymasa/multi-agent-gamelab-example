from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import GameLabTasks
from agents import GameLabAgents

tasks = GameLabTasks()
agents = GameLabAgents()

print("## GameLab Ekibine Hoş Geldiniz")
print('-------------------------------')
game = input("Hangi oyunu yapmak istiyorsunuz? Mekanikler neler olacak?\n")

# Ajanları Oluştur
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Görevleri Oluştur
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Kopyadan Sorumlu Ekibi Oluştur
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        code_game,
        review_game,
        approve_game
    ],
    verbose=True
)

game = crew.kickoff()

print("\n\n########################")
print("## İşte Sonuç")
print("########################\n")
print("Oyunun son kodu:")
print(game)
