import pytest
from television import Television

def test_init():
    tv = Television()
    assert tv._Television__status == False
    assert tv._Television__muted == False
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status == True

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._Television__muted == True
    assert tv._Television__volume == 0

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL + 1

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == Television.MIN_VOLUME + 1

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME

if __name__ == "__main__":
    pytest.main()
