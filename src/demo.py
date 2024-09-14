from bootstrap import bootstrap
from config import get_config
from scripts import run_recent_video_summary_for_channel

bushcraftowy_channel_id = "UCX92mVE0rfBDSyRticjqzIA"
max_length = 1000


if __name__ == "__main__":
    config = get_config()
    openai_client, youtube_client, transcription_client = bootstrap(config)

    run_recent_video_summary_for_channel(
        channel_id=bushcraftowy_channel_id,
        openai_client=openai_client,
        youtube_client=youtube_client,
        transcription_client=transcription_client,
        max_length=1000,
    )
