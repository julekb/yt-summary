from clients.clients import YoutubeClientImplementation, YoutubeTranscriptClientImpl
from clients.openai_client import FakeOpenAIClient, OpenAIClientImplementation, OpenAIModels
from config import Config
from interfaces import OpenAIClient, TranscriptionClient, YoutubeClient


def bootstrap(config: Config) -> (OpenAIClient, YoutubeClient, TranscriptionClient):
    if config.ENV == "test":
        openai_client = FakeOpenAIClient("fake-model")
    else:
        openai_client = OpenAIClientImplementation(
            api_key=config.OPENAI_API_KEY,
            model=OpenAIModels.GPT_3_5_TURBO,
        )

    youtube_client_resource = YoutubeClientImplementation.build_resource(config.GOOGLE_API_KEY)
    youtube_client = YoutubeClientImplementation(service=youtube_client_resource)
    youtube_transcription_client = YoutubeTranscriptClientImpl()

    return (
        openai_client,
        youtube_client,
        youtube_transcription_client,
    )
