from dataclasses import dataclass
from typing import Any, Literal

from googleapiclient.discovery import Resource, build
from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

from interfaces import TranscriptionClient, YoutubeClient


@dataclass
class YoutubeClientImplementation(YoutubeClient):
    service: Resource

    @classmethod
    def build_resource(cls, api_key: str) -> None:
        return build("youtube", "v3", developerKey=api_key)

    def get_latest_videos_for_channel(self, channel_id: str, latest_n: int) -> list[dict[str, Any]]:
        if latest_n > 50:
            raise Exception
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
            raise Exception
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
                "localization": localization,
            }
            out.append(item_dict)
        return out

    def get_channel_details(self, channel_id: str):
        request = self.service.channels().list(part="snippet,statistics", id=channel_id)
        response = request.execute()
        return response


LanguageCode = Literal["pl", "en"]


class YoutubeTranscriptClientImpl(TranscriptionClient):
    service = YouTubeTranscriptApi
    formatter = TextFormatter()

    def get_captions_for_video(self, video_id: str, language: LanguageCode = "pl") -> str:
        try:
            transcript_raw = self.service.get_transcript(video_id, languages=["pl"])
        except TranscriptsDisabled:
            raise Exception

        transcript = self.formatter.format_transcript(transcript_raw)
        return transcript
