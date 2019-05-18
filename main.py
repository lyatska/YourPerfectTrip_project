from restaurants import RestaurantSearch
from hotels import HotelSearch
import csv
import folium

def mappy1(city, date_in, date_out):
    """
    Main function that processes all the information and returns the\
    ending result that displays the map with the cheapest hotel of the city.
    """ 
    search = HotelSearch("08ef2b85", "a9bf1194bad1f36b6a5f286d549ad335")
    city1 = search.user_input(city)
    search.SearchHotelsByCity(int(city1))
    search.GetHotelPrice(int(city1), date_in, date_out)

    name_and_coords = search.search()
    lats = list(name_and_coords[1].values())
               
    map = folium.Map(location= lats, zoom_start=20)
    fg = folium.FeatureGroup(name = "The best proposition!")
    fg.add_child(folium.Marker(location = lats, popup=name_and_coords[0],icon = folium.Icon(color = 'red')))
    map.add_child(fg)
    map.save("templates\proposition_hot.html")
    res = map.get_root().render()
    return res


def mappy2(city_name):
    """
    Main function that processes all the information and returns the\
    ending result that displays the map with the most rated restaurants of the city.
    """    
    food = RestaurantSearch("7ef37e48992192baa0f44d90ab16a045")
    locat = food.getLocations(city_name)
    code = food.getByGeocode(locat[0], locat[1])
    food.search_res(code, 'city', 10, 'rating')
    res = food.explore_rest()

    map = folium.Map(location= locat, zoom_start=8)
    mp = folium.FeatureGroup(name = "The best rated restaurants!")
    for i in range(len(res)):
        lats1 = res[i][1]
        lats1 = [float(j) for j in lats1]                
        name = res[i][0]                
        mp.add_child(folium.Marker(location = lats1, popup=name,icon = folium.Icon(color = 'yellow')))

    map.add_child(mp)
    map.save("templates\proposition_res.html")
    res = map.get_root().render()
    return res


def is_valid(city):
    """
    Checks if city exists.
    """
    lst = []
    m = 0
    with open("city_list.csv", "r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            lst.append(row)
    for i in range(len(lst)):
        if city==lst[i][0] or city.title() == lst[i][0] :
            m += 1
        else:
            m == 0
    if m > 0:
        return True
    else:
        return False

    
                


