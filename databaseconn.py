
import tkinter as tk
import pyodbc

# Create the form
form = tk.Tk()

# Create the widgets
label = tk.Label(form, text="Enter your name:")
entry = tk.Entry(form)
button = tk.Button(form, text="Submit", command=lambda: submit(entry.get()))

# Add the widgets to the form
label.pack()
entry.pack()
button.pack()

# Connect to the database
conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\User\\Documents\\example.accdb;')

def submit(name):
    # Insert the name into the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO names (name) VALUES (?)", (name,))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Destroy the form
    form.destroy()

# Show the form
form.mainloop()
