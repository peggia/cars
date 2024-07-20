## it was necessary to run the following as there was an error openening the streamlit file .cli: 
#pip install --upgrade streamlit

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Cars dataset analysis")
@st.cache_data
def get_data():
    link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
    df= pd.read_csv(link)
    return df

try:
    df = get_data()
    df['year'] = df['year'].astype(int)
    regions = st.multiselect("Choose region", [' US.', ' Europe.', ' Japan.'], [' Europe.'])
    if not regions:
        st.error("Please select at least one region.")
    else:
        mask = df['continent'].isin(regions)
        data = df[mask]
        st.write("### Technical Characteristics", data)
        #-----
        st.write("### Statistics")
        st.write(data.describe())
        #-----
        st.write("### Correlation Heatmap")
        corr_matrix= data.drop(columns = 'continent').corr()
        correlation = sns.heatmap(corr_matrix, center=0, annot=True, cmap = sns.color_palette("cubehelix", as_cmap=True) )
        st.pyplot(correlation.figure,clear_figure = True)
        
        #-----
        st.write("### Cubicinches vs Cylinders")
        fig = sns.boxplot(data= data,y ='cubicinches', x= 'cylinders')
        st.pyplot(fig.figure,clear_figure = True)
    
        #-----
        st.write("### Mpg vs Cylinders")
        fig2 = sns.boxplot(data= data,y ='mpg', x= 'cylinders')
        st.pyplot(fig2.figure,clear_figure = True) 
        #-----
        st.write("### Number of cars per year")
        fig2 = sns.histplot(data,x='year')
        st.pyplot(fig2.figure,clear_figure = True) 
          #-----
        st.write("### Number of cars per Continent")
        fig2 = sns.histplot(data,x='continent',color='orange')
        st.pyplot(fig2.figure,clear_figure = True) 
        #-----
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )

