"""Tab for displaying spending over time"""

import streamlit as st
import pandas as pd
import altair as alt


def aggregate_data(df, period):
    """
    Aggregates data based on period

    :param df: pandas dataframe to aggregate on period
    :param period: string definition of period across which to aggregate
    """


    if period == "1 day":
        df["Period"] = df["Date"]
    elif period == "1 week":
        df["Period"] = df["Date"].dt.to_period("W").apply(lambda r: r.start_time)
    elif period == "1 month":
        df["Period"] = df["Date"].dt.to_period("M").apply(lambda r: r.start_time)
    else:
        st.error("Invalid aggregation period selected.")
        return df

    aggregated_data = (
        df.groupby(["Period", "Category"])["Amount"]
        .sum()
        .reset_index()
        .rename(columns={"Period": "Date"})
    )
    return aggregated_data

# Example line graph
def generate_example_graph(entries):
    """
    Generates a stacked line graph to display expenses

    :param entries: expense entries in a pandas dataframe
    """
    st.markdown("###### Spending Trends Over Time by Category")

    entries["Date"] = pd.to_datetime(entries["Date"], errors="coerce")

    # Sidebar for filtering
    categories = st.multiselect(
        "Select Categories",
        options=entries["Category"].unique(),
        default=entries["Category"].unique()
    )
    aggregation_period = st.selectbox(
        "Select Time Aggregation Period", ["1 day", "1 week", "1 month"], index=0
    )

    # Filter and aggregate data based on sidebar inputs
    filtered_data = entries[(entries["Category"].isin(categories))]
    aggregated_data = aggregate_data(filtered_data, aggregation_period)

    pivot_data = (
        aggregated_data.pivot(index="Date", columns="Category", values="Amount")
        .fillna(0)
    )

    # Plot the stacked line chart
    if not pivot_data.empty:
        chart = (
            alt.Chart(pivot_data.reset_index().melt("Date",
                                                    var_name="Category",
                                                    value_name="Amount"))
            .mark_area(opacity=0.6)
            .encode(
                x="Date:T",
                y="Amount:Q",
                color="Category:N",
                tooltip=["Date:T", "Category:N", "Amount:Q"]
            )
            .interactive()
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.warning("No data to display. Adjust your filters.")
