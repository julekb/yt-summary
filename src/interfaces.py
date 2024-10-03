import abc
from dataclasses import dataclass, field
from typing import Any

from models import LanguageCode


@dataclass
class YoutubeClient(abc.ABC):
    @abc.abstractmethod
    def get_latest_videos_for_channel(self, channel_id: str, latest_n: int) -> list[dict[str, Any]]: ...

    @abc.abstractmethod
    def get_videos_details(self, video_ids: list[str]) -> list[dict]: ...


@dataclass
class OpenAIClient(abc.ABC):
    model: str

    @abc.abstractmethod
    def summarize_text(self, text: str, max_length: int, min_sections: int, max_sections: int): ...


class TranscriptionClient(abc.ABC):
    @abc.abstractmethod
    def get_captions_for_video(self, video_id: str, language: LanguageCode) -> str: ...
