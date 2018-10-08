import folium
import pandas

data = pandas.read_csv("10_places.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])

map = folium.Map(location=[40.75, -73.98], zoom_start=12)

fg = folium.FeatureGroup(name="places")

for lt, ln, na in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=na, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("NY_Map.html")
