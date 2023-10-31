import requests
class DataService():
    '''get data from an API
    return the JSON as a Python structure'''
    def __init__(self, api):
        self.api = api
    @property
    def api(self):
        return self.__api
    @api.setter
    def api(self, new_api):
        if type(new_api)==str and new_api !='':
            self.__api = new_api
    def getData(self):
        try:
            response = requests.get(self.api)
            struct = response.json()
            return struct
        except Exception as err:
            print(f'Problem: {err}')

if __name__ == '__main__':
    u = 'http://jsonplaceholder.typicode.com/users'
    d = DataService(u)
    s = d.getData()
    print(s)