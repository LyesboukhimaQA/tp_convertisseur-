def celsius_vers_fahrenheit(c):
    return float((c * 9/5) + 32)


def fahrenheit_vers_celsius(f):
    return float((f - 32) * 5/9)


def celsius_vers_kelvin(c):
    return float(c + 273.15)


def kelvin_vers_celsius(k):
    if k < 0:
        raise ValueError("La température en Kelvin ne peut pas être négative.")
    return float(k - 273.15)
