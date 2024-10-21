import argparse

from bootstrap import bootstrap
from config.config import get_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--channel-id", required=Truep, type=str)
    parser.add_argument("-b", "--burn-money", required=False, action="store_true")
    parser.add_argument("-f", "--offline", required=False, action="store_true")

    args = parser.parse_args()

    channel_id = args.channel_id

    config_overrides = {"ENV": "dev" if args.burn_money else "test", "OFFLINE_MODE": args.offline}

    config = get_config(overrides=config_overrides)

    summary_service = bootstrap(config)
    latest = summary_service.get_latest_video_for_channel(channel_id)
    summary = summary_service.summary_for_video(latest)

    print("Summary:")
    print(summary)
