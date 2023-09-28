import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# getting path of directory
path = os.path.dirname(__file__)
# dataset path
dataset_path = path + '/mountain_flowers.csv'
# reading the dataset
mountain_flowers = pd.read_csv(dataset_path)

category = mountain_flowers['name']
petal_lengths = mountain_flowers['petal_length']

# Create a bar chart
plt.bar(category, petal_lengths)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Petal Lengths')
plt.title('Comparison of Petal Lengths of Mountain Flowers')

# Rotate x-axis labels if they are long
plt.xticks(rotation=45, ha='right')

st.pyplot(plt)
st.write("**Analysis/Observation:**") 
st.write("Thus we can see observe the following points from the above graph: \n"
"1. Violet category has the shortest petal length. \n"
"2. Colorado lotus category has the longest petal length.")

st.write('**Detailed Data View of caetgories and Petal Length**')
name_petal_length_df = mountain_flowers[['name', 'petal_length']]
st.write(name_petal_length_df)


