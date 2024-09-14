import os
from dataclasses import dataclass
from typing import Any, Literal

import yaml

CONFIG_FILE = "config.yaml"


class classproperty(property):
    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


@dataclass(frozen=True)
class Config:
    ENV: Literal["test", "dev"]
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str

    @classproperty
    def attributes(cls):
        return tuple(cls.__annotations__.keys())


def get_config(overrides: dict[str, Any] = None) -> Config:
    if not os.path.isfile(CONFIG_FILE):
        raise Exception("Config file missing.")

    env = os.environ.get("YTS_ENV", "test")

    with open(CONFIG_FILE, "r") as f:
        config_dict = yaml.safe_load(f)
        config_dict["ENV"] = env
    if overrides:
        for key, value in overrides.items():
            if key in Config.attributes:
                config_dict[key] = value
            else:
                raise Exception(f"Invalid config override key {key}.")
    return Config(**config_dict)
