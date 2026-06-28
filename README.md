# Student_Data_Project
Project Overview:-

This project analyzes student data and presents insights using data cleaning, visualization, and a simple dashboard.

It is built using Python, Pandas, Matplotlib, and Streamlit.

The dashboard helps in understanding:

Student performance 
Attendance trends 
Study habits vs marks 

Features:-
 Data Cleaning (remove duplicates, handle missing values)
 Basic Data Analysis (average marks & attendance)
 Simple Graphs using Matplotlib
 Interactive Dashboard using Streamlit
 Clean and beginner-friendly UI

Tech Stack:-
Python
Pandas
Matplotlib
Streamlit

Project Structure:-
project/
│── main.py                  # Main pipeline
│── clean_data.py            # Data cleaning
│── analyze_data.py          # Graph generation
│── dashboard.py             # Streamlit dashboard
│── student_dataset_v2.csv   # Input dataset
│
└── output/
    ├── cleaned_student_data.csv
    ├── avg_marks.png
    ├── avg_attendance.png
    └── study_vs_marks.png


    Usage:-
Step 1: Run Data Processing
python main.py
Step 2: Launch Dashboard
streamlit run dashboard.py

Learning Outcomes:-
Data cleaning using Pandas
Data visualization using Matplotlib
Building dashboards using Streamlit
Structuring real-world Python projects