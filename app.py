import streamlit as st
from gurobipy import Model, GRB
import matplotlib.pyplot as plt
import pandas as pd
import json
import webbrowser
import requests
import re

# **********************************************#
# Data Handling
# **********************************************#
# Load data from JSON file


# **********************************************#
# === Streamlit Layout ===
# **********************************************#
st.set_page_config(page_title="Factory Planning Optimization", page_icon=":bar_chart:", layout="wide")
st.markdown("""
    <style>
        .title-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #f4f4f9;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
            color: #333;
        }
        .title-bar h1 {
            margin: 0;
            font-size: 49px;
            color: #333;
            margin-left: 20px;
        }
        .title-bar .logo1 {
            max-width: auto;
            height: 60px;
            margin-right: 20px;
        }
        .title-bar a {
            text-decoration: none;
            color: #0073e6;
            font-size: 16px;
        }
        .footer-text {
            font-size: 20px;
            background-color: #f4f4f9;
            text-align: left;
            color: #333;
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
        }
    </style>
    <div class="title-bar">
        <h1>Problem 12.1 <br> Food Manufacture</h1>
        <div>
            <a href="https://decisionopt.com" target="_blank">
                <img src="https://decisionopt.com/static/media/DecisionOptLogo.7023a4e646b230de9fb8ff2717782860.svg" class="logo1" alt="Logo"/>
            </a>
        </div>
    </div>
    <div class="footer-text">
    <p style="margin-left:20px;">  'Model Building in Mathematical Programming, Fifth Edition' by H. Paul Williams</p>
    </div>    
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .container-c1 p {
            font-size: 20px;
        }
        .button {
            background-color: #FFFFFF;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
        .button:hover {
            background-color: #FFFFFF;
             box-shadow: 1px 1px 4px rgb(255, 75, 75); /* Shadow effect on hover */
        }
    </style>
    <div class="container-c1">
        <br><p> For a detailed view of the mathematical formulation, please visit my 
        <a href="https://github.com/Ash7erix/Model_Building_Assignments/tree/main/12.1_Food_Manufacture">Github</a> page.</p>

    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .container-c1 p {
            font-size: 20px;
        }
    </style>
    <div class="container-c1">
        <br><p >This app optimizes the food manufacturing process by selecting the best oils to refine 
        each month, maximizing profit. It uses <b>Gurobi</b> for optimization, considering factors like oil 
        costs, refining capacities, storage limits, and hardness constraints.</p> 
        <br><p>You can also adjust the parameters like refining capacities, storage costs, and oil prices, 
        using the options on the left side and the app provides detailed results including oil purchase, 
        refining, storage, and production data for each month.</p>
    </div>
""", unsafe_allow_html=True)

# **********************************************#
# Convert the prices dictionary into a DataFrame for display
# **********************************************#
st.title("Optimization Data and Constraints:")
st.markdown("""
    <style>
        .container-c1 p {
            font-size: 20px;
        }
    </style>
    <div class="container-c1">
        <br><p> You can view the mathematical formulation below by clicking the button.</p>
    </div>
""", unsafe_allow_html=True)

if st.button('Display Formulation'):
    def fetch_readme(repo_url):
        raw_url = f"{repo_url}/raw/main/12.1_Food_Manufacture/README.md"  # Adjust path if necessary
        response = requests.get(raw_url)
        return response.text


    repo_url = "https://github.com/Ash7erix/Model_Building_Assignments"
    try:
        readme_content = fetch_readme(repo_url)
        st.markdown(readme_content)
    except Exception as e:
        st.error(f"Could not fetch README: {e}")

# **********************************************#
#           Sidebar for user inputs
# **********************************************#



# **********************************************#
#              Optimization Model
# **********************************************#


# **********************************************#
# Solve Model when the button is clicked
# **********************************************#
st.markdown("""
    <style>
        .container-c2 p {
            font-size: 20px;
            margin-bottom: 20px;
        }
    </style>
    <div class="container-c2">
        <br><p>Click on the button below to solve the optimization problem.</p>
    </div>
""", unsafe_allow_html=True)
if st.button("Solve Optimization"):
        st.markdown("""
            <style>
                footer {
                    text-align: center;
                    background-color: #f1f1f1;
                    color: #333;
                    font-size: 19px;
                    margin-bottom:0px;
                }
                footer img {
                    width: 44px; /* Adjust size of the logo */
                    height: 44px;
                }
            </style>
            <footer>
                <h1>Author- Ashutosh <a href="https://www.linkedin.com/in/ashutoshpatel24x7/" target="_blank">
                <img src="https://decisionopt.com/static/media/LinkedIn.a6ad49e25c9a6b06030ba1b949fcd1f4.svg" class="img" alt="Logo"/></h1>
            </footer>
        """, unsafe_allow_html=True)
        st.markdown("""---
        """, unsafe_allow_html=True)

else:
    st.write("No optimal solution found.")
    st.markdown("""
        <style>
        footer {
            text-align: center;
            background-color: #f1f1f1;
            color: #333;
            font-size: 19px;
        }
        footer img {
            width: 44px; /* Adjust size of the logo */
            height: 44px;
        }
        </style>
        <footer>
            <h1>Author- Ashutosh <a href="https://www.linkedin.com/in/ashutoshpatel24x7/" target="_blank">
            <img src="https://decisionopt.com/static/media/LinkedIn.a6ad49e25c9a6b06030ba1b949fcd1f4.svg" class="img" alt="Logo"/></h1>
        </footer>
        """, unsafe_allow_html=True)
    st.markdown("""---""")
