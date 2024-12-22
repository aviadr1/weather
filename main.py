import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
df = sns.load_dataset("penguins")

# Sidebar for plot selection
plot_choice = st.radio("Choose your plot library:", ["Seaborn", "Plotly"])

if plot_choice == "Seaborn":
    # Seaborn plot
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=ax)
    st.pyplot(fig)
elif plot_choice == "Plotly":
    # Plotly plot
    fig = px.scatter(
        df,
        x="flipper_length_mm",
        y="bill_length_mm",
        color="species",
        title="Penguins: Flipper Length vs Bill Length",
    )
    st.plotly_chart(fig)

