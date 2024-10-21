from dataclasses import dataclass

from exceptions import ServiceException, YoutubeClientException
from interfaces import AIClient, TranscriptionClient, YoutubeClient
from models import VideoDetails
from prompts import build_summary_request_prompt


@dataclass
class SummaryService:
    youtube_client: YoutubeClient
    transcription_client: TranscriptionClient
    ai_client: AIClient

    def get_latest_video_for_channel(self, channel_id: str) -> VideoDetails:
        try:
            latest_video = self.youtube_client.get_latest_videos_for_channel(channel_id, 1)[0]
        except YoutubeClientException as e:
            raise ServiceException(e)
        video_id = latest_video["id"]
        lang = self.transcription_client.get_languages_for_video(video_id)[0]

        return VideoDetails(title=latest_video.get("title"), id=video_id, channel_name="noidea", language=lang)

    def summary_for_video(self, video: VideoDetails) -> str:
        transcript = self.transcription_client.get_captions_for_video(video.id, video.language)
        prompt = build_summary_request_prompt(transcript, 4000)
        summary = self.ai_client.generate_text(prompt)
        return summary
