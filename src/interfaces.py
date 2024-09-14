import abc
from dataclasses import dataclass, field
from typing import Any


@dataclass
class YoutubeClient(abc.ABC):
    @abc.abstractmethod
    def get_latest_videos_for_channel(self, channel_id: str, latest_n: int) -> list[dict[str, Any]]: ...


@dataclass
class OpenAIClient(abc.ABC):
    is_faked: bool = field(init=False)
    model: str

    @abc.abstractmethod
    def summarize_text(self, text: str, max_length: int): ...


class TranscriptionClient(abc.ABC):
    @abc.abstractmethod
    def get_captions_for_video(self, video_id: str) -> str: ...
