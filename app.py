import streamlit as st
import pandas as pd
from graphs import *

# Filter function
def dataframe_filter(df_input, insurer=None, label=None, star=None):
    df_filter = df_input.copy()
    filter_dict = {'insurer': insurer, 'label': label, 'star': star }
    
    for filter_name, filter in filter_dict.items():
        if filter not in [None, []]:                                # if str or [str]
            filter = [filter] if type(filter) == str else filter    # convert str to [str]
            df_filter = df_filter[df_filter[filter_name].isin(filter)]
    
    return df_filter

# Streamlit app
st.title('Project 2 - Insurance')

# Select language
lang = st.selectbox('Select Language', ['fr', 'en'])
df = pd.read_csv(f'data/df_assurance_{lang}_prepro.csv')

# Select mode
filter_table, graph_table = st.tabs(["Filter", "Graphs"])
with filter_table:
    st.subheader('Choose filter')
    st.write("Choose one or more options for the filters. If None, all the option will be applied.")
    filter_dict = {'insurer': [], 'label': [], 'star': [] }
    for filter_name in filter_dict.keys():
        filter_list =  df[filter_name].unique()
        filter_list.sort()
        filter_dict[filter_name] = st.multiselect(f'Select {filter_name}', filter_list)
    
    if st.button('Apply filter'):
        df_filter = dataframe_filter(df, **filter_dict)

        st.subheader('Row data')
        st.write(df_filter)
        
        st.subheader('Header')
        length = min(40, len(df_filter)-1)
        for _, row in df_filter.head(length).iterrows():
            st.write(f"{row['label']}: {'⭐' * row['star']}/5")
            st.write(row['avis'])
            st.write("---")

with graph_table:
    st.subheader('Graphs')
    plot_reviews_by_stars(df)
    plot_average_star_by_category(df)
    plot_average_star_by_insurer(df)
    plot_number_of_reviews_by_insurer(df)
    plot_categories_by_insurer(df)