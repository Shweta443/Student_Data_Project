import os  #used to work with folders/files(create folder,save files)
import matplotlib.pyplot as plt #used to create graphs

def analyze_data(df, output_folder):  #where graphs will be saved
    print("\n Analysis Started...")

    os.makedirs(output_folder, exist_ok=True)  #creates folder(like output/)   exist_ok=true :-no error if folder already exist

    # GRAPH 1: Average Marks
    plt.figure() #Starts a new blank graph
    avg_marks = df['marks'].mean() #calculate average of marks column
    plt.bar(['Average Marks'], [avg_marks])  #creates bar chart
    plt.title("Average Marks") #add title
    plt.ylabel("Marks") #y-axis label
    plt.savefig(os.path.join(output_folder, "avg_marks.png")) #Saves graph as image in output folder
    plt.close()  #CLose graph (important to avoid overlap)

    #GRAPH 2: Average Attendance 
    plt.figure()
    avg_att = df['attendance'].mean()  #Calculate average attendance
    plt.bar(['Average Attendance'], [avg_att]) #create bar chart
    plt.title("Average Attendance")
    plt.ylabel("Attendance") #label
    plt.savefig(os.path.join(output_folder, "avg_attendance.png"))
    plt.close()  #Save and close

    #  GRAPH 3: Study vs Marks (Simple Line) 
    sorted_df = df.sort_values(by='studyhours')  #MAkes line graph smooth and easy to read

    plt.figure()  #New graph
    plt.plot(sorted_df['studyhours'], sorted_df['marks'])  #x-axis->Study hours    y-axis->marks  (Shows relationship between study and marks)
    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")  #label and title
    plt.savefig(os.path.join(output_folder, "study_vs_marks.png"))
    plt.close()  #Save and close graph

    print(" Simple graphs saved in output folder")  #COnfirms graphs are created

    return {
        "avg_marks": avg_marks,
        "avg_attendance": avg_att
    }  #function send back results 
        # Returns a dictionary:  average marks average attendance