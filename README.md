# 🎨GitHub Portfolio

This project is a portfolio application for displaying GitHub repositories in a visually appealing manner using Streamlit. The application fetches data from a specified GitHub username and presents it with various interactive charts and filters.

## ✨ Features

- **Responsive UI**: Modern and clean user interface with custom CSS styling.
- **Interactive Charts**: Visualize GitHub repositories using pie charts, bar charts, and advanced Altair charts.
- **Filters**: Filter repositories by programming language and star count.
- **Dynamic Updates**: Automatically updates the list of repositories and charts based on user input.

## 🛠️ Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/faezedrx/github-portfolio.git
    cd github-portfolio
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## 🚀 Usage

1. Open your web browser and go to `http://localhost:8501`.
2. Enter your GitHub username in the sidebar input field.
3. Use the filters in the sidebar to customize the displayed data:
    - **Filter by Language**: Select the programming languages to filter repositories.
    - **Minimum Star Count**: Use the slider to filter repositories by the minimum number of stars.
4. Explore the interactive charts and repository list.

** or check [this](https://app-portfolio.streamlit.app/) website**

## 🎨 Customization

You can customize the look and feel of the application by modifying the CSS styles in the `app.py` file. Additional functionality can be added by extending the Streamlit code.

## 📋 Requirements

- Python 3.7 or higher
- Streamlit
- Pandas
- Requests
- Matplotlib
- Plotly
- Altair

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the existing style and add appropriate tests.


## 💡 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/python/)
- [Altair](https://altair-viz.github.io/)

