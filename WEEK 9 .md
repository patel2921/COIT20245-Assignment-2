# Task 6 Add a GPS stub
def gps(city):
    # Stub implementation, always returns Brisbane's GPS coordinates
    return {"latitude": -27.4689682, "longitude": 153.0234991}

def search_species(city):
    coordinates = gps(city)
    
    # Search species based on coordinates (stub implementation)
    species_list = [
        {"name": "Kangaroo", "class": "Mammal"},
        {"name": "Kookaburra", "class": "Bird"},
        {"name": "Koala", "class": "Mammal"}
    ]
    
    return species_list

# Assert statement to check if Brisbane returns the correct GPS coordinate
assert gps("Brisbane") == {"latitude": -27.4689682, "longitude": 153.0234991}

# Testing the search_species function
city = "Cairns"
species_found = search_species(city)
print(f"Species found in {city}:")
for species in species_found:
    print(f"{species['name']} ({species['class']})")


api token = "pk.37e94aa3017ca984d06aff04b69037ef"
