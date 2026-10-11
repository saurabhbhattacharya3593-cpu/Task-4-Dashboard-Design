import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Sales & Financial Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales & Financial Performance Dashboard")
st.caption("Task 4 — Dashboard Design | Interactive business overview")

DATA_PATH = Path(__file__).parent / "data" / "sales_financial_sample.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["Order Date"])

with st.sidebar:
    st.header("Dashboard Filters")
    min_date, max_date = df["Order Date"].min().date(), df["Order Date"].max().date()
    date_range = st.date_input("Order date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    regions = st.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
    categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    st.markdown("---")
    st.caption("Use the filters to explore different parts of the business.")

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
else:
    start_date, end_date = df["Order Date"].min(), df["Order Date"].max()

f = df[
    df["Order Date"].between(start_date, end_date)
    & df["Region"].isin(regions)
    & df["Category"].isin(categories)
].copy()

if f.empty:
    st.warning("No records match these filters. Please change the filters.")
    st.stop()

total_sales = f["Sales"].sum()
total_profit = f["Profit"].sum()
orders = f["Order ID"].nunique()
profit_margin = (total_profit / total_sales * 100) if total_sales else 0

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Sales", f"${total_sales:,.0f}")
c2.metric("Total Profit", f"${total_profit:,.0f}")
c3.metric("Orders", f"{orders:,}")
c4.metric("Profit Margin", f"{profit_margin:.1f}%")

st.markdown("### Sales trend over time")
monthly = f.set_index("Order Date").resample("MS").agg(Sales=("Sales","sum"), Profit=("Profit","sum")).reset_index()
trend = px.line(monthly, x="Order Date", y=["Sales","Profit"], markers=True,
                title="Monthly Sales and Profit", template="plotly_white",
                color_discrete_sequence=["#4F46E5","#16A34A"])
st.plotly_chart(trend, use_container_width=True)

left,right = st.columns(2)
with left:
    region_perf = f.groupby("Region", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
    fig_region = px.bar(region_perf, x="Region", y=["Sales","Profit"], barmode="group",
                        title="Sales and Profit by Region", template="plotly_white",
                        color_discrete_sequence=["#4F46E5","#16A34A"])
    st.plotly_chart(fig_region, use_container_width=True)
with right:
    cat_perf = f.groupby("Category", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
    fig_cat = px.bar(cat_perf, x="Category", y="Sales", title="Sales by Category",
                     template="plotly_white", color="Category")
    st.plotly_chart(fig_cat, use_container_width=True)

left2,right2 = st.columns(2)
with left2:
    product_perf = f.groupby("Product", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum")).sort_values("Sales", ascending=False).head(8)
    fig_prod = px.bar(product_perf.sort_values("Sales"), x="Sales", y="Product", orientation="h",
                      title="Top Products by Sales", template="plotly_white", color="Sales")
    st.plotly_chart(fig_prod, use_container_width=True)
with right2:
    f["Month"] = f["Order Date"].dt.to_period("M").astype(str)
    monthly_cat = f.groupby(["Month","Category"], as_index=False)["Sales"].sum()
    fig_stack = px.area(monthly_cat, x="Month", y="Sales", color="Category",
                        title="Monthly Sales Mix by Category", template="plotly_white")
    st.plotly_chart(fig_stack, use_container_width=True)

st.markdown("### Data preview")
st.dataframe(f.sort_values("Order Date", ascending=False), use_container_width=True, hide_index=True)
st.download_button("⬇️ Download filtered data (CSV)", f.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_sales_data.csv", mime="text/csv")
st.caption("Dataset note: this repository includes a generated sample dataset for demonstration. Replace it with a properly licensed Kaggle Sales/Financial dataset for a real-world submission.")
