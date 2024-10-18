import logging
import os
from dataclasses import dataclass
from typing import Any, Literal

from config.aws_config_helper import get_secrets as get_secrets_from_aws
from config.yaml_config_helper import get_secrets as get_secrets_from_yaml
from exceptions import ConfigError


class classproperty(property):
    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


@dataclass(frozen=True)
class Config:
    ENV: Literal["test", "dev"]
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str

    OFFLINE_MODE: str

    @classproperty
    def attributes(cls):
        return tuple(cls.__annotations__.keys())


def get_config(overrides: dict[str, Any] | None = None) -> Config:
    config_dict: dict[str, str] | None = None
    for handler in (get_secrets_from_yaml, get_secrets_from_yaml):
        try:
            config_dict = handler()
        except ConfigError as e:
            logging.info(f"No config found using {handler.__name__}: {e}")

    if config_dict is None:
        raise ConfigError("Config Canno")

    env = os.environ.get("YTS_ENV", "test")
    config_dict["ENV"] = env

    if overrides:
        for key, value in overrides.items():
            if key in Config.attributes:
                config_dict[key] = value
            else:
                raise Exception(f"Invalid config override key {key}.")
    return Config(**config_dict)
