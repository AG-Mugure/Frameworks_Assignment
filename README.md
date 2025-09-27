# 📊 COVID-19 Research Papers Explorer (CORD-19 Metadata)

This project provides a **simple exploration of COVID-19 research papers** using the [CORD-19 metadata dataset](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge).  
It demonstrates **data loading, cleaning, analysis, visualization, and interactive exploration** through a Streamlit app.  

---

##  Project Structure

- **Part 1: Data Loading & Basic Exploration**  
  - Load the `metadata.csv` dataset.  
  - Inspect rows, columns, datatypes, and missing values.  

- **Part 2: Data Cleaning & Preparation**  
  - Handle missing data by dropping unnecessary or incomplete columns/rows.  
  - Convert `publish_time` to datetime and extract publication year.  
  - (Optional) Calculate word counts for abstracts.  

- **Part 3: Data Analysis & Visualization**  
  - Publications per year.  
  - Top publishing journals.  
  - Word frequency in titles.  
  - Word cloud of research paper titles.  
  - Distribution of papers by source.  

- **Part 4: Streamlit Application**  
  - Interactive year range filter.  
  - Display filtered results and summary.  
  - Visualize publications by year in real time.  

- **Part 5: Documentation & Reflection**  
 Reflection

Challenges:

-Handling missing data (especially abstracts).

-Ensuring date formats were parsed correctly.

-Large dataset slowed down visualizations.

Learnings:

-Gained practical skills in cleaning real-world datasets.

-Learned to visualize patterns in research data.

-Streamlit makes it easy to build interactive dashboards.  


Future Work

-Improve text analysis with NLP (topic modeling, sentiment analysis).

-Add more interactivity to Streamlit app (filters by journal, keyword search).

-Deploy the app online for easier access.
---

## 🛠️ Requirements

Install dependencies before running the notebook and Streamlit app:

```bash
pip install pandas matplotlib seaborn wordcloud streamlit

