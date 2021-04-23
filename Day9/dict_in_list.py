travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(pais, cant_visit, lugares):
    travel_log.append({
        "country": pais,
        "visits": cant_visit,
        "cities": lugares
    })

add_new_country("Colombia",2, ["Caldas", "Bogota"])
print(travel_log)