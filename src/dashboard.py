import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#  PAGE SETTINGS 
st.set_page_config(page_title="Student Dashboard", layout="centered")

st.title("Student Performance Dashboard")

# LOAD DATA 
@st.cache_data
def load_data():
    return pd.read_csv("output/cleaned_student_data.csv")

df = load_data()

# SHOW DATA
st.subheader("Dataset Preview")
st.dataframe(df.head())

#  BASIC STATS 
st.subheader(" Key Metrics")

avg_marks = df['marks'].mean()
avg_attendance = df['attendance'].mean()

col1, col2 = st.columns(2)

col1.metric("Average Marks", f"{avg_marks:.2f}")
col2.metric("Average Attendance", f"{avg_attendance:.2f}")

#  GRAPH 1: Marks 
st.subheader(" Average Marks")

fig1, ax1 = plt.subplots()
ax1.bar(['Marks'], [avg_marks])
ax1.set_ylabel("Marks")

st.pyplot(fig1)

# GRAPH 2: Attendance 
st.subheader("Average Attendance")

fig2, ax2 = plt.subplots()
ax2.bar(['Attendance'], [avg_attendance])
ax2.set_ylabel("Attendance")

st.pyplot(fig2)

#  GRAPH 3: Study vs Marks 
st.subheader(" Study Hours vs Marks")

sorted_df = df.sort_values(by='studyhours')

fig3, ax3 = plt.subplots()
ax3.plot(sorted_df['studyhours'], sorted_df['marks'])
ax3.set_xlabel("Study Hours")
ax3.set_ylabel("Marks")

st.pyplot(fig3)

st.success("Dashboard Loaded Successfully!")