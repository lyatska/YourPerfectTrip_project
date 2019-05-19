from hotels import HotelSearch
from arrays import DynamicArray

search = HotelSearch("08ef2b85", "a9bf1194bad1f36b6a5f286d549ad335")
city = input("Please, enter the name of the city: ")
city1 = search.user_input(city)
print(city1)
search.SearchHotelsByCity(int(city1))
date_in = int(input("PLease, enter the date you come in the city in format YYYYMMDD: "))
date_out = int(input("Please, enter the date you leave the city in format YYYYMMDD: "))
search.GetHotelPrice(int(city1), date_in, date_out)
name_and_coords = search.search()
print(name_and_coords)