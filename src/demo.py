from bootstrap import bootstrap
from config.config import get_config

bushcraftowy_channel_id = "UCX92mVE0rfBDSyRticjqzIA"
max_length = 1000


if __name__ == "__main__":
    config = get_config()

    summary_service = bootstrap(config)
    latest = summary_service.get_latest_video_for_channel(bushcraftowy_channel_id)
    summary = summary_service.summary_for_video(latest)

    print("Summary:")
    print(summary)
