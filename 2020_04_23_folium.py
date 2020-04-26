import pandas as pd
import numpy as np

pop_korea = pd.read_csv("./folium_Korea/Total_People_2018.csv", encoding='utf-8')
pop_korea.head()

pop_korea.rename(columns={pop_korea.columns[0]:'코드',
                          pop_korea.columns[1]:'인구수'}, inplace=True)

pop_korea.head()


import json

geo_path = './folium_Korea/TL_SCCO_SIG_WGS84.json'
geo_str = json.load(open(geo_path))



print(geo_str)

import folium
import webbrowser

map = folium.Map(location = [37.5502, 126.982], zoom_start=7)

map.choropleth(geo_data=geo_path,
               data=pop_korea,
               columns = ['코드', '인구수'],
               fill_color='YlGn',
               fill_opacity=0.7,
               line_opacity=0.5,
               key_on='feature.properties.SIG_CD')

map.save('folium_kr4.html')
webbrowser.open_new("folium_kr4.html")