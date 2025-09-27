# 📊 Data Analysis Project: CORD-19 Metadata Dataset



##Part 1: Data Loading and Basic Exploration

### Load Dataset
## We used the **CORD-19 metadata.csv** file.


import pandas as pd

try:
    df = pd.read_csv('metadata.csv')
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("Error: metadata.csv not found")
except Exception as e:
    print(f"Unexpected error: {e}")


### Inspect Data

print(df.head())          # First 5 rows
print(df.shape)           # Rows, Columns
print(df.info())          # Structure, datatypes
print(df.isnull().sum())  # Missing values per column


##**Findings:**
##- Metadata contains publication info: title, abstract, authors, publish_time, source, etc.
##- Several columns have missing values (common in large datasets).



##Part 2: Data Cleaning and Preparation

### Handle Missing Data

# Drop columns with too many missing values
df = df.drop(columns=['abstract'], errors='ignore')

# Drop rows missing essential info like title or publish_time
df = df.dropna(subset=['title','publish_time'])

### Prepare Data

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Create abstract word count (if abstract column exists)
if 'abstract' in df.columns:
    df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))



## Part 3: Data Analysis and Visualization

### Analysis

# Publications per year
year_counts = df['year'].value_counts().sort_index()

# Top journals
top_journals = df['journal'].value_counts().head(10)

# Word frequency in titles
from collections import Counter
import re

words = " ".join(df['title'].dropna().tolist()).lower()
words = re.findall(r'\b[a-z]{3,}\b', words)
word_freq = Counter(words).most_common(20)

### Visualizations

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Publications over time
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Top publishing journals
plt.figure(figsize=(8,5))
top_journals.plot(kind='bar')
plt.title("Top Journals Publishing COVID-19 Research")
plt.ylabel("Count")
plt.show()

# Word cloud of titles
wc = WordCloud(width=800, height=400, background_color='white').generate(" ".join(words))
plt.figure(figsize=(10,6))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.title("Most Frequent Words in Titles")
plt.show()

# Distribution of paper counts by source
plt.figure(figsize=(8,5))
sns.countplot(x='source_x', data=df, order=df['source_x'].value_counts().index[:10])
plt.title("Top Sources of Papers")
plt.xticks(rotation=45)
plt.show()




## Part 4: Streamlit Application


import streamlit as st

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Year range slider
year_range = st.slider("Select year range", 2015, 2023, (2019, 2021))

# Filter data by selection
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write("Number of papers in selected range:", filtered.shape[0])

# Show sample data
st.dataframe(filtered.head())

# Plot publications over time
counts = filtered['year'].value_counts().sort_index()
st.bar_chart(counts)


