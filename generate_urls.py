# https://www.google.com/maps/@9.9632316,-84.0607899
# Generate urls from inicial coordinates to final coordinates
import random
from tkinter import messagebox
import geopy.distance
import os
import xlsxwriter


def generate_urls(inicial_coordinates, max_urls, ratio, gmb_name, data_link):
    # message start
    messagebox.showinfo("Start", "Start generating urls")
    print(ratio)
    # split inicial coordinates
    inicial_coordinates = inicial_coordinates.split(",")
    # generate a tuple with the inicial coordinates
    origin = geopy.Point(inicial_coordinates[0], inicial_coordinates[1])
    # get current directory
    current_directory = os.getcwd()
    # create excel file
    workbook = xlsxwriter.Workbook(
        current_directory + "/geo_urls.xlsx")
    # create worksheet
    worksheet = workbook.add_worksheet()
    worksheet.set_default_row(20, 100)
    # Generate urls from max_urls
    for i in range(int(max_urls)):
        # generate ramdon distance beteween 5 to 30 miles
        distance = random.randint(1, ratio)
        # generate ramdon angle between 0 to 360
        angle = random.randint(0, 360)
        # calculate coordinate
        coordinates = geopy.distance.distance(
            miles=distance).destination(origin, angle)
        # generate url
        place = gmb_name.replace(" ", "+")
        # remplace special characters
        place = place.replace("&", "%26")
        url = "https://www.google.com/maps/place/" + place + "/@" + \
            str(coordinates.latitude) + "," + \
            str(coordinates.longitude) + "/" + data_link + "\n"
        # write url
        worksheet.write_row('A'+str(i + 1), [url])
        worksheet.write_url('B'+str(i + 1), url, string=gmb_name)

    # close excel file
    workbook.close()
    # message end
    messagebox.showinfo("End", "Urls generated")

    return ""  # return nothing
