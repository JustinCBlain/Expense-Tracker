"""Generates pie/donut charts"""

import streamlit as st
import streamlit_echarts as st_echarts
import pandas as pd

def generate_example_pie_chart(entries):
    """Generates charts to display spending categories/vendors/etc

    Args:
        entries (dataframe): Pandas dataframe to display
    """
    if entries.empty:
        st.write("Entries dataframe is empty.")
        return

    required_columns = ['Category', 'Amount']
    if not all(col in entries.columns for col in required_columns):
        st.write(f"Missing required columns: {', '.join(required_columns)}")
        return

    # Convert Amount to numeric if necessary
    entries['Amount'] = pd.to_numeric(entries['Amount'], errors='coerce')
    
    # Drop rows where 'Amount' is NaN
    entries = entries.dropna(subset=['Amount'])

    if entries.empty:
        st.write("No valid spending data available after cleaning.")
        return

    # Calculate total cost per category
    category_costs = entries.groupby('Category')['Amount'].sum().reset_index()

    if category_costs.empty:
        st.write("No valid spending data available.")
        return

    # Prepare Data for echarts
    donut_data = [{"name": row['Category'], "value": row['Amount']} for _, row in category_costs.iterrows()]

    # Echarts donut config
    option = {
        "title": {
            "text": "Expense Distribution by Category",
            "subtext": "Total Cost",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item",
            "formatter": "{b}: {c} ({d}%)"
        },
        "series": [
            {
                "name": "Total Cost",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "label": {
                    "show": True,
                    "position": "center"
                },
                "emphasis": {
                    "label": {
                        "show": True,
                        "fontSize": "20",
                        "fontWeight": "bold"
                    }
                },
                "data": donut_data
            }
        ]
    }

    # Render Chart using streamlit_echarts
    try:
        st_echarts.st_echarts(options=option, height="400px")
    except Exception as e:
        st.write(f"Error in rendering the chart: {e}")
        import traceback
        st.write(traceback.format_exc())
