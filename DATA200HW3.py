import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

path = os.path.dirname(__file__)
file_path =  path + '/toy_dataset.csv'
data = pd.read_csv(file_path)
data.head()

gen_count = data['Gender'].value_counts()

plt.bar(gen_count.index, gen_count.values, color='Red')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender in Dataset')
plt.show()

st.pyplot(plt)
