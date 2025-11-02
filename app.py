import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analysis Assistant", layout="wide")

st.title("📊 Data Analysis Assistant")

# Upload datasetpip show streamlit
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📑 Dataset Info")
    st.write("Rows:", df.shape[0], " | Columns:", df.shape[1])
    st.write("Columns:", list(df.columns))

    # Summary stats
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # Null values
    st.subheader("⚠️ Missing Values")
    st.write(df.isnull().sum())

    # Chart selection
    st.subheader("📊 Visualizations")
    chart_type = st.selectbox("Choose a chart", ["Histogram", "Line Chart", "Bar Chart"])

    column = st.selectbox("Select column", df.columns)

    if chart_type == "Histogram":
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=20)
        st.pyplot(fig)

    elif chart_type == "Line Chart":
        st.line_chart(df[column])

    elif chart_type == "Bar Chart":
        st.bar_chart(df[column].value_counts())

    # Auto Report
    st.subheader("📝 Auto Report")
    st.write(f"- Dataset has **{df.shape[0]} rows** and **{df.shape[1]} columns**.")
    st.write("- Numerical summary provided above.")
    st.write("- Use visualizations to explore distributions and trends.")
else:
    st.info("Please upload a dataset to begin.")
