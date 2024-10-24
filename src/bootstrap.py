import clients
from config.config import Config
from interfaces import AIClient, TranscriptionClient, YoutubeClient
from service import SummaryService


def bootstrap(config: Config) -> SummaryService:
    openai_client: AIClient
    youtube_client: YoutubeClient
    youtube_transcript_api: TranscriptionClient

    if config.OFFLINE_MODE or config.ENV == "test":
        openai_client = clients.FakeOpenAIClient(model="fake-model")
    else:
        openai_client = clients.OpenAIClientImplementation(
            api_key=config.OPENAI_API_KEY,
            model=clients.OpenAIModels.GPT_4o_LATEST,
        )

    if config.OFFLINE_MODE:
        youtube_client = clients.FakeYoutubeClient()
        youtube_transcription_client = clients.FakeYoutubeTranscriptClient()
    else:
        youtube_client_resource = clients.YoutubeClientImplementation.build_resource(config.GOOGLE_API_KEY)
        youtube_client = clients.YoutubeClientImplementation(service=youtube_client_resource)
        youtube_transcription_client = clients.YoutubeTranscriptClientImpl()

    return SummaryService(
        ai_client=openai_client,
        youtube_client=youtube_client,
        transcription_client=youtube_transcription_client,
    )
