def transform_data(df):

    def grade(m):
        if m >= 90:
            return "A"
        elif m >= 75:
            return "B"
        elif m >= 60:
            return "C"
        elif m >= 40:
            return "D"
        else:
            return "F"

    df['Grade'] = df['Marks'].apply(grade)
    df['Result'] = df['Marks'].apply(lambda x: "Pass" if x >= 40 else "Fail")

    df['Performance Score'] = (
        df['Marks'] * 0.6 +
        df['Attendance'] * 0.2 +
        df['Study Hours'] * 0.2
    )

    return df