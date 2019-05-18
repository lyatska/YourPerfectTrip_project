import requests
import json


class Api:
    def __init__(self, USER_KEY, host="https://developers.zomato.com/api/v2.1",
                 content_type='application/json'):
        self.host = host
        self.user_key = USER_KEY
        self.headers = {
            "User-agent": "curl/7.43.0",
            'Accept': content_type,
            'X-Zomato-API-Key': self.user_key
        }

    def get(self, endpoint, params):

        url = self.host + endpoint + "?"
        for k,v in params.items():
            url = url + "{}={}&".format(k, v)
        url = url.rstrip("&")
        response = requests.get(url, headers=self.headers)
        return response.json()

class RestaurantSearch:
    """
    Class that represents search of restaurants.
    """
    def __init__(self, USER_KEY):
        self.api = Api(USER_KEY)

    def getLocations(self, query):
        """
        Returns city coordinates.
        """
        params = {"query": query}
        locations = self.api.get("/locations", params)
        
        lat = locations['location_suggestions'][0]['latitude']
        
        lon = locations['location_suggestions'][0]['longitude']
        return [float(lat), float(lon)]

    
    def getByGeocode(self, lat, lon):
        """
        Returns code of the city.
        """
        params = {"lat": lat, "lon": lon}
        response = self.api.get("/geocode", params)
        return response['location']['city_id']
        

    def search_res(self,entity_id,entity_type,count,sort):
        """
        """
        params = {"entity_id": entity_id, "entity_type": entity_type, 
        "count": count, "sort": sort}
        
        results = self.api.get("/search", params)
        with open("rating_restaurants.json", "w") as outfile:
            json.dump(results, outfile)


    def explore_rest(self):
        """
        Give info from json file such as name and coordinates.
        """
        info = json.load(open("rating_restaurants.json", "r", encoding = "utf-8"))
        all = []
        for i in range(len(info['restaurants'])):
            lat = info['restaurants'][i]['restaurant']['location']['latitude']
            lon = info['restaurants'][i]['restaurant']['location']['longitude']
            all.append((info['restaurants'][i]['restaurant']['name'], [lat, lon]))
        return all



   
        
