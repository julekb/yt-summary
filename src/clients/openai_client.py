import enum

from openai import OpenAI

from interfaces import OpenAIClient


class OpenAIModels(str, enum.Enum):
    GPT_4 = "gpt-4o-mini"
    GPT_3_5_TURBO = "gpt-3.5-turbo-0125"


class OpenAIClientImplementation(OpenAIClient):
    is_faked = False

    def __init__(self, api_key: str, model: OpenAIModels):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def summarize_text(self, text: str, max_length: int):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": f"You want to summerize the input and be precise and on-point using at most \
                    {max_length} characters.",
                },
                {"role": "user", "content": text},
            ],
            max_tokens=2000,
        )
        message = completion.choices[0].message.content
        return message


class FakeOpenAIClient(OpenAIClient):
    is_faked = True
    model = "fake-model"

    def summarize_text(self, text: str, max_length: int):
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
        return message[:max_length]
