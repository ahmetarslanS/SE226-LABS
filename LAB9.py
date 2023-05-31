import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ahmet",
    database="marvel"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        ID INT,
        MOVIE VARCHAR(255),
        DATE DATE,
        MCU_PHASE VARCHAR(255)
    )
""")

with open("Marvel.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split("\t")
        if len(line) == 4:
            ID = int(line[0].split()[0])
            MOVIE = line[1]
            DATE = line[2]
            MCU_PHASE = line[3]
            cursor.execute("INSERT INTO movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)",
                           (ID, MOVIE, DATE, MCU_PHASE))
    conn.commit()


def add_movie():
    def add_to_database():
        ID = int(id_entry.get())
        MOVIE = movie_entry.get()
        DATE = date_entry.get()
        MCU_PHASE = phase_entry.get()
        cursor.execute("INSERT INTO movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)",
                       (ID, MOVIE, DATE, MCU_PHASE))
        conn.commit()
        messagebox.showinfo("Success", "Movie added successfully!")
        popup.destroy()

    def cancel_add():
        popup.destroy()

    popup = tk.Toplevel(root)
    popup.title("Add Movie")
    popup.geometry("300x200")

    id_label = tk.Label(popup, text="ID:")
    id_label.pack()
    id_entry = tk.Entry(popup)
    id_entry.pack()

    movie_label = tk.Label(popup, text="Movie:")
    movie_label.pack()
    movie_entry = tk.Entry(popup)
    movie_entry.pack()

    date_label = tk.Label(popup, text="Date:")
    date_label.pack()
    date_entry = tk.Entry(popup)
    date_entry.pack()

    phase_label = tk.Label(popup, text="MCU Phase:")
    phase_label.pack()
    phase_entry = tk.Entry(popup)
    phase_entry.pack()

    ok_button = tk.Button(popup, text="Ok", command=add_to_database)
    ok_button.pack(side=tk.LEFT)

    cancel_button = tk.Button(popup, text="Cancel", command=cancel_add)
    cancel_button.pack(side=tk.RIGHT)


def list_all_movies():
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    text_box.delete("1.0", tk.END)
    for row in rows:
        text_box.insert(tk.END, f"ID: {row[0]}, Movie: {row[1]}, Date: {row[2]}, MCU Phase: {row[3]}\n")


root = tk.Tk()
root.title("Marvel Movies")
root.geometry("400x300")

dropdown_label = tk.Label(root, text="Choose ID:")
dropdown_label.pack()
dropdown_var = tk.StringVar(root)

cursor.execute("SELECT ID FROM movies")
ids = [str(row[0]) for row in cursor.fetchall()]

if ids:
    dropdown_var.set(ids[0])
    dropdown = tk.OptionMenu(root, dropdown_var, *ids)
    dropdown.pack()
else:
    dropdown_var.set("No Movies Found")
    dropdown = tk.OptionMenu(root, dropdown_var, "No Movies Found")
    dropdown.configure(state='disabled')
    dropdown.pack()

text_box = tk.Text(root, height=10, width=50)
text_box.pack()

add_button = tk.Button(root, text="Add", command=add_movie)
add_button.pack(side=tk.LEFT)

list_button = tk.Button(root, text="LIST ALL", command=list_all_movies)
list_button.pack(side=tk.RIGHT)

root.mainloop()

text_box = tk.Text(root, height=10, width=50)
text_box.pack()

add_button = tk.Button(root, text="Add", command=add_movie)
add_button.pack(side=tk.LEFT)

list_button = tk.Button(root, text="LIST ALL", command=list_all_movies)
list_button.pack(side=tk.RIGHT)

root.mainloop()
