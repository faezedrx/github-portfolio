import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

# Page configuration
st.set_page_config(page_title="GitHub Portfolio", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffecd2, #fcb69f);
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .main {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .main:hover {
        transform: scale(1.01);
    }
    .sidebar .sidebar-content {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        color: #ff6f61;
        text-shadow: 2px 2px #fcb69f;
    }
    .stButton button {
        background-color: #ff6f61;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 10px;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #ff6f61;
    }
    .stTextInput input {
        border-radius: 5px;
        border: 2px solid #ff6f61;
    }
    .stMultiselect div {
        border-radius: 5px;
        border: 2px solid #ff6f61;
    }
    .stSlider > div > div > div {
        background-color: #ff6f61;
    }
    </style>
    """, unsafe_allow_html=True)

# Fetch data from GitHub
@st.cache_data
def get_github_data(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json()

# Title
st.title("GitHub Portfolio")

# Sidebar settings
st.sidebar.title("Settings")
username = st.sidebar.text_input("GitHub Username:", "faezedrx")
github_link = f"https://github.com/{username}?tab=repositories"
st.sidebar.markdown(f"[View GitHub Profile]({github_link})", unsafe_allow_html=True)

# Filter by programming language
language_filter = st.sidebar.multiselect("Filter by Language:", options=[], default=[])

# Filter by star count
star_filter = st.sidebar.slider("Minimum Star Count:", 0, 100, 0)

# Chart options
show_pie_chart = st.sidebar.checkbox("Show Pie Chart by Language", True)
show_bar_chart = st.sidebar.checkbox("Show Bar Chart for Stars and Forks", True)

if username:
    data = get_github_data(username)

    # Convert data to DataFrame
    df = pd.DataFrame(data)
    if df.empty:
        st.write("No projects found.")
    else:
        # Filter data
        if language_filter:
            df = df[df['language'].isin(language_filter)]
        df = df[df['stargazers_count'] >= star_filter]

        if df.empty:
            st.write("No projects match the filters.")
        else:
            # Update language filter options
            st.sidebar.multiselect("Filter by Language:", options=df['language'].unique(), default=language_filter)

            # Display project list
            st.subheader("Project List")
            st.write(df[['name', 'html_url', 'stargazers_count', 'forks_count', 'language']])

            # Display charts
            if show_pie_chart:
                st.subheader("Project Distribution by Language")
                fig = px.pie(df, names='language', title='Projects by Language')
                st.plotly_chart(fig)

            if show_bar_chart:
                st.subheader("Stars and Forks Comparison")
                fig, ax = plt.subplots()
                ax.barh(df['name'], df['stargazers_count'], color='#ff6f61', label='Stars')
                ax.barh(df['name'], df['forks_count'], color='#fcb69f', label='Forks', left=df['stargazers_count'])
                ax.set_xlabel('Count')
                ax.set_title('Stars and Forks Comparison')
                ax.legend()
                st.pyplot(fig)

            # Display advanced Altair chart
            st.subheader("Advanced Project Chart")
            chart = alt.Chart(df).mark_point().encode(
                x='stargazers_count:Q',
                y='forks_count:Q',
                color='language:N',
                tooltip=['name', 'html_url']
            ).interactive().properties(
                width='container',
                height=400,
                title='Stars and Forks by Language'
            )
            st.altair_chart(chart, use_container_width=True)
