from requests import get
import json
import folium
import os
import webbrowser
import html

#assign blue for the coldest temps
#assign red for the hottest temps
#assign green for the mid-range temps
def colourgrad(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value - minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    r = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    hexcolour = '#%02x%02x%02x' % (r,g,b)
    return hexcolour

#store URL as a string
url = "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement"

#fetch the data
station_data = get(url).json()

#create a color scale with tmax and tmin
temps = []
tmax = 0.0
tmin = 100.0
lons = [data["weather_stn_long"] for data in station_data["items"]]
lats = [data["weather_stn_lat"] for data in station_data["items"]]
wsnames = [html.escape(station["weather_stn_name"]) for station in station_data["items"]]

#check for values less than -30 and greather than 50 degrees and sent values otside of that to 20 degees
for data in station_data["items"]:
    if "ambient_temp" in data:
        t = data ["ambient_temp"]
        if t > 50 or t < -30:
            t = 20
        if t > tmax:
            tmax = t
        if t < tmin:
            tmin = t
        temps.append(str(t))    
#setting up the map
map_ws = folium.Map(location = [47,7], zoom_start=6)

#add locations of all weather stations
for n in range(len(lons)-1):
    hcol = colourgrad(tmin, tmax, float(temps[n]))
    folium.CircleMarker ([lats[n], lons[n]],
                         radius = 5,
                         popup = wsnames[n]+':'+temps[n],
                         fill_color = hcol).add_to(map_ws)
                         
     
#save new file and oper browser    
CWD = os.getcwd()
map_ws.save("wetterkarte.html")
webbrowser.open_new_tab('file://'+CWD+'/'+'wetterkarte.html')