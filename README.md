# Assurance Review Analysis

### Description
This project analyzes user reviews related to insurance services. Through data cleaning, sentiment analysis, topic classification, and summarization, it provides insights into customer satisfaction and highlights recurring themes across various insurers.

## Table of Contents

1. Project Overview
2. Data
3. Installation
4. Usage
5. Project Structure
6. Authors
7. License

## Project Overview

- Objective: Leverage NLP techniques to derive meaningful insights from insurance-related reviews, including sentiment polarity, dominant discussion topics, and summarized feedback.
- Key Features:
  - Data cleaning and preprocessing of multilingual reviews (French & English).
  - Sentiment prediction using a pre-trained multilingual model.
  - Topic classification via zero-shot learning.
  - Summarization of lengthy reviews.
  - Interactive dashboards and visualizations built with Streamlit.

## Data

Dowload the data from the following [link](https://drive.google.com/file/d/1_kg5JzAzntzLI6eGM3_vmUSoeWk7f8ip/view) and unzip it in the folder data/assurance

## Installation

1. Clone or Download this repository.
```
git clone https://github.com/Bluebloodfr/Project2_ML_NLP.git
```
2. Create and Activate a virtual environment (recommended).
```
# Using Python's built-in venv:
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```
3. Install Dependencies from requirements.txt or a similar file.
```
pip install -r requirements.txt
```

## Usage

1. Download and Prepare the Data
- Follow the steps in the Data section to place your data in the correct directory.

2. Run the Streamlit App
```
streamlit run app.py
```
- This command launches the interactive dashboard in your default web browser.
- Analysis Tab: Displays sample reviews with predicted sentiment scores and topic classifications.
- Graphs Tab: Visualizes the entire dataset through charts (number of reviews by star rating, average rating by category, etc.).

3. Explore Other Notebooks/Code
- You can also open and explore the Jupyter notebooks in the notebooks/ folder (if applicable) for deeper insights into data preprocessing, model training, and evaluation.

## Project Structure
```
Project2_ML_NLP/
│
├─ app.py                      # Main Streamlit app script
├─ requirements.txt           # Dependencies
├─ data/
│   └─ assurance/             # Contains the unzipped data files
├─ notebooks/                 # Jupyter notebooks (optional)
├─ scripts/                   # Scripts for cleaning, training, etc. (optional)
├─ graphs.py                  # Visualization functions used by Streamlit
├─ README.md                  # This README
└─ ...
```
- app.py: Implements the Streamlit application logic for both the Analysis and Graphs tabs.
- graphs.py: Defines functions to generate Matplotlib/Seaborn plots used in the Graphs tab.
- data/assurance/: Should contain the .xlsx or .csv files with user reviews after unzipping.

## Authors

Louis-Melchior GIRAUD (DIA2) \
Ruben LEON (DIA3) \
Feel free to reach out with any questions or suggestions.

## License

Free
