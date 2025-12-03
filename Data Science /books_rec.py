import pandas as pd 
import streamlit as st 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

df = pd.read_csv("books.csv")
df['title'] = df['title'].str.strip()
df['description'] = df['description'].fillna("")

vectorizer = TfidfVectorizer(stop_words = 'english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()

def get_recommendations(title, df, cosine_sim, indices):
    title = title.strip().lower()
     
    

    if title not in indices.index:
        return f"{title} not in records."
    
     #this is why we created the pd series, or else we would have to loop through the 
    #entire line
    
    idx = indices.loc[title]

    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]


st.title("Book Recommendation Engine")
st.write("Enter a Book Title and get similar recommendations")
selected_book = st.text_input("Book: title")

if selected_book:
    results = get_recommendations(selected_book, df, cosine_sim, indices)
    if isinstance(results, pd.DataFrame):
        st.table(results)
    else:
        st.warning(results)
