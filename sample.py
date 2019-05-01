from hotels import HotelSearch

search = HotelSearch("08ef2b85", "a9bf1194bad1f36b6a5f286d549ad335")

print(search.GetHotelData([1017089108070373346, 6085103403340214927]))
print(search.GetHotelPrice(6771549831164675055, 20141101, 20141102))