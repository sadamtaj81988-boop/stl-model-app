import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("STL MODEL")
st.write("Structured Intelligence Engine")

# Sample data
data = pd.DataFrame({
    "channel": ["Online", "Store"],
    "revenue": [300, 200]
})


# Chart
fig = px.bar(data, x="channel", y="revenue", title="Revenue by Channel")
st.plotly_chart(fig)

# Total revenue
total = data["revenue"].sum()
st.write("Total Revenue:", total)

# Decision logic
if total > 400:
    st.success("HIGH PERFORMANCE")
else:
    st.warning("LOW PERFORMANCE")
