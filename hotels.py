import requests
import json
import csv
import folium
from arrays import DynamicArray

class HotelSearch:
        """
        Class that represents search of hotels and its info.
        DynamicArray ADT in usage.
        Based on Goibibo API and needs app_id and app_key.
        """
        BASE = "http://developer.goibibo.com/api/"

        def __init__(self, app_id, app_key):
                self.auth = {"app_id" : app_id,
                        "app_key" : app_key}

       
        def user_input(self, city):
                """
                Reads the CSV file and returns a city code.
                """
                lst = DynamicArray()
                with open("city_list.csv", "r") as csvFile:
                        reader = csv.reader(csvFile)
                        for row in reader:
                                lst.append(row)
                for i in range(len(lst)):
                        if lst[i][0] == city or lst[i][0] == city.title():
                                code = lst[i][1]
                return code

        
        def SearchHotelsByCity(self, city_id):
                """
                Gets a list of hotels available in a city alongwith
                information of each hotel. Creates a JSON file with all the info.
                Parameter
                ----------
                city_id : City ID of the city for which hotel prices are required.
                ----------
                
                goibiboAPI.SearchHotelsByCity(6771549831164675055)
                """

                all = requests.get(self.BASE + "voyager/" +
                        "?method=hotels.get_hotels_data_by_city" +
                        "&city_id=%d" % city_id, params=self.auth).json()
                with open('hotels.json', 'w') as outfile:
                        json.dump(all, outfile)
                


        def GetHotelPrice(self, city_id, check_in, check_out):
                '''
                Gets the price information of
                all the available hotels in the given city.
                Creates a JSON file with all the info.
                Parameters
                ----------
                city_id : City ID of the city for which hotel prices are required.
                check_in : Hotel Check in date - format YYYYMMDD
                check_out : Hotel Check out date - format YYYYMMDD
                Examples
                --------
                goibiboAPI.GetHotelPriceByCity(6771549831164675055,
                                                20141101, 2011102)
                '''

                data = requests.get(self.BASE + "cyclone/" +
                        "?city_id=%d" % city_id +
                        "&check_in=%d" % check_in +
                        "&check_out=%d" % check_out, params=self.auth).json()
                with open('data.json', 'w') as outfile:
                        json.dump(data, outfile)


       
        def research_id(self):
                """
                Reads the JSON file and returns all the identification numbers of needed hotels.
                """
                info = json.load(open("hotels.json", "r", encoding = "utf-8"))
                ids = []
                for j in info["data"]:
                        ids.append(info["data"][j]["hotel_geo_node"]["_id"])
                return ids
        

        def research_price(self):
                """
                Reads the JSON file and returns the dictionary of hotels IDs and their prices.
                """
                info = json.load(open("data.json", "r", encoding = "utf-8"))
                prices = {}
                for j in info["data"]:
                    prices[j] = info["data"][j]["op"]
                return prices


        def search(self):
                """
                Processes all the information and returns the best variant\
                of hotel with the cheapest price, and its coordinations.
                """
    
                first = self.research_id()
                second = self.research_price()
                h = {}
                for i in first:
                        try:
                                h[i] = second[i]    
                        except KeyError:
                                continue

                m = sorted(h.items(), key = lambda x:(x[1], x[0]))[0] 
                info = json.load(open("hotels.json", "r", encoding = "utf-8"))
                selected = info["data"][m[0]]["hotel_geo_node"]["name"]
                coords = info["data"][m[0]]["hotel_geo_node"]["location"]
                return selected, coords

        def get_coordinates(self):
                """
                Returns the coordinations of the cheapes hotel.
                """
                coords = self.search()
                return list(coords[1].values())

                

       


        

                
                        
                                        
                                





                



                        
