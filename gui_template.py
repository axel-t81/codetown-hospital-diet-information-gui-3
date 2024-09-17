#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

def nutrition():
     pass

root = Tk()

root.title("Codetown Hospital: Diet Information")

frame = ttk.Frame(root, padding = "3 3 12 12", borderwidth = 5, relief = "sunken")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame.grid(column = 0, row = 0, sticky = (N, W, E, S))

for i in range(1, 10):
    frame.rowconfigure(i, weight=1)

for i in range(1, 6):
    frame.columnconfigure(i, weight=1)
       

# Create the labels
selected_diet_label = ttk.Label(frame, text = "Selected Diet:")
protein_label = ttk.Label(frame, text = "Protein (g):")
carbohydrates_label = ttk.Label(frame, text = "Cabohydrates (g):")
fat_label = ttk.Label(frame, text = "Fat (g):")
kilojoules_label = ttk.Label(frame, text = "Kilojoules (kJs):")

select_diet_label = ttk.Label(frame, text = "Select Below the Diet Option to Display:")
# Display the label
selected_diet_label.grid(column = 2, row = 2, sticky = (N, S, E, W))
protein_label.grid(column = 2, row = 3, sticky = (N, S, E, W))
carbohydrates_label.grid(column = 2, row = 4, sticky = (N, S, E, W))
fat_label.grid(column = 2, row = 5, sticky = (N, S, E, W))
kilojoules_label.grid(column = 2, row = 6, sticky = (N, S, E, W))
select_diet_label.grid(column = 2, row = 8, columnspan = 3, sticky = ((N, S, E, W)))


# Create Buttons
normal_button = ttk.Button(frame, width = 8, text = "Normal", command = nutrition)
oncology_button = ttk.Button(frame, width = 8, text = "Oncology", command = nutrition)	
cardiology_button = ttk.Button(frame, width = 8, text = "Cardiology", command = nutrition)	
diabetes_button = ttk.Button(frame, width = 8, text = "Diabetes", command = nutrition)	
kidney_button = ttk.Button(frame, width = 8, text = "Kidney", command = nutrition)		
# Display Buttons
normal_button.grid(column = 1, row = 9, sticky = (N, S, E, W))
oncology_button.grid(column = 2, row = 9, sticky = (N, S, E, W))
cardiology_button.grid(column = 3, row = 9, sticky = (N, S, E, W))
diabetes_button.grid(column = 4, row = 9, sticky = (N, S, E, W))
kidney_button.grid(column = 5, row = 9, sticky = (N, S, E, W))

for child in frame.winfo_children():			
	child.grid_configure(padx = 3, pady = 3)


root.mainloop()