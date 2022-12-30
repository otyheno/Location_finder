
import pygeoip
import urllib.request, json

gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(target):
    #record  = gi.get_record(target)
    record  = gi.record_by_name(target)
    city = record['city']
    continent = record['continent']
    country = record['country_name']
    longitude = record['longitude']
    latitude = record['latitude']

    print('Target ' + target + ' GeoLocated')
    print('City: ', str(city) + "" +' , Country:', str(country) + "" +' , Continent:', str(continent) + "")
    print('Latitude: ' ,str(latitude) + "" +', Longitude:', str(longitude))

data = json.loads(urllib.request.urlopen("http://www.example.com/").read())
target = data["ip"]
print("IP Address Found : ", target)
printRecord(target)