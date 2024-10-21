class SummaryBaseException(Exception):
    pass


class ConfigError(SummaryBaseException):
    pass


class ConfigHelperError(ConfigError):
    pass


class BaseClientError(SummaryBaseException):
    pass


class YoutubeClientException(BaseClientError):
    pass


class ChannelNotFound(YoutubeClientException):
    pass


class VideoNotFound(YoutubeClientException):
    pass


class YoutubeTranscriptClientException(BaseClientError):
    pass


class ServiceException(SummaryBaseException):
    pass
