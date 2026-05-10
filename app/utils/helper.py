import os
from dotenv import load_dotenv

load_dotenv()


def get_env_variable(variable_name):
    """
    Fetch environment variable safely.
    """
    value = os.getenv(variable_name)

    if value is None:
        raise ValueError(f"{variable_name} is not set")

    return value


def chunk_text(text, chunk_size=500):
    """
    Split text into smaller chunks.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks