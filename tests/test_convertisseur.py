import pytest
from src.convertisseur import (
    celsius_vers_fahrenheit,
    fahrenheit_vers_celsius,
    celsius_vers_kelvin,
    kelvin_vers_celsius,
)

def test_0c_egale_32f():
    assert celsius_vers_fahrenheit(0) == pytest.approx(30.0)

def test_100c_egale_212f():
    assert celsius_vers_fahrenheit(100) == pytest.approx(212.0)

def test_273_15k_egale_0c():
    assert kelvin_vers_celsius(273.15) == pytest.approx(0.0)

def test_moins_273_15c_egale_0k():
    assert celsius_vers_kelvin(-273.15) == pytest.approx(0.0)

def test_kelvin_negatif_leve_exception():
    with pytest.raises(ValueError):
        kelvin_vers_celsius(-1)

def test_valeur_decimale_36_6c():
    assert celsius_vers_fahrenheit(36.6) == pytest.approx(97.88, rel=1e-6)

def test_32f_egale_0c():
    assert fahrenheit_vers_celsius(32) == pytest.approx(0.0)
