import requests

class WeatherGetter():
    ''''''
    def __init__(self, city='hull'):
        self.__city = city
    def getWeather(self):
        '''make a cal for the weather'''
        w = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.__city}&units=metric&APPID=957d663a2296945e39a56609740a2548')
        return w.json()


if __name__ == '__main__':
    wg = WeatherGetter()
    report = wg.getWeather()
    print(report)

