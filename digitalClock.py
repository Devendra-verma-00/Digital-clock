import tkinter as tk
from time import strftime 

# Create the main window
root = tk.Tk()
root.title("Digital Clock !")

# Function to update time
def time():
    string = strftime('%H:%M:%S %p\n %D')  # Format time and date
    label.config(text=string)
    label.after(1000, time)  # Update every 1 second

# Label design
label = tk.Label(root, font=('calibri', 50, 'bold'),
                 background='Yellow', foreground='black')
label.pack(anchor='center')

# Start the clock
time() 
root.mainloop()
