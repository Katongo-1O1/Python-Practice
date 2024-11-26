import folium


from geopy.geocoders import Nominatim

# Initialize the geolocator
geolocator = Nominatim(user_agent="city_locator")

# Get location by city name

city = input ("Enter your town and country info e.g Lusaka, Zambia: \n")
location = geolocator.geocode(city)

# Check if a result was found and print coordinates
if location:
    print(f"Coordinates for {city}:")
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")

    # Define map center coordinates
    map_center = [location.latitude, location.longitude]

    # Create a folium map
    mymap = folium.Map(location=map_center, zoom_start=15)

    # Add a marker to the map
    folium.Marker(
        location=[location.latitude, location.longitude],
        popup="Lusaka",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mymap)

    # Save the map to an HTML file
    mymap.save("map.html")

    print("Map saved as map.html. Open this file in a browser to view the map.")

else:
    print(f"Could not find coordinates for {city}.")





