def clean_data(df):  #creating a function 
    # Step 1: Clean column names (universal fix)
    df.columns = (
        df.columns
        .str.strip()          # remove extra spaces
        .str.lower()          # lowercase
        .str.replace(" ", "_")  # spaces → underscore
    )  # GEts all column names from the dataset

    print("Cleaned Columns:", df.columns.tolist()) #Displays cleaned column names in terminal   #.tolist() converts column object to list

    # 🔹 Step 2: Handle Study Hours safely
    if 'study_hours' in df.columns:
        df['study_hours'] = df['study_hours'].clip(lower=0)  #Checks if column exists(safe coding practice)
    else:#.clip() it removes negative values
        print(" 'study_hours' column not found")

    # 🔹 Step 3: Fill missing values (optional but good practice)
    df = df.fillna(0)  #Replace all missing values with 0  (Prevent error during calculations)

    # 🔹 Step 4: Remove duplicates
    df = df.drop_duplicates()  #Removes repeated rows

    return df