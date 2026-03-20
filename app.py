import streamlit as st
import pandas as pd
import plotly.express as px

# TITLE
st.title("STL MODEL")
st.subheader("Structured Intelligence Engine")

# DATA INPUT (Applications Layer)
channel = st.selectbox("Select Channel", ["Online", "Store"])
revenue = st.number_input("Enter Revenue", value=100)

# STORE DATA (Pipelines → Storage)
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["channel", "revenue"])

new_data = pd.DataFrame([[channel, revenue]], columns=["channel", "revenue"])
st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)

data = st.session_state.data

# VISUALIZATION (Storage → Intelligence)
if not data.empty:
    fig = px.bar(data, x="channel", y="revenue", title="Revenue by Channel")
    st.plotly_chart(fig)

# INTELLIGENCE LAYER
if not data.empty:
    total = data["revenue"].sum()
    st.write("Total Revenue:", total)

    online = data[data["channel"] == "Online"]["revenue"].sum()
    store = data[data["channel"] == "Store"]["revenue"].sum()

    st.write("Online Revenue:", online)
    st.write("Store Revenue:", store)

    # DECISION ENGINE
    if online > store:
        st.success("Insight: Online channel is dominant")
    elif store > online:
        st.warning("Insight: Store channel is dominant")
    else:
        st.info("Insight: Channels are balanced")
