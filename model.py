# model.py

from langchain_huggingface import HuggingFaceEndpoint
from config import HUGGINGFACE_TOKEN

# Set up Hugging Face model endpoint
def get_model(repo_id="mistralai/Mistral-7B-Instruct-v0.2", max_length=128, temperature=0.7):
    return HuggingFaceEndpoint(repo_id=repo_id, 
                               max_length=max_length, 
                               temperature=temperature, 
                               token=HUGGINGFACE_TOKEN)
