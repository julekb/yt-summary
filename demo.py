from bootstrap import bootstrap
from config import get_config

bushcraftowy_channel_id = "UCX92mVE0rfBDSyRticjqzIA"
max_length = 1000


def _print_visual_space():
    print("\n" * 2, "-" * 40, "\n" * 2)


def run_demo(channel_id):
    print("YO STOP WATCHIN START READIN")
    _print_visual_space()

    latest_videos = youtube_client.get_latest_videos_for_channel(channel_id, 1)
    video_data = latest_videos[0]
    video_id = video_data["id"]

    for key, val in video_data.items():
        print(f"{key}: {val}")
    _print_visual_space()

    video_transcript = transcription_client.get_captions_for_video(video_id)
    print("Transcript:\n")
    print(video_transcript)
    _print_visual_space()

    video_summary = openai_client.summarize_text(video_transcript, max_length=max_length)
    print(f"Summary in {max_length} chars:")
    if config.ENV == "test":
        print(
            "Info: This output below is actually faked. Please add your own OPENAI key and set env variable YTS_ENV to dev."
        )
    print(video_summary)


if __name__ == "__main__":
    config = get_config()
    openai_client, youtube_client, transcription_client = bootstrap(config)

    run_demo(channel_id=bushcraftowy_channel_id)
