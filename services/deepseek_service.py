import os
import dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

dotenv.load_dotenv()


class DeepSeekService:
    def __init__(self):
        self.client = ChatCompletionsClient(
            endpoint=os.getenv("DEEPSEEK_ENDPOINT"),
            credential=AzureKeyCredential(os.getenv("DEEPSEEK_API_KEY")),
            timeout=2000
        )

    def chat_completion(self, system_prompt: str, user_prompt: str, model: str = "DeepSeek-R1") -> str:
        response = self.client.complete(
            messages=[
                SystemMessage(content=system_prompt),
                UserMessage(content=user_prompt)
            ],
            model="DeepSeek-R1"
        )

        answer = response.choices[0].message.content

        # remove <think> content </think>
        end_think_index = answer.find("</think>")
        answer = answer[end_think_index + len("</think>"):]

        return answer
