# CourseRecommender AI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Gemini-green)

> Descubra cursos ideais com inteligência artificial, validação automática de links e interface web moderna.

## Oque é e qual o príncipio do projeto?

> Encontrar cursos de qualidade na internet não é difícil, difícil é separar o que realmente vale a pena do que é repetitivo, desatualizado ou simplesmente não funciona.

O **CourseRecommender AI** foi criado para resolver exatamente esse problema.

A partir de uma área de interesse e nível do usuário, o sistema utiliza **IA generativa (Google Gemini)** para identificar
cursos relevantes, validar automaticamente os links e garantir que o usuário tenha acesso a opções reais, acessíveis e utilizáveis,
sem perder tempo com páginas quebradas ou recomendações genéricas.

O projeto surgiu da necessidade prática de filtrar conteúdo educacional confiável em meio a um volume massivo de opções
inconsistentes na internet, transformando uma busca manual e incerta em uma experiência rápida, inteligente e orientada.

## ⚡ Como funciona
1. **IA Generativa**: Gera recomendações de cursos personalizadas conforme área e nível do usuário (Google Gemini).
2. **Validação Automática**: Todos os links são testados em paralelo para garantir que funcionam.
3. **Fallback Inteligente**: Se um link estiver quebrado, o sistema sugere automaticamente uma busca alternativa no Google.

## Tecnologias Utilizadas
- **Python 3.11+**
- **Google Generative AI (Gemini)**
- **Streamlit** (interface web)
- **Requests** (validação de links)
- **python-dotenv** (gestão de variáveis de ambiente)
- **ThreadPoolExecutor** (concorrência para validação)

## Instalação
1. Clone este repositório:
```powershell
git clone <url-do-repositorio>
```
2. Instale as dependências:
```powershell
pip install -r requirements.txt
```
3. Crie um arquivo `.env` com sua chave da API Gemini:
```
GEMINI_API_KEY=your_key
GEMINI_MODEL=your_model
```

## Uso
Execute a interface web:
```powershell
streamlit run main.py
```
Ou apenas o backend (para integração com outras aplicações):
```powershell
python backend.py
```

## API e Fluxo de Uso
- O backend expõe funções para recomendação de cursos via IA.
- A interface coleta área e nível do usuário, chama o backend e exibe recomendações.
- Exemplo de chamada direta (Python):
```python
import backend as b
cursos = b.formar_prompt('Data Science', 5)
print(cursos)
```
- Cada curso recomendado inclui: Nome, Plataforma, Link validado e um breve texto.

## Diferenciais
- Recomendações reais, com links validados automaticamente.
- Uso de IA generativa para personalização.
- Interface web amigável e pronta para deploy.
- Fácil integração com outros sistemas Python.

## Estrutura do Projeto
- `backend.py`: Lógica principal, integração com IA e validação de links.
- `interface.py`: Interface web (Streamlit).
- `requirements.txt`: Dependências do projeto.

## Licença
MIT License

