import folium 
import pandas 

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LON"])
lon = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000: 
        return 'green'
    elif elevation 1000 <= elevation < 3000
        return 'orange'
    else: 
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6)


fgv = folium.FeatureGroup(name="Volcanoes")



for lt, ln, el in zip(lat, lan, elev): 
    print(type(el))
    fgv.add_child(folium.CircleMarker(location=[lt, ln],  radius = 6, popup=str(el)+ "m", 
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'), 
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 1000000 
else 'orange' if 1000000 <= x['properties']['POP2005']< 2000000 else 'red'}))

map.add_child(folium.LayerControl())
map.add_child(fgv)
map.add_child(fgp)


map.save("Map1.html")

