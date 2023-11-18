class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''Starts the Television class.'''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        '''Changes whether the power of the tv is on or off.'''
        self.__status = not self.__status

    def mute(self) -> None:
        '''Changes whether the volume of the tv is muted or unmuted.'''
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__temp_volume: int = self.__volume
                self.__volume = 0
            elif not self.__muted and self.__temp_volume > 0:
                self.__volume = self.__temp_volume

    def channel_up(self) -> None:
        '''Changes the channel of the tv, increasing by 1 each time.'''
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        '''Changes the channel of the tv, decreasing by 1 each time.'''
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        '''Changes the volume of the tv, increasing by 1 each time.'''
        if self.__status and not self.__muted:
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)
        elif self.__muted:
            self.__muted = False
            self.__volume = min(self.__temp_volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        '''Changes the volume of the tv, decreasing by 1 each time.'''
        if self.__status and not self.__muted:
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)
        elif self.__muted:
            self.__muted = False
            self.__volume = max(self.__temp_volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        '''Returns the status of the TV
        When it's On or Off
        The channel it's currently on
        and the Volume of the TV.'''
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
