import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location= [-36.85, -185.25], zoom_start= 6, tiles= "Stamen Terrain")

features = folium.FeatureGroup(name= "My Map")

for lt, ln in zip(lat, lon):
    features.add_child(folium.Marker(location= [lt, ln], popup= "Hi I am a Marker", icon= folium.Icon(color="green")))
map.add_child(features)

map.save("Map1.html")