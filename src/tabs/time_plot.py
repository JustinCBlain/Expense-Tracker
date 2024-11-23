"""Generates a scatterplot by time of day"""

from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import altair as alt


def generate_time_plot(entries):
    """
    Generates separate single-axis charts for each day in the selected date range,
    where 'time' is the x-axis and point size represents the expense amount.

    :param entries: A Pandas dataframe containing expense data
    """

    st.markdown("###### Daily Expense Timeline with Time as X-Axis")

    with st.container():
        # Ensure Date column is in datetime format
        entries["Date"] = pd.to_datetime(entries["Date"], errors="coerce")
        entries["Datetime"] = \
            pd.to_datetime(entries['Date'].astype(str) + ' ' + entries['Time'].astype(str))

        # Sidebar filters for date range and category selection
        min_date, max_date = entries["Date"].min(), entries["Date"].max()
        if entries.empty:
            max_date = datetime.now()
            min_date = max_date - timedelta(weeks=2)
        selected_date_range = st.date_input("Select Date Range", value=(min_date, max_date))
        if len(selected_date_range) == 2:
            entries = entries[(entries["Date"] >= pd.to_datetime(selected_date_range[0])) &
                              (entries["Date"] <= pd.to_datetime(selected_date_range[1]))]

        categories = st.multiselect(
            "Select categories for display",
            options=entries["Category"].unique(),
            default=entries["Category"].unique()
        )
        entries = entries[entries["Category"].isin(categories)]

        if entries.empty:
            st.warning("No data to display. Adjust your filters.")
            return

        # Create a separate chart for each day
        for day in entries['Date'].unique():
            day_data = entries[entries['Date'] == day]

            # Define the Altair chart for daily expenses with time on the x-axis
            chart = (
                alt.Chart(day_data)
                .mark_point(filled=True, opacity=0.6)
                .encode(
                    x=alt.X('hoursminutesseconds(Time):O',
                            title="Time of Day",
                            scale=alt.Scale(domainMin={"hours": 0, "minutes": 0, "seconds": 0},
                                            domainMax={"hours": 23, "minutes": 59, "seconds": 59}),
                            axis=alt.Axis(labelAngle=45)
                    ),
                    size=alt.Size('Amount:Q', scale=alt.Scale(range=[10, 300]), legend=None),
                    color='Category:N',
                    tooltip=['hoursminutesseconds(Time):O', 'Category:N', 'Amount:Q', 'Vendor:N']
                )
                .properties(
                    width=800,
                    height=175,
                    title=f"Expenses on {day.strftime('%Y-%m-%d')}"
                )
                .configure_axis(
                    labelAngle=0
                )
            )

            st.altair_chart(chart, use_container_width=True)
