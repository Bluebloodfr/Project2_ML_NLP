import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_reviews_by_stars(df):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.countplot(x='star', data=df, palette='viridis')
    plt.title('Number of Reviews by Stars')
    plt.xlabel('Stars')
    plt.ylabel('Number of Reviews')
    plt.grid(True)
    st.pyplot(plt)

def plot_average_star_by_category(df):
    avg_star_by_category = df.groupby('label')['star'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.set_style("darkgrid")
    sns.barplot(x='star', y='label', data=avg_star_by_category, palette='magma')
    plt.title('Average Star Rating by Category')
    plt.xlabel('Average Star Rating')
    plt.ylabel('Category')
    plt.grid(True)
    st.pyplot(plt)

def plot_average_star_by_insurer(df):
    avg_star_by_insurer = df.groupby('insurer')['star'].mean().reset_index()
    plt.figure(figsize=(10, 12))
    sns.set_style("white")
    sns.barplot(x='star', y='insurer', data=avg_star_by_insurer, palette='coolwarm')
    plt.title('Average Star Rating by Insurer')
    plt.xlabel('Average Star Rating')
    plt.ylabel('Insurer')
    plt.grid(True)
    st.pyplot(plt)

def plot_number_of_reviews_by_insurer(df):
    reviews_by_insurer = df['insurer'].value_counts().reset_index()
    reviews_by_insurer.columns = ['insurer', 'count']
    plt.figure(figsize=(10, 12))
    sns.set_style("ticks")
    sns.barplot(x='count', y='insurer', data=reviews_by_insurer, palette='cubehelix')
    plt.title('Number of Reviews by Insurer')
    plt.xlabel('Number of Reviews')
    plt.ylabel('Insurer')
    plt.grid(True)
    st.pyplot(plt)

def plot_categories_by_insurer(df):
    categories_by_insurer = df.groupby(['insurer', 'label']).size().reset_index(name='count')
    top_categories_by_insurer = categories_by_insurer.groupby('insurer').apply(lambda x: x.nlargest(3, 'count')).reset_index(drop=True)
    pivot_df = top_categories_by_insurer.pivot(index='insurer', columns='label', values='count').fillna(0)
    pivot_df.plot(kind='bar', stacked=True, figsize=(14, 10), colormap='viridis')
    plt.title('Top Categories by Insurer')
    plt.xlabel('Insurer')
    plt.xticks(rotation=60)
    plt.ylabel('Number of Reviews')
    plt.legend(title='Category')
    plt.grid(True)
    st.pyplot(plt)