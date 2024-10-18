from config.config import Config
from interfaces import OpenAIClient, TranscriptionClient, YoutubeClient
from models import LanguageCode
from prompts import build_summary_request_prompt


def _print_visual_space():
    print("\n" * 2, "-" * 40, "\n" * 2)


def run_recent_video_summary_for_channel(
    config: Config,
    channel_id: str,
    openai_client: OpenAIClient,
    youtube_client: YoutubeClient,
    transcription_client: TranscriptionClient,
    max_length: int,
) -> None:
    print("YO STOP WATCHIN START READIN")
    _print_visual_space()

    latest_videos = youtube_client.get_latest_videos_for_channel(channel_id, 1)
    video_data = latest_videos[0]
    video_id = video_data["id"]

    for key, val in video_data.items():
        print(f"{key}: {val}")
    _print_visual_space()

    video_details = youtube_client.get_videos_details(video_ids=[video_id])
    print("Video details:\n")
    print(video_details[0])

    _print_visual_space()
    lang = video_details[0]["language"][0] or LanguageCode.EN

    video_transcript = transcription_client.get_captions_for_video(video_id, language=lang)
    print("Transcript:\n")
    print(video_transcript)
    _print_visual_space()

    prompt = build_summary_request_prompt(video_transcript, 4000)
    video_summary = openai_client.generate_text(prompt)

    print(f"Prompt:\n")
    for msg in prompt:
        for key, val in msg.items():
            print(key, val)
    print(f"Summary in {max_length} chars:")
    if config.ENV != "dev":
        print(
            "Info: This output below is actually faked. Please add your own OPENAI key and set env variable YTS_ENV to dev."
        )
    print(video_summary)

    return video_summary
