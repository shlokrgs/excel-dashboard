# frontend/app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import io

st.set_page_config(page_title="Excel Dashboard", layout="wide")

st.title("📊 Excel File Merger, Filter & Visualization App")

# Upload Excel Files
uploaded_files = st.file_uploader("Upload Multiple Excel Files", type=["xlsx"], accept_multiple_files=True)

if uploaded_files:
    # Merge all files into a single DataFrame
    dfs = []
    for uploaded_file in uploaded_files:
        df = pd.read_excel(uploaded_file)
        dfs.append(df)
    merged_df = pd.concat(dfs, ignore_index=True)

    st.success(f"Uploaded and merged {len(uploaded_files)} files!")

    # Show preview
    if st.checkbox("Show Merged Data Preview"):
        st.dataframe(merged_df.head(100))

    # Column selection
    selected_columns = st.multiselect("Select Columns to Keep", options=merged_df.columns.tolist(),
                                      default=merged_df.columns.tolist())

    if selected_columns:
        selected_df = merged_df[selected_columns]
        st.write("Filtered Columns Preview")
        st.dataframe(selected_df.head(50))

        # Filter Options
        filters = {}
        st.subheader("Apply Filters")
        for col in selected_columns:
            unique_vals = selected_df[col].unique().tolist()
            selected_vals = st.multiselect(f"Select values for {col} (optional)", unique_vals)
            if selected_vals:
                filters[col] = selected_vals

        filtered_df = selected_df.copy()
        for col, vals in filters.items():
            filtered_df = filtered_df[filtered_df[col].isin(vals)]

        st.success(f"Filtered data has {filtered_df.shape[0]} rows.")
        st.dataframe(filtered_df.head(50))

        # Download Filtered Data
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            filtered_df.to_excel(writer, index=False)
        st.download_button(
            label="📥 Download Filtered Data as Excel",
            data=output.getvalue(),
            file_name="filtered_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Visualization
        st.subheader("📈 Visualization Options")
        x_axis = st.selectbox("Select X-axis Column", options=selected_columns)
        y_axis = st.selectbox("Select Y-axis Column", options=selected_columns)

        if x_axis and y_axis:
            chart_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Pie Chart", "Trend Line"])

            if chart_type == "Bar Chart":
                fig = px.bar(filtered_df, x=x_axis, y=y_axis, title=f"Bar Chart: {y_axis} vs {x_axis}")
                st.plotly_chart(fig, use_container_width=True)
            elif chart_type == "Pie Chart":
                fig = px.pie(filtered_df, names=x_axis, values=y_axis, title=f"Pie Chart: {x_axis}")
                st.plotly_chart(fig, use_container_width=True)
            elif chart_type == "Trend Line":
                fig = px.line(filtered_df, x=x_axis, y=y_axis, title=f"Trend Line: {y_axis} over {x_axis}")
                st.plotly_chart(fig, use_container_width=True)

        # Moving Average
        st.subheader("📈 Moving Average / Growth Rate")
        if st.button("Calculate Moving Average"):
            filtered_df["Moving_Avg"] = filtered_df[y_axis].rolling(window=3).mean()
            fig = px.line(filtered_df, x=x_axis, y="Moving_Avg", title=f"3-Point Moving Average: {y_axis}")
            st.plotly_chart(fig, use_container_width=True)

        if st.button("Calculate Growth Rate"):
            filtered_df["Growth_Rate_%"] = filtered_df[y_axis].pct_change().mul(100)
            fig = px.line(filtered_df, x=x_axis, y="Growth_Rate_%", title=f"Growth Rate (%): {y_axis}")
            st.plotly_chart(fig, use_container_width=True)

else:
    st.info("⬆️ Please upload Excel files to get started.")

