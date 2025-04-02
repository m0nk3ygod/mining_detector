import streamlit as st
import pandas as pd
import time

st.title("Mining Detection Dashboard")

resource_placeholder = st.empty()
anomaly_placeholder = st.empty()

while True:
    try:
        resource_df = pd.read_csv("resource_log.txt")
        resource_placeholder.subheader("Resource Usage")
        resource_placeholder.line_chart(resource_df)

        anomaly_df = pd.read_csv("anomaly_log.txt")
        anomaly_placeholder.subheader("Anomaly Detection")
        anomaly_placeholder.dataframe(anomaly_df.tail(10))
    except Exception as e:
        st.warning(f"Waiting for data... ({e})")

    time.sleep(5)
