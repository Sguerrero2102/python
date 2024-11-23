import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_channel_up_down():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_up_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
