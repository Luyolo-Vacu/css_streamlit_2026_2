# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 18:17:00 2026

@author: Wits-User
"""
import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Contact"],)


if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    name = "Luyolo Vacu"
    field = "Computational Chemistry"
    institution = "University of the Witwatersrand"

    st.subheader(name)
    st.write(f"**Field:** {field}")
    st.write(f"**Institution:** {institution}")

    st.markdown("""
    ### Research Interests
    - Computational chemistry and molecular modeling  
    - AI-driven multi-target drug discovery  
    - Molecular dynamics and enhanced sampling techniques  
    - Sustainable and green formulation science  

    ### Current Focus
    My research focuses on integrating AI and molecular simulations to improve
    bioavailability, toxicity, and metabolism prediction in drug candidates
    """)

    st.subheader("Skills")
    st.markdown("""
    - Molecular modeling & simulation  
    - Data analysis (Python, Pandas, NumPy)  
    - Laboratory formulation & quality testing  
    - Scientific reporting & method validation  
    """)

    st.image(
        "https://www.itheoc.uni-stuttgart.de/img/computational_chemistry.jpg?__scale=w:1000,h:1000,q:100,t:3.jpg",
        caption="Computational & Molecular Research"
    )
    
elif menu == "Contact":
        # Add a contact section
        st.header("Contact Information")
        email = "luyolovacu97@gmail.com"

        st.write(f"You can reach me at {email}.")
