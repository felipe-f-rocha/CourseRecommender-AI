# CourseRecommender AI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Gemini-green)

> Sistema inteligente de recomendação de cursos usando IA generativa, validação automática de links e arquitetura modular.

---

## Visão Geral

O CourseRecommender AI resolve o problema de encontrar cursos confiáveis na internet.

Ele usa IA (Google Gemini) para gerar recomendações personalizadas e valida automaticamente os links.

---

## Como Funciona

Fluxo do sistema:

````
Streamlit (UI)  
↓  
Service Layer (orquestração)  
↓  
Domain Layer (regras e validação)  
↓  
Infrastructure Layer (Gemini + requests)  
↓  
Resposta formatada e exibida  

````


---

## Arquitetura

### UI (Streamlit)
- Entrada de dados
  - Exibição de resultados
  - Exibição de erros

### Service Layer
- Orquestra todo o fluxo
  - Controla fallback
  - Gerencia chamadas de IA
  - Coordena validação e parsing

### Domain Layer
- Regras de validação
  - Estrutura de dados (Curso)
  - Parsing da resposta da IA

### Infrastructure Layer
- Integração com Gemini API
  - Requisições HTTP
  - Validação de URLs

### Config
- Chaves de API
  - Modelos Gemini
  - Fallback settings

---

## Funcionalidades

````
- Validação automática de links
- Sistema de fallback de modelo
- Validação paralela de URLs
- Arquitetura modular
````


---

## 🛡 Tratamento de Erros

### Infraestrutura
- 429 → ativa fallback
  - 5xx → retry/fallback
  - 403 → erro de configuração

### UI
- Mostra erros amigáveis
  - Não decide lógica de recuperação

### Service
- Decide fallback
  - Controla retry
  - Propaga erros tratados

---

## Fallback

### Link
Se o link estiver quebrado, substitui por busca no Google.

---

## Tecnologias

- Python 3.11+
  - Google Gemini API
  - Streamlit
  - Requests
  - python-dotenv
  - ThreadPoolExecutor

---

# Estrutura do Projeto

    config/
    infra/
    domain/
    service/
    ui/
    
    main.py
    requirements.txt
    README.md

---
# Licença

MIT License