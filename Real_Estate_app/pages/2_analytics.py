import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import json

st.set_page_config(page_title='Gurugram Analysis',
                   layout='wide')

st.title("Gurugram Overall Price Analysis")

# --- Function to plot choropleth with labels ---
def plot_sectors_plotly(geojson_path = '../6.1_gurugram_sectors_final.geojson'):

    sectors_gdf = gpd.read_file(geojson_path)

    if sectors_gdf.empty:
        print("No sectors to plot.")
        return

    try:
        # Convert to WGS84 for Mapbox
        sectors_gdf = sectors_gdf.to_crs(epsg=4326)

        # Reproject to UTM for accurate centroid calc
        sectors_proj = sectors_gdf.to_crs(epsg=32643)
        sectors_gdf["centroid_lon"] = sectors_proj.centroid.to_crs(epsg=4326).x
        sectors_gdf["centroid_lat"] = sectors_proj.centroid.to_crs(epsg=4326).y

        # Convert GeoDataFrame geometry to GeoJSON FeatureCollection
        geojson = json.loads(sectors_gdf.to_json())

        # Create choropleth layer
        choropleth = go.Choroplethmapbox(
                                        geojson=geojson,
                                        locations=sectors_gdf.index,
                                        z=sectors_gdf["price_sqft"],
                                        colorscale="Viridis",
                                        marker_opacity=0.6,
                                        marker_line_width=0,
                                        text=sectors_gdf["name"] + "<br>₹" + sectors_gdf["price_sqft"].round(2).astype(str) + "/sqft",
                                        hoverinfo="text"
                                )

        # Create text label layer
        text_labels = go.Scattermapbox(
            lat=sectors_gdf["centroid_lat"],
            lon=sectors_gdf["centroid_lon"],
            mode='text',
            text=sectors_gdf["name"].str.title(),
            textfont=dict(size=12, color="black"),
            showlegend=False,
            hoverinfo="none"
        )

        # Build figure
        fig = go.Figure()
        fig.add_trace(text_labels)
        fig.add_trace(choropleth)
        

        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=11.5,
            mapbox_center={"lat": 28.4595, "lon": 77.0266},
            margin={"r": 0, "t": 30, "l": 0, "b": 0},
            title="Gurugram Sector Price per Sqft",
            height = 700,
            width = 1000

        )
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            print('eror occured')
            st.warning("No figure could be generated. Please check if the sector geometries are valid and not empty.")

    except Exception as e:
        print(f"Error while plotting with Plotly: {e}")


#
plot_sectors_plotly(geojson_path='../6.1_gurugram_sectors_final.geojson')