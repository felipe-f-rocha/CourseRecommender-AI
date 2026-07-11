# CourseRecommender AI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/AI-Gemini-green)

> A Python application that recommends real courses based on interests, education level, and desired course level using Google Gemini AI and automatic link validation.

## Overview

CourseRecommender AI is a Streamlit-based web application that helps users find relevant and trustworthy online courses. Based on a few basic inputs, the system sends a prompt to Gemini, receives course suggestions, and validates whether the returned links still work.

## Features

- Interactive Streamlit form to collect:
  - area of interest
  - education level
  - desired course level
- Course recommendations generated with the Gemini model
- Use of Google search grounding to improve response quality
- Automatic link validation with fallback to a Google search when a link is unavailable
- Error handling for invalid input, API failures, and configuration issues

## How it works

The application flow is straightforward:

1. The user provides their area of interest, education level, and course level.
2. The service layer builds a prompt for Gemini.
3. The Gemini client generates course suggestions.
4. The parser structures the response into a usable format.
5. Validation checks the links and replaces them with a Google search when needed.
6. Results are displayed in the Streamlit interface.

## Technologies

- Python 3.11+
- Streamlit
- Google Gemini API
- Requests
- pytest

## Project structure

- config/: credential loading and access
- domain/: domain validation and exceptions
- infrastructure/: Gemini integration, parsing, validation, and prompt building
- presentation/: user-facing error message handling
- services/: recommendation orchestration
- main.py: Streamlit application entry point
- tests/: automated tests

## Setup

### 1. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure credentials

Copy the example file and fill in your keys:

```bash
copy secrets_example.toml secrets.toml
```

The file should contain:

```toml
[GEMINI]
GEMINI_API_KEY="your_api_key"
GEMINI_MODEL="primary_model"
FALLBACK_MODEL="secondary_model"
```

## Running the app

```bash
streamlit run main.py
```

## Tests

```bash
pytest
```

## License

This project is licensed under the MIT License.