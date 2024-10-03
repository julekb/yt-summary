from dataclasses import dataclass
from datetime import datetime
from typing import Any

from googleapiclient.discovery import Resource, build
from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

from interfaces import TranscriptionClient, YoutubeClient
from models import LanguageCode


@dataclass
class YoutubeClientImplementation(YoutubeClient):
    service: Resource

    @classmethod
    def build_resource(cls, api_key: str) -> None:
        return build("youtube", "v3", developerKey=api_key)

    def get_latest_videos_for_channel(self, channel_id: str, latest_n: int) -> list[dict]:
        if latest_n > 50:
            raise Exception("Too many last videos requested.")
        request = self.service.search().list(
            part="id,snippet",
            type="video",
            order="date",
            channelId=channel_id,
            maxResults=latest_n,
        )
        response = request.execute()
        items = response["items"]
        if not items:
            raise Exception(f"No videos found for channel id {channel_id}.")
        return [
            {
                "id": item["id"]["videoId"],
                "title": item["snippet"]["publishedAt"],
                "description": item["snippet"]["description"],
                "published_at": item["snippet"]["publishedAt"],
            }
            for item in items
        ]

    def get_videos_details(self, video_ids: list[str]) -> list[dict[str, Any]]:
        video_ids_str = ",".join(video_ids)
        request = self.service.videos().list(part="localizations", id=video_ids_str)
        response = request.execute()
        items = response["items"]
        out = []
        for item in items:
            localization = []
            if "localizations" in item:
                localization = list(item["localizations"].keys())
            item_dict = {
                "id": item["id"],
                "language": localization,
            }
            out.append(item_dict)
        return out

    def get_channel_details(self, channel_id: str):
        request = self.service.channels().list(part="snippet,statistics", id=channel_id)
        response = request.execute()
        return response


class YoutubeTranscriptClientImpl(TranscriptionClient):
    service = YouTubeTranscriptApi
    formatter = TextFormatter()

    def get_captions_for_video(self, video_id: str, language: LanguageCode) -> str:
        try:
            transcript_raw = self.service.get_transcript(video_id, languages=[language])
        except TranscriptsDisabled as e:
            raise Exception(e)

        transcript = self.formatter.format_transcript(transcript_raw)
        return transcript


class FakeYoutubeClient(YoutubeClient):
    def get_latest_videos_for_channel(self, channel_id: str, latest_n: int) -> list[dict[str, Any]]:
        return [{"id": "video_id"}]

    def get_videos_details(self, video_ids: list[str]) -> list[dict]:
        return [
            {
                "id": "123",
                "title": "Fake vid title",
                "description": "Fake vid description",
                "published_at": datetime.now(),
                "language": LanguageCode.EN
            }
        ]


class FakeYoutubeTranscriptClient(YouTubeTranscriptApi):
    def get_captions_for_video(self, video_id: str, language: LanguageCode) -> str:
        return "These are faked video captions. Don't expect anything overly exciting."
