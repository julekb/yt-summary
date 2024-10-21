import enum
from dataclasses import dataclass


class LanguageCode(str, enum.Enum):
    EN = "en"
    PL = "pl"


@dataclass
class VideoDetails:
    title: str
    id: str
    channel_name: str
    language: str
