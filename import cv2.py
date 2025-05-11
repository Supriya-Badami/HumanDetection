import cv2
import imutils
import winsound  
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  


def start_detection():
   
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():  
        messagebox.showerror("Camera Error", "Could not open camera. Please check your camera settings.")
        return

    while True:
        ret, frame = cap.read()
        if not ret: 
            messagebox.showerror("Camera Error", "Failed to capture video.")
            break
        
        frame = imutils.resize(frame, width=650)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

       
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        face_count = 0

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_count += 1 

        
        if face_count > 0:
            winsound.Beep(1000, 200)  

        cv2.putText(frame, "Total humans detected = " + str(face_count), (10, 425), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

        
        key = cv2.waitKey(1)
        if key != -1:  
            break

    
    cv2.destroyAllWindows()
    cap.release()
    login_window.deiconify()  


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "Supriya" and password == "pass":  
        show_success_window(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def show_success_window(username):
    
    success_window = tk.Toplevel()
    success_window.title("Login Successful")
    success_window.geometry("400x400")  

   
    success_bg_image = Image.open(r"C:\Project\humanDetect\4.jpg") 
    success_bg_image = success_bg_image.resize((900, 600), Image.Resampling.LANCZOS)  
    success_bg_photo = ImageTk.PhotoImage(success_bg_image)

   
    success_bg_label = tk.Label(success_window, image=success_bg_photo)
    success_bg_label.image = success_bg_photo  
    success_bg_label.place(x=0, y=0, relwidth=1, relheight=1)  

   
    success_label = tk.Label(success_window, text=f"Welcome, {username}!", font=("Arial", 30), bg='#DDA0DD')
    success_label.pack(expand=True)

    # Add your name and registration number
    name_label = tk.Label(success_window, text="Name: Supriya Badami", font=("Arial", 20), bg='#FFA07A')
    name_label.pack(pady=(20, 5))  # Reduced gap before name

    reg_num_label = tk.Label(success_window, text="Reg No: [P15ZZ22S126017]", font=("Arial", 20), bg='#FFA07A')
    reg_num_label.pack(pady=(0, 40))  # Reduced gap before OK button

    # Create an OK button to start detection and close the success window
    ok_button = tk.Button(success_window, text="OK", font=("Arial", 20), command=lambda: [success_window.destroy(), login_window.withdraw(), start_detection()])
    ok_button.pack(pady=20)

# Function to exit the application
def exit_application():
    login_window.destroy()  # Close the Tkinter window

# Create the Tkinter window
login_window = tk.Tk()
login_window.title("Sign-In Page")
login_window.geometry("600x500")  # Increased window size

# Load and set background image
bg_image = Image.open(r"C:\Project\humanDetect\3.jpg")  # Replace with your image path
bg_image = bg_image.resize((1600, 1500), Image.Resampling.LANCZOS)  # Resize the image to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(login_window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configure the grid to allow centering
login_window.grid_columnconfigure(0, weight=1)
login_window.grid_columnconfigure(1, weight=1)

# Add a heading for the university and center it
university_heading = tk.Label(login_window, text="RANI CHANNAMMA UNIVERSITY,BELAGAVI", font=("Algerian", 45), bg='#900C3F')
university_heading.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Add a heading and center it
project_heading = tk.Label(login_window, text="Welcome to My Project:- NIGHT VISION MOTION DETECTION", font=("Algerian", 35), bg='#FFC300')
project_heading.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Create and place username and password labels and entry widgets
tk.Label(login_window, text="Username:", font=("Algerian", 30), bg='#FF00FF').grid(row=2, column=0, padx=10, pady=(10, 5), sticky="e")
entry_username = tk.Entry(login_window, font=("Arial", 30))
entry_username.grid(row=2, column=1, padx=20, pady=5)

tk.Label(login_window, text="Password:", font=("Algerian", 30), bg='#FF00FF').grid(row=3, column=0, padx=10, pady=(10, 5), sticky="e")
entry_password = tk.Entry(login_window, show="*", font=("Arial", 30))
entry_password.grid(row=3, column=1, padx=20, pady=5)

# Create and place the login button
login_button = tk.Button(login_window, text="Login", font=("Arial", 30), bg='#00FFFF', command=login)
login_button.grid(row=4, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

# Create and place the exit button
exit_button = tk.Button(login_window, text="Exit", font=("Arial", 30), bg='#FF0000', command=exit_application)
exit_button.grid(row=5, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

# Run the Tkinter main loop
login_window.mainloop()
