import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


st.text("Hello, Streamlit!")

# Add a checkbox to switch between Seaborn and Plotly
chart_type = st.radio(
    "Choose Chart Library:",
    ("Plotly", "Seaborn")
)

# load dataset
data = sns.load_dataset("iris")

if chart_type == "Plotly":
    # Create a Plotly chart
    fig = px.scatter(
        data,
        x="sepal_length",
        y="sepal_width",
        color="species",
        title="Iris Sepal Dimensions (Plotly)",
        labels={"sepal_length": "Sepal Length", "sepal_width": "Sepal Width"}
    )
    # Display the Plotly chart
    st.plotly_chart(fig)
else:
    # Create a Seaborn chart
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=data,
        x="sepal_length",
        y="sepal_width",
        hue="species",
        ax=ax
    )
    ax.set_title("Iris Sepal Dimensions (Seaborn)")
    # Display the Seaborn chart
    st.pyplot(fig)
