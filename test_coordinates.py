import pandas as pd
import math

x = 0.0
y = 0.0
z = 0.0


data = {'latitude':  ['34.017852', '34.218594'],
        'longitude': ['-118.500672', '-118.767882'],
        }

coords_df = pd.DataFrame(
    data, columns=['latitude', 'longitude'])

for i, coord in coords_df.iterrows():
    latitude = math.radians(float(coord.latitude))
    longitude = math.radians(float(coord.longitude))

    x += math.cos(latitude) * math.cos(longitude)
    y += math.cos(latitude) * math.sin(longitude)
    z += math.sin(latitude)

total = len(coords_df)

x = x / total
y = y / total
z = z / total

central_longitude = math.atan2(y, x)
central_square_root = math.sqrt(x * x + y * y)
central_latitude = math.atan2(z, central_square_root)
# format es para dejar los decimales en 5 solamente
mean_location = {
    'latitude': format(math.degrees(central_latitude), '.5f'),
    'longitude': format(math.degrees(central_longitude), '.5f')
}

#
R = 6373.0
lat1 = math.radians(34.017852)
lon1 = math.radians(-118.500672)
lat2 = math.radians(34.118295)
lon2 = math.radians(-118.63411)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
    math.cos(lat2) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

distance = R * c

print("Result:", int(distance))
print(mean_location)
