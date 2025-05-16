from crewai.tools import BaseTool
from pydantic import Field
import datetime

class SaveToMarkdownTool(BaseTool):
    name: str = "SaveToMarkdownTool"
    description: str = "Salva um texto em um arquivo markdown com título e conteúdo fornecidos"
    
    title: str = Field(..., description="Título do relatório")
    content: str = Field(..., description="Conteúdo do relatório em texto")

    # def save_evaluation(self, evaluation_result: str) -> str:
    #     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    #     filename = f"avaliacao_{timestamp}.md"
        
    #     with open(filename, "w", encoding="utf-8") as f:
    #         f.write(f"# Avaliação\n\n")
    #         f.write(evaluation_result)

    #     return f"Avaliação salva em {filename}"

    def _run(self) -> str:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"relatorio_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {self.title}\n\n")
            f.write(self.content)

        return f"Relatório salvo em {filename}"
        