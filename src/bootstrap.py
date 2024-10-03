from clients.clients import (FakeYoutubeClient, FakeYoutubeTranscriptClient, YoutubeClientImplementation,
                             YoutubeTranscriptClientImpl)
from clients.openai_client import FakeOpenAIClient, OpenAIClientImplementation, OpenAIModels
from config import Config
from interfaces import OpenAIClient, TranscriptionClient, YoutubeClient


def bootstrap(config: Config) -> tuple[OpenAIClient, YoutubeClient, TranscriptionClient]:
    openai_client: OpenAIClient
    youtube_client: YoutubeClient
    youtube_transcript_api: TranscriptionClient

    if config.OFFLINE_MODE or config.ENV == "test":
        openai_client = FakeOpenAIClient(model="fake-model")
    else:
        openai_client = OpenAIClientImplementation(
            api_key=config.OPENAI_API_KEY,
            model=OpenAIModels.GPT_3_5_TURBO,
        )

    if config.OFFLINE_MODE:
        youtube_client = FakeYoutubeClient()
        youtube_transcription_client = FakeYoutubeTranscriptClient()
    else:
        youtube_client_resource = YoutubeClientImplementation.build_resource(config.GOOGLE_API_KEY)
        youtube_client = YoutubeClientImplementation(service=youtube_client_resource)  # type: ignore
        youtube_transcription_client = YoutubeTranscriptClientImpl()

    return (
        openai_client,
        youtube_client,
        youtube_transcription_client,
    )
