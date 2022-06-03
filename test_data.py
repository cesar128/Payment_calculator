import pytest
from .main import rate_calculator

def test_data():
    assert rate_calculator("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00") == "The amount to pay RENE is: 215 USD"
    assert rate_calculator("ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00") == "The amount to pay ASTRID is: 85 USD"