import abc
from dataclasses import dataclass
from typing import Any


@dataclass
class YoutubeClient(abc.ABC):
    def get_latest_videos_for_channel(self, channel_id: str, latest_n: int) -> list[dict[str, Any]]: ...


@dataclass
class OpenAIClient(abc.ABC):
    model: str

    @abc.abstractmethod
    def summarize_text(self, text: str, max_length: int): ...


class TranscriptionClient(abc.ABC):
    def get_captions_for_video(self, video_id: str) -> str: ...
