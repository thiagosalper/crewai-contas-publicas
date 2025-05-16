import os 

# os.environ["OPENAI_API_KEY"] = ""
os.environ["LLM_PROVIDER"] = "ollama"
os.environ["LLM_MODEL"] = "gemma3:1b"
os.environ["OLLAMA_BASE_URL"] = "http://localhost:11434"
os.environ["MODEL_NAME"] = "gemma3:1b"

from crewai import Agent, Task, Crew
from crewai_tools import CSVSearchTool
from langchain_ollama import OllamaLLM as Ollama



# llm = Ollama(model="ollama/gemma3:1b", base_url="http://localhost:11434")

# csv_tool = CSVSearchTool(csv='csv/small_despesas.csv')
csv_tool = FileReadTool(file_path='./csv/small_despesas.csv')

analyst = Agent(
    role="Analista de Dados",
    goal="Ler e interpretar dados brutos de despesas públicas a partir de um arquivo CSV.",
    backstory="Você é um expert em dados públicos e sabe extrair informações relevantes de planilhas.",
    verbose=True,
    tool=[csv_tool],
    # llm=llm
)


task1 = Task(
    description="Analise os dados de despesas públicas e identifique os principais fornecedores e valores pagos.",
    agent=analyst,
    expected_output="Valor total pago para cada fornecedor e quais as subfunções de despesa mais relevantes."
)

team = Crew(
    agents=[analyst],
    tasks=[task1],
    verbose=True
)

result = team.kickoff()
print(result)
