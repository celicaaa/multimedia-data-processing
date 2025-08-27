import folium
import pandas as pd
import geopandas as gpd

gdata = gpd.read_file('africa-countries_6.geojson')
alldata = pd.read_csv('africa_unempl.csv', sep=';')

country = gdata[gdata['name'] == 'Algeria']
coord_polygon = country.geometry.union_all()

map = folium.Map(location=[-12, 18], zoom_start=2)

folium.GeoJson(
    {
        'type': 'Feature',
        'geometry': coord_polygon.__geo_interface__
    },
    style_function=lambda x: {'fillColor': 'red', 'color': 'blue'},
    tooltip='Algeria'
).add_to(map)


threshold_scale=list(alldata['obs_value'].quantile([0,0.25,0.5,0.75,1]))

folium.Choropleth(
    geo_data='africa-countries_6.geojson',
    name='choropleth',
    data=alldata,
    columns=["ref_area_id", "obs_value"],
    key_on="feature.properties.postal",
    fill_color="BuPu",
    fill_opacity=0.3,
    line_opacity=0.7,
    legend_name='Target Variable',
    threshold_scale=threshold_scale,
    bins=5
).add_to(map)
folium.LayerControl().add_to(map)
map.save('africa_map.html')