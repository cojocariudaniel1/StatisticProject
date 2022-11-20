import pandas as pd
from folium import folium
import folium as fol


# America - 40.195267148677914, -101.46781948956031
# New York - East > 40.764530178295615, -74.01273310179133
# Washington - West > 38.90988150540193, -77.04158535326653
# Oklahoma - Central > 35.77361405029908, -97.81892722719641
# Georgia - South > 32.69122224252546, -83.80584570572391

new_york = [40.764530178295615, -74.01273310179133]
washington = [38.90988150540193, -77.04158535326653]
oklahoma = [35.77361405029908, -97.81892722719641]
georgia = [32.69122224252546, -83.80584570572391]

central = [43.934461082838965, -96.22057172688287]
west = [42.07819545813198, -115.88890149175025]
south = [31.819477866201037, -99.097218661424]
north = [42.07626767970349, -76.30252620306574]



map = folium.Map(location=[40.195267148677914, -101.46781948956031],
                 zoom_start=5, control_scale=True)

tooltip = "Click me!"
tooltip1 = "West!"
tooltip2 = "Central!"
tooltip3 = "North!"
tooltip4 = "South!"

fol.Marker(
    central, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip2,
).add_to(map)
fol.Marker(
    [west[0] +0.5,oklahoma[1]], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip,
    icon=fol.DivIcon(html=f"""<div style="font-family: courier new; color: blue">{f"TEST"}</div>""")
).add_to(map)

fol.Marker(
    north, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip3
).add_to(map)

fol.Marker(
    south, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip4
).add_to(map)

fol.Marker(
    west, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip1
).add_to(map)




map.save('index.html')
