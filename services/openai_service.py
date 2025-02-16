import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment="gpt-4o",
            api_version="2024-10-21"
        )
    
    def chat_completion(self, system_prompt, user_prompt, temperature=0.7, max_tokens=16000, model="o1-mini"):
        
        if model == "gpt-4o":
            self.client = AzureOpenAI(
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                azure_deployment="gpt-4o",
                api_version="2024-10-21"
            )
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
        elif model == "o1-mini":
            self.client = AzureOpenAI(
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                azure_deployment="o1-mini",
                # api_version="2024-10-21"
                api_version="2024-12-01-preview"
            )
            response = self.client.chat.completions.create(
                model="o1-mini",
                messages=[
                    {"role": "user", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_completion_tokens=32000
            )
        return response.choices[0].message.content