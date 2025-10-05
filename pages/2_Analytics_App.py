import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import json
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pickle
import os
st.set_page_config(page_title='Gurugram Analysis',
                   layout='wide')


st.title("Gurugram Overall Housing Analysis")

MAIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEANED_DATASET_PATH = os.path.join(MAIN_DIR,'1_Datasets','4.3_dataset_clean_v2.csv')
FEATURE_SELECTED_DATASET = os.path.join(MAIN_DIR,'1_Datasets','4.6_dataset_feature_selected.csv')

GEOJSON_PATH = os.path.join(MAIN_DIR,'4_resources','4.1_gurugram_sectors_final.geojson')
FEATURE_TEXT_PATH = os.path.join(MAIN_DIR,'4_resources','4.2_feature_text.pkl')

df = pd.read_csv(CLEANED_DATASET_PATH)
df_2= pd.read_csv(FEATURE_SELECTED_DATASET)



# --- Function to plot choropleth with labels ---
st.markdown('<br>',unsafe_allow_html=True)
st.header('Sector wise Averge Price/Sqft Geomap')
def plot_sectors_plotly(geojson_path = GEOJSON_PATH):

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
            # title="Gurugram Sector Price per Sqft",
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

plot_sectors_plotly(geojson_path=GEOJSON_PATH)

#----------------------------------------------------------------
#adding sectorwise average price/sqft as dataframe

# Define a sorting key function
def extract_sector_number(sector):
    match = re.search(r'\d+', sector)
    return int(match.group()) if match else float('inf')  # non-numeric sectors go last

# Sort the Series using the extracted number
df_average_price = df.groupby('sector')['price_sqft'].mean().sort_index()
df_average_price_sorted = df_average_price.sort_index(key=lambda x: x.map(extract_sector_number))

st.dataframe(df_average_price_sorted)

#----------------------------------------------------------------
#wordcloud
# Split each string by commas and flatten the list
st.markdown("<br>", unsafe_allow_html=True) 
st.header('Gurugram Housing Societies Ameneties Wordcloud')
with open (FEATURE_TEXT_PATH,'rb') as f: 
    txt = pickle.load(f)
wordcloud = WordCloud(width = 800, height = 600, 
                      background_color ='white', 
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(txt)

# Step 3: Plot and convert to image

st.image(wordcloud.to_array(), use_container_width=True)

col1,col2 = st.columns(2)
#scatter plot -> area vs price
with col1:
    st.markdown("<br>", unsafe_allow_html=True) 
    st.header('Price variation with Apartment size')
    fig = px.scatter(df_2,x='super_area', y='price', color='bedrooms' , title="Price(Cr) vs Super Built-up Area(Sqft)")
    fig.update_layout(
        xaxis_title = "Super Built-up Area(Sqft)",
        yaxis_title = "Price (Cr)"
    )
    st.plotly_chart(fig)


#-----Distribution of houses based on BHK
with col2:
    st.markdown('<br>', unsafe_allow_html=True)
    st.header('Distibution of houses based on BHK')
    pie_fig = px.pie(data_frame=df,names ='bedrooms', title="BHK distribution")
    pie_fig.update_layout(title = {'text':"Number of Houses of Particular BHK",
                'x': 0.5,
                'xanchor':'center'})
    st.plotly_chart(pie_fig)


#----- BHK wise price distribution
st.markdown('<br>',unsafe_allow_html=True)
st.header('BHK wise price distributions')
bhk_price_fig = px.box(data_frame=df,x='bedrooms', y='price', title = "BHK vs Price Distibution Box-plot")
bhk_price_fig.update_layout(
    xaxis_title = "No of Bedrooms",
    yaxis_title = "Price (Cr)",
    title = {'text':"BHK vs Price Distibution Box-plot",
             'x': 0.5,
            'xanchor':'center'}
)
st.plotly_chart(bhk_price_fig)