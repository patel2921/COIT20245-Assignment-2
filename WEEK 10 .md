**Here you can show the Task 9 and 10 both are included in this code this function only because of the sighting.py file has many contant so there is only code of function that is used for task 10. In the sighting.py whole code in it.**



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
                    #  display_sightings(abc['features'])
                     file_patha = f"{city}_extract_specific_info.json"
                     aaa = sort_by_date(abc['features'])
                     save_to_json(extract_specific_info(aaa), file_patha)
                     print_species_data(extract_specific_info(aaa))
                    #  print(extract_specific_info(aaa))
                 else:
                     print("No sightings data to display.")

             else:
                 print(f"No species data found for {city} within {radius} meters.")
