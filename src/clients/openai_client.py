import enum

from openai import OpenAI

from interfaces import OpenAIClient


class OpenAIModels(str, enum.Enum):
    GPT_4o_LATEST = "chatgpt-4o-latest"
    GPT_4 = "gpt-4o-mini"
    GPT_3_5_TURBO = "gpt-3.5-turbo-0125"


class OpenAIClientImplementation(OpenAIClient):

    def __init__(self, api_key: str, model: OpenAIModels):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.max_tokens = 10_000

    def generate_text(self, prompt: list[dict[str, str]]) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=prompt,
            max_tokens=self.max_tokens
        )
        return completion.choices[0].message.content

    def summarize_text(self, text: str, max_length: int, min_sections: int = 2, max_sections: int = 4):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "",
                },
                {"role": "user", "content": f"""Summerize the input and be precise and on-point using at most \
                    {max_length} characters. Skip any advertisement. \
                     Start with numbered list of {str(min_sections)}-{str(max_sections)} main topics. \
                     The topics should be short and descriptive.
                     After, provide more context for each topic in a visually separated section.\
                    
                    Text: \"\"\" {text} \"\"\""""},
            ],
            max_tokens=2000,
        )
        message = completion.choices[0].message.content
        return message


class FakeOpenAIClient(OpenAIClient):
    model = "fake-model"
    message = """
    The input provided is a detailed and lengthy transcription in Polish,
    covering various topics related to filming, answering viewer questions,
    outdoor activities, camping tips, personal preferences, gear recommendations,
    training, and more. It touches on practical advice for outdoor activities,
    such as dealing with wet gear during camping, managing camp setup,
    handling firewood, and encountering wildlife.

    To summarize concisely, the transcript discusses preparing for outdoor adventures,
    dealing with humid conditions while camping, managing wet gear, using equipment
    like microfiber towels, considerations for packing wet gear, handling camp setup.
    dealing with campfire smoke on clothes, not being interested in urban
    survival scenarios, the challenges of winter camping,
    the importance of appropriate clothing and gear,
    experiences with camping and wildlife encounters, choosing water filters,
    and training and filming practices. The speaker shares personal insights,
    preferences, and experiences related to outdoor activities, camping,
    and filming adventures.
            """

    def generate_text(self, prompt: list[dict[str, str]]) -> str:
        return self.message[:2000]

    def summarize_text(self, text: str, max_length: int, min_sections: int = 2, max_sections: int = 4):
        return self.message[:max_length]
