import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CORD-19 Research Dataset Explorer")

# Load data
df = pd.read_csv('metadata.csv')
df['year'] = pd.to_datetime(df['publish_time'], errors='coerce').dt.year

# Sidebar
st.sidebar.header("Filters")
year_filter = st.sidebar.slider("Select Year", int(df['year'].min()), int(df['year'].max()), (2019, 2023))

filtered_df = df[(df['year'] >= year_filter[0]) & (df['year'] <= year_filter[1])]

st.write(f"### Showing papers from {year_filter[0]} to {year_filter[1]}")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'year']].head(10))

# Visualization
st.write("### Publications by Year")
year_counts = df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)
