from crewai import Agent
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM as Ollama
# from tools.save_to_markdown_tool import SaveToMarkdownTool
from crewai_tools import (
    FileReadTool,
    DirectoryReadTool
)

docs_tool = DirectoryReadTool(directory='./output')
file_tool = FileReadTool()

# llm_extracao = Ollama(model="ollama/llama3:latest", base_url="http://localhost:11434")
llm_extracao = Ollama(model="ollama/gemma3:1b", base_url="http://localhost:11434")

# save_tool = SaveToMarkdownTool(
#     title="analyst_output.md",
#     content="aqui o conteúdo do relatório",
# )

analyser_agent = Agent(
    role="Analista de finanças públicas",
    goal="Gerar insights estratégicos com base nas despesas municipais e salvar usando o SaveToMarkdownTool.",
    backstory="Você é um especialista em contas públicas e orçamento, capaz de identificar padrões e anomalias nos dados.",
    llm=llm_extracao,
    tools=[docs_tool, file_tool],
    allow_delegation=False,
    verbose=True
)