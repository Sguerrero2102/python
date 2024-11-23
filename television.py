class Television:
    """
    A class representing a television with adjustable volume and channels.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize the television with default settings.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the TV power."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the TV."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel, wrapping to MIN_CHANNEL if at MAX_CHANNEL."""
        if self.__status:
            self.__channel = (
                Television.MIN_CHANNEL
                if self.__channel == Television.MAX_CHANNEL
                else self.__channel + 1
            )

    def channel_down(self) -> None:
        """Decrease the channel, wrapping to MAX_CHANNEL if at MIN_CHANNEL."""
        if self.__status:
            self.__channel = (
                Television.MAX_CHANNEL
                if self.__channel == Television.MIN_CHANNEL
                else self.__channel - 1
            )

    def volume_up(self) -> None:
        """Increase the volume if not at MAX_VOLUME."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume if not at MIN_VOLUME."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return the TV status, channel, and volume as a formatted string.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
