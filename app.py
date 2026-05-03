import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.set_page_config(page_title="Expense Tracker", page_icon="💰")
st.title("💰 Personal Expense Tracker")
st.markdown("Track and visualise your daily expenses!")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.subheader("Add New Expense")
col1, col2, col3, col4 = st.columns(4)
with col1: desc = st.text_input("Description")
with col2: amount = st.number_input("Amount (SGD)", min_value=0.0, step=0.50)
with col3: category = st.selectbox("Category", ["Food","Transport","Shopping","Entertainment","Bills","Health","Other"])
with col4: exp_date = st.date_input("Date", value=date.today())

if st.button("Add Expense") and desc and amount > 0:
    st.session_state.expenses.append({"Description": desc, "Amount": amount, "Category": category, "Date": str(exp_date)})
    st.success(f"Added: {desc} — SGD {amount:.2f}")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader(f"Total Spent: SGD {df['Amount'].sum():.2f}")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.pie(df, names='Category', values='Amount', title='Spending by Category')
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.bar(df, x='Description', y='Amount', color='Category', title='Expenses Breakdown')
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("All Expenses")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No expenses added yet. Add your first expense above!")
