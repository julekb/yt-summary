import argparse

from bootstrap import bootstrap
from config import get_config
from scripts import run_recent_video_summary_for_channel

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--channel-id", required=False, type=str)
    parser.add_argument("-b", "--burn-money", required=False, action="store_true")
    args = parser.parse_args()

    args = parser.parse_args()

    channel_id = args.channel_id
    burn_money = args.burn_money
    env = "dev" if burn_money else "test"

    config = get_config(overrides={"ENV": env})

    openai_client, youtube_client, transcription_client = bootstrap(config)

    run_recent_video_summary_for_channel(
        channel_id=channel_id,
        openai_client=openai_client,
        youtube_client=youtube_client,
        transcription_client=transcription_client,
        max_length=1000,
    )