import streamlit as st

# Class to manage multiple pages in the Streamlit app
class MultiPage:
    def __init__(self, app_name: str) -> None:
        """
        Initialize the MultiPage class with the application name.
        
        Args:
        app_name (str): The name of the application.
        """
        self.pages = []  # List to store pages
        self.app_name = app_name  # Store the application name

        # Configure the Streamlit page with title and icon
        st.set_page_config(
            page_title=self.app_name,
            page_icon="🌿",
        )

    def add_page(self, title: str, func) -> None:
        """
        Add a new page to the app.
        
        Args:
        title (str): Title of the page.
        func (function): Function to render the content of the page.
        """
        self.pages.append({"title": title, "function": func})

    def run(self) -> None:
        """
        Run the Streamlit app, displaying the sidebar and executing the selected page.
        """
        st.sidebar.title(f"Navigate {self.app_name}")
        page = st.sidebar.radio(
            "Menu", self.pages, format_func=lambda page: page['title']
        )
        page['function']()