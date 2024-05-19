# Task 6 Add a GPS stub



    def gps(city):
        return {"latitude": -27.4689682, "longitude": 153.0234991}
        def search_species(city):
            coordinates = gps(city)
            Search species based on coordinates (stub implementation)
            species_list = [
                {"name": "Kangaroo", "class": "Mammal"},
                {"name": "Kookaburra", "class": "Bird"},
                {"name": "Koala", "class": "Mammal"}
            ]
            return species_list
        Assert statement to check if Brisbane returns the correct GPS coordinate
        assert gps("Brisbane") == {"latitude": -27.4689682, "longitude": 153.0234991}
        
        Testing the search_species function
        city = "Cairns"
    species_found = search_species(city)
    print(f"Species found in {city}:")
    for species in species_found:
        print(f"{species['name']} ({species['class']})")

#Task 7 GPS Webservice Module
    
    nomibatim.py file
    import requests

    def gps_coordinate(city):
        if city.lower() == 'queensland':
            return {'latitude': -16.92, 'longitude': 145.777}
        
    base_url = f"https://nominatim.openstreetmap.org/search?q=Queensland&format=json"

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an HTTPError for bad status codes (e.g., 404, 500)
        data = response.json()

        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return {'latitude': latitude, 'longitude': longitude}
        else:
            print(f"No coordinates found for {city}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching coordinates for {city}: {e}")
        return None

**Test the gps_coordinate function**
    
    if __name__ == "__main__":
    # Test with different cities
    cities = ["Cairns", "Brisbane", "Sydney","Queensland"]

    for city in cities:
        coordinates = gps_coordinate(city)
        if coordinates:
            print(f"Coordinates for {city}: {coordinates}")
        else:
            print(f"No coordinates found for {city}")
