import pandas as pd
from crewai import Crew, Task 
from agents.data_reader_agent import data_reader_agent
from agents.analyst_agent import analyser_agent
from crewai_tools import FileReadTool, CSVSearchTool
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def carregar_prompt(nome_arquivo):
    with open(f"prompts/{nome_arquivo}", "r", encoding="utf-8") as f:
        return f.read()

df = pd.read_csv("csv/despesas.csv", encoding="utf-8")

# summary = df.describe(include="all").to_string()

amostra = df.head().to_string(index=False)



task1 = Task(
    # description=f"Analise os seguintes dados de despesas públicas:\n\n{amostra}\n\nIdentifique Nome do Fornecedor e Valor Pago até Hoje.",
    # description=carregar_prompt("data_reader_prompt.txt"),
    description=f"""
    Sua tarefa é analisar os dados de despesas municipais fornecidos no arquivo CSV.
    Você deve se concentrar nas seguintes colunas:
    - Nome Fornecedor
    - Dotação
    - Valor Pago
    - Nome da Subfunção
    Com base nisso, identifique:
    - As principais subfunções de despesa
    - Quais fornecedores receberam mais
    """,
    agent=data_reader_agent,
    expected_output="Valor total pago para cada fornecedor e quais as subfunções de despesa mais relevantes."
)

task2 = Task(
    # description="Com base na análise anterior, gere insights relevantes sobre os gastos do município. Destaque padrões, possíveis excessos e fornecedores concentradores.",
    description=carregar_prompt("analyst_prompt.txt"),
    agent=analyser_agent,
    output_file=f'output/report_{timestamp}.md',
    expected_output="Principais fornecedores e total pago para cada, principais subfunções que mais foram pagas."
)

crew = Crew(
    agents=[data_reader_agent, analyser_agent],
    tasks=[task1, task2],
    verbose=True
)

result = crew.kickoff()

# exemplo de tools para tratar csv
# https://www.youtube.com/watch?v=2Fu_GgS-Q4s