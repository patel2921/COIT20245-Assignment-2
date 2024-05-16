# sighting.py
from nominatim import gps_coordinate
from wildlife import get_species_list,get_surveys_by_species,display_sightings,sort_by_date,extract_specific_info
import json

def display_menu():
    """Display the menu options."""
    print("Welcome to Wildlife Sighting Tracker!")
    print("a. Print help menu")
    print("b. Exit the program")
    print("c. Display animal species in a city")
    print("d. Display venomous species in a city")
    print("e. enter city name get the lan lon")


def print_help_menu():
    """Display the help menu."""
    print("Help Menu:")
    print("This program allows you to track wildlife sightings.")
    print("You can enter specific sightings and manage your records.")

def save_to_json(data, file_path):
    """
    Save data to a JSON file.

    Args:
        data (dict): Data to be saved.
        file_path (str): File path to save the JSON data.
    """
    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {file_path}")
    except IOError as e:
        print(f"Error saving data to JSON file: {e}")


def display_species(species_data):
    """
    Print species information including TaxonID, AcceptedCommonName, and PestStatus.

    Args:
        species_data (dict): Dictionary containing species information.
    """
    if "Species" in species_data:
        taxon_id = species_data["Species"]["TaxonID"]
        accepted_common_name = species_data["Species"]["AcceptedCommonName"]
        pest_status = species_data["Species"]["PestStatus"]

        print(f"TaxonID: {taxon_id}")
        print(f"Accepted Common Name: {accepted_common_name}")
        print(f"Pest Status: {pest_status}")
    else:
        print("Invalid species data format.")

def filter_venomous(species_list):
    """
    Filter species to include only venomous species.

    Args:
        species_list (list): List of species dictionaries.

    Returns:
        list: Filtered list containing only venomous species dictionaries.
    """
    return [entry for entry in species_list if entry['Species']['PestStatus'] == 'Venomous']

def main():
    """Main function to run the Wildlife Sighting Tracker program."""
    while True:
        display_menu()
        choice = input("Enter your choice (a/b/c/d/e/f): ").strip().lower()

        if choice == 'a':
            print_help_menu()
        elif choice == 'b':
            print("Exiting the program. Goodbye!")
            break
        elif choice == 'c':
            city = input("Enter the city name: ").strip()
            radius=10000
            coordinates = gps_coordinate(city)
            species_data = get_species_list(coordinates['latitude'], coordinates['longitude'], radius)
            print(species_data)
            display_species(species_data)
        elif choice == 'd':
            city = input("Enter the city name: ").strip()
            radius=10000
            coordinates = gps_coordinate(city)
            species_data = get_species_list(coordinates['latitude'], coordinates['longitude'], radius)
            # species_list = search_species(city)
            print(species_data)
            venomous_species_list = filter_venomous(species_data)
            display_species(venomous_species_list)

        elif  choice == 'e':
             city = input("Enter the city name: ").strip()
             coordinates=gps_coordinate(city)
             print(f"Latitude: {coordinates['latitude']}, Longitude: {coordinates['longitude']}")

        elif choice == 'f':
             city = input("Enter the city name: ").strip()
             taxon_id = input("Enter the taxon_id name: ").strip()

             radius = 10000
    # radius = int(input("Enter search radius in meters: ").strip())

    # Retrieve geographic coordinates for the specified city
             coordinates = gps_coordinate(city)
             if not coordinates:
                 print(f"Coordinates not found for {city}. Exiting...")
                 return

    # Retrieve species list for the specified coordinates and radius
             species_data = get_species_list(coordinates['latitude'], coordinates['longitude'], radius)
             abc = get_surveys_by_species(int(taxon_id), coordinates['latitude'], coordinates['longitude'], radius)

             if abc:
        # Save species data to a JSON file
                 file_path = f"{city}_abc_species_list.json"
                 save_to_json(species_data, file_path)

        # Display sorted sightings by date
                 if 'features' in abc:
                     display_sightings(abc['features'])
                     file_patha = f"{city}_extract_specific_info.json"
                     aaa = sort_by_date(abc['features'])
                     save_to_json(extract_specific_info(aaa), file_patha)
                     print(extract_specific_info(aaa))
                 else:
                     print("No sightings data to display.")

             else:
                 print(f"No species data found for {city} within {radius} meters.")


if __name__ == "__main__":
    main()
