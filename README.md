# LEIA

## Descrição da ideia
Basicamente a ideia inicial é receber (ou scrapar) uma planilha com dados do Portal Transparencia Pública de um municipio, e utilizando Agentes para normalizar os dados e posterior Agentes para identificar padroes, gastos, e outras informações como se fossem especialistas.
Com os dados analisados, gerar e exportar relatórios resumidos e explicativos para leigos sobre como e onde foi gasto o dinheiro público daquele período daquele município.

## Características do Projeto
Usando Crewai, Ollama, Docker, Python, Portal Transparência

## Desafios
Inicialmente tentei usar a api da OpenAi mas a cota free não foi suficiente. Com isso, tentei algumas abordagens para injetar o uso de uma LLM local, usando Ollama.

Ainda estou ajustando os prompts e interação dos agentes e conexão local com Ollama, pois, a tools não funcionou como esperado.

wip
