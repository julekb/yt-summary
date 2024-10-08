from config import Config
from interfaces import OpenAIClient, TranscriptionClient, YoutubeClient
from models import LanguageCode


def calculate_min_max_section_count(char_length: int) -> tuple[int, int]:
    min_sections = max(int(char_length / 1000), 1)
    max_sections = max(int(char_length / 500), min_sections + 1)
    return min_sections, max_sections

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

    min_sections, max_sections = calculate_min_max_section_count(max_length)
    video_summary = openai_client.summarize_text(
        video_transcript, max_length=max_length, min_sections=min_sections, max_sections=max_sections
    )
    print(f"Summary in {max_length} chars:")
    if config.ENV != "dev":
        print(
            "Info: This output below is actually faked. Please add your own OPENAI key and set env variable YTS_ENV to dev."
        )
    print(video_summary)
