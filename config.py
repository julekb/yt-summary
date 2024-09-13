import os
from dataclasses import dataclass
from typing import Literal

import yaml

CONFIG_FILE = "config.yaml"


@dataclass(frozen=True)
class Config:
    ENV: Literal["test", "dev"]
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str


def get_config() -> Config:
    if not os.path.isfile(CONFIG_FILE):
        raise Exception("Config file missing.")

    env = os.environ.get("YTS_ENV", "test")

    with open(CONFIG_FILE, "r") as f:
        config_dict = yaml.safe_load(f)
        config_dict["ENV"] = env
        return Config(**config_dict)
