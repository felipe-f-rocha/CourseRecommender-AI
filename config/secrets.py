import streamlit as st
import tomllib
from pathlib import Path
from domain.exceptions import ConfigurationError

def get_secrets():
    api_key = None
    model = None
    fallback_model = None

    # 1. Try the local file
    try:
        base_dir = Path(__file__).resolve().parent.parent
        file_path = base_dir / "secrets.toml"

        with open(file_path, "rb") as f:
            config = tomllib.load(f)

        api_key = config["GEMINI"]["GEMINI_API_KEY"]
        model = config["GEMINI"]["GEMINI_MODEL"]
        fallback_model = config["GEMINI"]["FALLBACK_MODEL"]

    except (FileNotFoundError, KeyError):
        pass  # fallback will be used

    # 2. fallback Streamlit
    if not api_key or not model:
        try:
            api_key = st.secrets["GEMINI"]["GEMINI_API_KEY"]
            model = st.secrets["GEMINI"]["GEMINI_MODEL"]
            fallback_model = st.secrets["GEMINI"]["FALLBACK_MODEL"]
        except Exception:
            pass

    # 3. Final validation
    if not api_key:
        raise ConfigurationError("GEMINI_API_KEY not found")

    if not model:
        raise ConfigurationError("GEMINI_MODEL not found")

    if not fallback_model:
        raise ConfigurationError("FALLBACK_MODEL not found")

    return api_key, model, fallback_model