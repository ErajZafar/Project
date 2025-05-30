def calculate_central_url(initial_lat_long, final_lat_long):
    # calculate the central coordinate
    coordinates = []
    x = 0.0
    y = 0.0
    z = 0.0
    # info for the dataframe for pandas
    data = {
        "lat": [initial_lat_long[0], final_lat_long[0]],
        "long": [initial_lat_long[1], final_lat_long[1]]
    }
    # create dataframe
    coords_df = pd.DataFrame(
        data, columns=['lat', 'long'])
    # calculate the distance between the initial and final coordinates
    for i, coord in coords_df.iterrows():
        lat = math.radians(float(coord.lat))
        long = math.radians(float(coord.long))
        x += math.cos(lat) * math.cos(long)
        y += math.cos(lat) * math.sin(long)
        z += math.sin(lat)

    total = len(coords_df)

    x = x / total
    y = y / total
    z = z / total
    central_longitude = math.atan2(y, x)
    central_square_root = math.sqrt(x * x + y * y)
    central_latitude = math.atan2(z, central_square_root)
    # formt the central coordinates
    coordinates = {
        'latitude': format(math.degrees(central_latitude), '.5f'),
        'longitude': format(math.degrees(central_longitude), '.5f')
    }
    return coordinates


inicial_coordinates = input("Enter your inicial coordinates: ")
final_coordinates = input("Enter your final coordinates: ")

generate_urls(inicial_coordinates, final_coordinates)
