class UnitConverter:
    #static, no self needed.
    @staticmethod
    def celsiusToFahrenheit(c):
        fah = c*9/5+32
        return fah
    @staticmethod
    def fahrenheitToCelsius(f):
        cel = (f-32)*5/9
        return cel
    @staticmethod
    def celsiusToKelvin(c):
        kel = c+273.15
        return kel
    @staticmethod
    def fahrenheitToKelvin(f):
        kel = (f-32)*5/9+273.15
        return kel
    @staticmethod
    def kelvinToCelsius(k):
        cel = k-273.15
        return cel
    @staticmethod
    def kelvinToFahrenheit(k):
        fah = (k-273.15)*9/5+32
        return fah