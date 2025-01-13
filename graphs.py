import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_reviews_by_stars(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='star', data=df, palette='viridis')
    plt.title('Number of Reviews by Stars')
    plt.xlabel('Stars')
    plt.ylabel('Number of Reviews')
    plt.grid(True)
    st.pyplot(plt)

def plot_average_star_by_category(df):
    avg_star_by_category = df.groupby('label')['star'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='star', y='label', data=avg_star_by_category, palette='viridis')
    plt.title('Average Star Rating by Category')
    plt.xlabel('Average Star Rating')
    plt.ylabel('Category')
    plt.grid(True)
    st.pyplot(plt)