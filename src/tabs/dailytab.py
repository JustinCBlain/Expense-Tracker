"""Tab for displaying spending over time"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit_echarts as st_echarts
import pandas as pd

# Example line graph
def generate_example_graph(entries):
    """
    Displays spending over time
    """
    # Getting Data ready for echarts
    if entries.empty:
        st.write("Entries dataframe is empty.")
        return

    required_columns = ['Category', 'Amount', 'Date']
    if not all(col in entries.columns for col in required_columns):
        st.write(f"Missing required columns: {', '.join(required_columns)}")
        return

    # Convert Amount to numeric if necessary
    entries['Amount'] = pd.to_numeric(entries['Amount'], errors='coerce')

    # Convert Date to Date Time if necessary
    entries['Date'] = pd.to_datetime(entries['Date'], errors='coerce')
    
    # Drop rows where 'Amount' is NaN
    entries = entries.dropna(subset=['Amount', 'Date'])

    if entries.empty:
        st.write("No valid spending data available after cleaning.")
        return

    # Pivot data so each category becomes a separate series
    pivot_data = entries.pivot_table(index='Date', columns='Category', values='Amount', aggfunc='sum')

    st.write(entries.head())

    if pivot_data.empty:
        st.write("No valid spending data available.")
        return

    pivot_data = pivot_data.fillna(0)

    # Prepare Data for echarts
    x_data = pivot_data.index.strftime('%Y-%m-%d').tolist()

    data_as_lists = pivot_data.values.tolist()

    series_data = [
        {
            "name": category,
            "type": "line",
            "stack": "total",
            "data": pivot_data[category].tolist(),
        }
        for category in pivot_data.columns
    ]

    st.write("Category:", pivot_data)
    st.write("Lists:", data_as_lists)
    st.write("X Data:", x_data)
    st.write("Series Data:", series_data)

    # Echarts stacked config
    option = {
        "title": {
            "text": "Stacked Line Chart",
            "left": "center"
        },
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "cross",
                "crossStyle": {
                    "color": "#999"
                }
            }
        },
        "legend": {
            "data": pivot_data.columns.tolist(),
        },
        "xAxis": {
            "type": "category",
            "data": x_data,
            "name": "Date",
            "axisLabel": {
                "rotate": 45
            }
        },
        "yAxis": {
            "type": "value",
            "name": "Amount",
        },
        "series": series_data
    }

    # Render Chart using streamlit_echarts
    try:
        st_echarts.st_echarts(options=option, height="600px")
    except Exception as e:
        st.write(f"Error in rendering the chart: {e}")
        import traceback
        st.write(traceback.format_exc())
