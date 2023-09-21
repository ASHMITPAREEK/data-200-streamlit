import pandas as pd
import matplotlib.pyplot as plt
file_path = 'https://github.com/ASHMITPAREEK/data-200-streamlit/blob/main/toy_dataset.csv'
data = pd.read_csv(file_path)
data.head()
gen_count = data['Gender'].value_counts()

plt.bar(gen_count.index, gen_count.values, color='skyblue')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender in Toy Dataset')
plt.show()