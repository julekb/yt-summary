import argparse

from bootstrap import bootstrap
from config import get_config
from scripts import run_recent_video_summary_for_channel

test_channel = "UC-Q1gV2g_ck4LZG8axhAeVg"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--channel-id", required=False, type=str)
    parser.add_argument("-b", "--burn-money", required=False, action="store_true")
    parser.add_argument("-f", "--offline", required=False, action="store_true")

    args = parser.parse_args()

    channel_id = args.channel_id or test_channel


    config_overrides = {"ENV": "dev" if args.burn_money else "test", "OFFLINE_MODE": args.offline}

    config = get_config(overrides=config_overrides)


    openai_client, youtube_client, transcription_client = bootstrap(config)

    run_recent_video_summary_for_channel(config, channel_id=channel_id, openai_client=openai_client,
                                         youtube_client=youtube_client, transcription_client=transcription_client,
                                         max_length=1000)
