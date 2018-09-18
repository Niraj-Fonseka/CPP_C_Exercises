import requests

def hello_world():
        r = requests.get('https://www.metaweather.com/api/location/2357536/')
        return r.json()        



if __name__ == '__main__':
    print(hello_world())