import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setze den Titel der App
st.title("JK Streamlit App")

# Lade ein Beispiel-Datenset aus dem Internet
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    return pd.read_csv(url)

data = load_data()

# Zeige die Daten in einer Tabelle an
st.subheader("Datensatz")
st.write(data.head())

# Wähle eine Visualisierungsmethode
visualization = st.radio(
    "Wähle eine Visualisierungsmethode",
    ('Tabelle', 'Scatterplot', 'Histogramm')
)

# Eingabefelder zur Steuerung der Anzeige
if visualization == 'Tabelle':
    st.dataframe(data)

elif visualization == 'Scatterplot':
    x_axis = st.selectbox('Wähle die x-Achse', data.columns)
    y_axis = st.selectbox('Wähle die y-Achse', data.columns)
    fig, ax = plt.subplots()
    sns.scatterplot(x=data[x_axis], y=data[y_axis], ax=ax)
    st.pyplot(fig)

elif visualization == 'Histogramm':
    column = st.selectbox('Wähle eine Spalte für das Histogramm', data.columns)
    bins = st.slider('Anzahl der Bins', 5, 50, 20)
    fig, ax = plt.subplots()
    ax.hist(data[column].dropna(), bins=bins)
    st.pyplot(fig)