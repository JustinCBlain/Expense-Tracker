import streamlit as st
import plotly.express as px

def generate_example_pie_chart(entries):
    if not entries.empty:
        # Calculate total cost per category
        category_costs = entries.groupby('Category')['Cost'].sum().reset_index()
        category_costs.columns = ['Category', 'Total Cost']

        # Create a pie chart
        fig = px.pie(category_costs, values='Total Cost', names='Category', title='Expense Distribution by Category')

        # Render the chart in Streamlit
        st.plotly_chart(fig)
    else:
        st.write("No data available for the pie chart.")
