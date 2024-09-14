#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

def nutrition():
     pass

root = Tk()
# root.geometry("650x250+400+300")

root.title("Codetown Hospital: Diet Information")

frame = ttk.Frame(root, padding = "3 3 12 12")

frame.grid(column = 0, row = 0, sticky = (N, W, E, S))

rows = 8
columns = 10

#for i in range(rows):
#    root.rowconfigure(index=i,weight=1)

#for i in range(columns):
#    root.columnconfigure(index=i, weight=1)

Grid.grid_configure(Grid, 9, weight = 1)
Grid.grid_configure(Grid, 3, weight = 1)


# Blank cell create
#blank_cell = ttk.Label(frame, text = "")
#blank_cell.grid(column = 1, row = 1, sticky = (N, S, E, W))
#blank_cell.grid(column = 1, row = 2, sticky = (N, S, E, W))
#blank_cell.grid(column = 1, row = 3, sticky = (N, S, E, W))
#blank_cell.grid(column = 1, row = 4, sticky = (N, S, E, W))
#blank_cell.grid(column = 1, row = 5, sticky = (N, S, E, W))
#blank_cell.grid(column = 1, row = 6, sticky = (N, S, E, W))
#blank_cell.grid(column = 1, row = 7, sticky = (N, S, E, W))

# Create the labels
selected_diet_label = ttk.Label(frame, text = "Selected Diet:")
protein_label = ttk.Label(frame, text = "Protein (g):")
carbohydrates_label = ttk.Label(frame, text = "Cabohydrates (g):")
fat_label = ttk.Label(frame, text = "Fat (g):")
kilojoules_label = ttk.Label(frame, text = "Kilojoules (kJs):")

select_diet_label = ttk.Label(frame, text = "Select Below the Diet Option to Display:")
# Display the label
selected_diet_label.grid(column = 2, row = 2, sticky = E)
protein_label.grid(column = 2, row = 3, sticky = E)
carbohydrates_label.grid(column = 2, row = 4, sticky = E)
fat_label.grid(column = 2, row = 5, sticky = E)
kilojoules_label.grid(column = 2, row = 6, sticky = E)
select_diet_label.grid(column = 2, row = 8, columnspan = 3, sticky = (N, S))

# Create blank label
blank_label1 = ttk.Label(frame, text = "")
blank_label2 = ttk.Label(frame, text = "")
# Display blank labels
blank_label1.grid(column = 2, row = 1, columnspan = 3, sticky = (N, S))
blank_label2.grid(column = 2, row = 7, columnspan = 3, sticky = (N, S))

# Create Buttons
normal_button = ttk.Button(frame, width = 8, text = "Normal", command = nutrition)
oncology_button = ttk.Button(frame, width = 8, text = "Oncology", command = nutrition)	
cardiology_button = ttk.Button(frame, width = 8, text = "Cardiology", command = nutrition)	
diabetes_button = ttk.Button(frame, width = 8, text = "Diabetes", command = nutrition)	
kidney_button = ttk.Button(frame, width = 8, text = "Kidney", command = nutrition)		
# Display Buttons
normal_button.grid(column = 1, row = 9, sticky = (E, W))
oncology_button.grid(column = 2, row = 9, sticky = (E, W))
cardiology_button.grid(column = 3, row = 9, sticky = (E, W))
diabetes_button.grid(column = 4, row = 9, sticky = (E, W))
kidney_button.grid(column = 5, row = 9, sticky = (E, W))

for child in frame.winfo_children():			
	child.grid_configure(padx = 3, pady = 3)

#for c in sorted(root.children):
#    root.children[c].pack()

root.mainloop()