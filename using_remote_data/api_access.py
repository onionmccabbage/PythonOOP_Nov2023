# requests does not usually come with Python
# if it is not installed:
# pip install requests
# or
# python -m pip install requests
import requests

# we can use requests in immediate code, in functions or in classes
def getUsers():
    '''We will retreive user s data from a web-based API'''
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    return response.json() # convert the JSON data into a Python structure

if __name__ == '__main__':
    u_l = getUsers()
    print(u_l)
