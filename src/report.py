import pandas as pd

def generate_report(df, output_folder):

    report = pd.DataFrame({
        "Metric": [
            "Total Students",
            "Passed Students",
            "Failed Students",
            "Highest Marks",
            "Lowest Marks",
            "Average Marks",
            "Average Attendance"
        ],
        "Value": [
            len(df),
            (df['Result'] == "Pass").sum(),
            (df['Result'] == "Fail").sum(),
            df['Marks'].max(),
            df['Marks'].min(),
            df['Marks'].mean(),
            df['Attendance'].mean()
        ]
    })

    report.to_csv(f"{output_folder}/report.csv", index=False)