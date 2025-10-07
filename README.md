
🕒 Digital Clock (Tkinter)

A simple Digital Clock GUI application built using Python’s Tkinter library.
It displays the current time (hours, minutes, seconds, and AM/PM format) along with the current date.
The clock updates automatically every second.

📸 Features

🕓 Displays current time in HH:MM:SS AM/PM format

📅 Shows the current date below the time

🔁 Auto-refreshes every second

🎨 Beautiful and clean GUI using Tkinter

🧩 Lightweight and beginner-friendly

🧠 How It Works

The strftime() function from the time module is used to fetch the current system time and date.

The after(1000, time) method in Tkinter updates the label every 1000 milliseconds (1 second) to refresh the display.

The Label widget displays the formatted time and date in a styled font and color.

💻 Technologies Used

Python 3.x

Tkinter (for GUI)

time module (for fetching system time)
