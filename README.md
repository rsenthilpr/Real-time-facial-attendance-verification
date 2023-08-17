# Face-recognition-for-taking-attendance


Problem Statement: Managing attendance in colleges and organizations has proven to be a time-consuming task. Additionally, there exists a risk of fake attendance and proxy attendance in educational institutions. To overcome these challenges, enhance accuracy, and automate the process without human intervention, we propose a solution that utilizes computer vision technology.

Libraries Used: We utilize open-source libraries for implementing computer vision in this project. Specifically, we employ the following libraries:

        •	OpenCV: An open-source computer vision library in Python.
        
        •	PIL (Python Imaging Library): For image processing tasks.
        
        •	pyttsx: For generating audio output of the attendance status.

Process Flow: The proposed solution eliminates the need for teachers to manually take attendance. Instead, the entire process occurs in the background. The attendance results are announced via voice output at regular intervals. Furthermore, the attendance data is automatically updated in the database.

LBPF Face Recognizer: The project utilizes a Local Binary Pattern (LBP) face recognizer. This method involves comparing the pixel values of neighboring regions in images. The images are converted into numpy arrays of pixel values, which are then transformed into histograms for analysis.

To Run the Program:
1.	Create the following folders: "Classifiers," "trainer," and "dataSet."
2.	Execute the following scripts in sequence:
   
        •	dataSet.py: This script collects and prepares the training dataset.
        
        •	train.py: Trains the LBPF face recognizer using the dataset.
        
        •	detect.py: Uses the trained model to detect and recognize faces for attendance.

By following these steps, the automated attendance system using computer vision will be up and running.
Please ensure that you have the required libraries installed and the necessary dataset available before running the program.
