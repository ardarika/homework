class Element:
    def __init__(self, melting_temp, boiling_temp):
        self.melting_temp = melting_temp
        self.boiling_temp = boiling_temp


    def agg_state(self, temp, scale):
        if scale != 'C':
            temp = self.convert_to_c(temp, scale)
        if temp <= self.melting_temp:
            return 'Element is solid'
        elif self.melting_temp <= temp <= self.boiling_temp:
            return 'Element is liquid'
        elif temp >= self.boiling_temp:
            return 'Element is gas'


    def convert_to_c(self, temp, scale):
        if scale == 'K':
            ntemp = temp - 273.15
        elif scale == 'F':
            ntemp = ((temp - 32) * 5) / 9
        return round(ntemp, 2)


if __name__ == '__main__':
    ferrum = Element(melting_temp=1538, boiling_temp=2862)
    print(ferrum.agg_state(4034, 'F'))
    print(ferrum.convert_to_c(1900, 'K'))