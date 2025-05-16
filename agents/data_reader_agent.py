from crewai import Agent
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM as Ollama
from crewai_tools import FileReadTool, CSVSearchTool
# from crewai.tools.csv_tools import CSVSearchTool

# llm = Ollama(model="ollama/llama3:latest", base_url="http://localhost:11434")
llm = Ollama(model="ollama/gemma3:1b", base_url="http://localhost:11434")


# tool = CSVSearchTool(csv='path/to/your/csvfile.csv')

csv_tool = FileReadTool(file_path='../csv/small_despesas.csv')

data_reader_agent = Agent(
    role="Especialista em dados governamentais",
    goal="Ler e interpretar dados brutos de despesas públicas.",
    backstory="Você é um expert em dados públicos e sabe extrair informações relevantes de planilhas.",
    verbose=True,
    llm=llm,
    tool=[csv_tool],
    allow_delegation=False,
    allow_code_execution=True
)