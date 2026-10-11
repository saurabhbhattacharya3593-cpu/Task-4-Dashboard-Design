# Task 4 — Sales & Financial Dashboard Design

## Objective
Build an interactive dashboard for business stakeholders, covering sales, profit, growth/trends, filters, summary cards, a consistent theme, and a data preview.

## What is included
- `app.py` — interactive Streamlit dashboard with date, region, and category filters.
- `data/sales_financial_sample.csv` — sample data to run the project immediately.
- `Task4_Dashboard_Summary.pptx` — short presentation summarizing the dashboard, KPIs, visuals, and business recommendations.
- `screenshots/dashboard_preview.png` — static preview of the dashboard design.
- `requirements.txt` — Python packages required.

## Important dataset note
The included CSV is **generated sample data for demonstration**, not a downloaded Kaggle dataset. The task sheet asks for a Sales/Financial dataset from Kaggle. To fully match that requirement, replace this CSV with a properly licensed Kaggle dataset and adjust the column names in `app.py` if needed. A public Sample Superstore dataset is one possible starting point:
https://github.com/Technology-Hatchery/Rcode/blob/master/Data/Sample%20-%20Superstore%20Sales%20%28Excel%29.csv

## Run the dashboard (free)
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`
5. Your browser opens the dashboard. Use the left sidebar to filter by date, region, and category.

## Dashboard features
- KPI cards: Total Sales, Total Profit, Orders, Profit Margin
- Monthly sales and profit trend
- Sales and profit by region
- Sales by category
- Top products by sales
- Monthly sales mix by category
- Interactive filters and filtered CSV download

## Business questions this dashboard helps answer
- How much sales and profit did the business generate?
- How does performance change over time?
- Which region and category contribute the most sales?
- Which products have the highest sales?
- How do results change when date, region, or category filters are applied?

## GitHub upload
Create a new **Public** repository named `Task-4-Dashboard-Design`, then upload all files and folders from this project. Do not upload only the ZIP if your reviewer expects to see the project files directly in the repository. The ZIP is a convenient backup/transfer package.

## Interview questions — short answers
1. **Key elements of a dashboard:** KPIs, charts, filters/slicers, clear layout, labels, and consistent colors.
2. **What is a KPI?** A Key Performance Indicator is a measurable value used to track progress toward a business goal.
3. **What are slicers in Power BI?** Visual filters that let users interactively filter report data.
4. **Power BI vs Tableau:** Both are BI tools. Power BI integrates closely with Microsoft products and is often cost-effective; Tableau is known for flexible visual exploration. Choice depends on needs, skills, licensing, and data environment.
5. **How to make a dashboard interactive?** Add slicers/filters, cross-filtering, drill-down, tooltips, and navigation.
6. **How to deal with large datasets?** Clean data, remove unnecessary columns, aggregate where suitable, use efficient data models, query folding/incremental refresh where available, and optimize visuals.
7. **Charts for trend analysis:** Line charts are common for trends over time; area charts can show contribution/mix; bar charts compare categories.

## Limitations
This is a working interactive dashboard built with Streamlit as a free alternative to Power BI/Tableau. It is not a `.pbix` or Tableau workbook file.
