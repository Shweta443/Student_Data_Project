import sys  #used to interact with pythonsystem(likes path)
import os  #used to work with file paths and folder

# Fix module path issue
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  #Gets the current file location  #Adds it to the python path

from src.load_data import load_data #read dataset
from src.clean_data import clean_data #cleandataset
from src.analysis import analyze_data  # Perform analysis
from src.save_output import save_output # save result

def main(): #MAin workflow of the project #All steps will run inside this
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #Finds location of your project folder

    data_path = os.path.join(BASE_DIR, "data", "student_dataset_v2.csv") #Creates full path to dataset

    print(" File path:", data_path)  #shows file location

    if not os.path.exists(data_path):
        print(" File not found!")
        return  #checks if file is present or not

    df = load_data(data_path)
    print(" Loaded")  #Read CSV file into Dataframe

    df = clean_data(df)
    print("Cleaned")  #Calls your cleaning function  #Remove errors,missing values,etc.

    result = analyze_data(df,"output")
    print(" Analyzed") #performs analysis  Output->folder name for saving visuals

    save_output(df, result, BASE_DIR)
    print(" Saved in output folder")  ##Saves:-- clean datset, Analysis results --- inside output folder

if __name__ == "__main__":
    main()  #ensures main() runs only when file is executed  (Not when importedd)
