import os

def save_output(df, result, base_dir):
    output_folder = os.path.join(base_dir, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Save cleaned data
    df.to_csv(os.path.join(output_folder, "cleaned_data.csv"), index=False)

    # Save results
    with open(os.path.join(output_folder, "analysis.txt"), "w") as f:
        for key, value in result.items():
            f.write(f"{key}: {value}\n")

    print(" Output saved successfully")