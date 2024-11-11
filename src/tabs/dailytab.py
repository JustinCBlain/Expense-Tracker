"""Tab for displaying spending over time"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Example line graph
def generate_example_graph():
    """
    Displays spending over time
    """
    # Fake data for line graph
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Creating plot
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Fake Data', color='blue')
    plt.title("Example Graph")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend()
    plt.grid()

    # Show plot in Streamlit Widget
    st.pyplot(plt)
