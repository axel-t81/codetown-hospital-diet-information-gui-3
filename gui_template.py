#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

def nutrition():
     pass

# Calculate Kjs for each diet, that will be displayed
def calc_kjs(pr, ca, fa):
    kilojoules_unrounded = (4.18 * (4 * pr + 4 * ca + 9.30 * fa))
    # Using the round() function to handle complex float; 
    # Setting precision to 4 to not lose data within calculations, even though the output is later formatted to 2 decinal places
    kilojoules_var = round(kilojoules_unrounded, 2)
    return kilojoules_var


normal_diet = {
    "protein": 32.5,
    "carbohydrates": 60.0,
    "fat": 40.86
}



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
selected_diet_label = ttk.Label(frame, text = "Selected Diet:", anchor = "e")
protein_label = ttk.Label(frame, text = "Protein (g):", anchor = "e")
carbohydrates_label = ttk.Label(frame, text = "Cabohydrates (g):", anchor = "e")
fat_label = ttk.Label(frame, text = "Fat (g):", anchor = "e")
kilojoules_label = ttk.Label(frame, text = "Kilojoules (kJs):", anchor = "e")

select_diet_label = ttk.Label(frame, text = "Select Below the Diet Option to Display:", anchor = "center")
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

# Create the DoubleVars
protein = DoubleVar(frame)
carbohydrates = DoubleVar(frame)
fat = DoubleVar(frame)
kilojoules = DoubleVar(frame)
# Set the DoubleVars
kilojoules.set(f'{calc_kjs(normal_diet["protein"], normal_diet["carbohydrates"], normal_diet["fat"]):.2f}')
protein.set(f'{normal_diet["protein"]:.2f}')
carbohydrates.set(f'{normal_diet["carbohydrates"]:.2f}')
fat.set(f'{normal_diet["fat"]:.2f}')
# Create the labels for the DoubleVars
selected_diet_label_var = ttk.Label(frame, anchor = "e")
protein_label_var = ttk.Label(frame, width = 12, textvariable = protein, anchor = "e")
carbohydrates_label_var = ttk.Label(frame, width = 12, textvariable = carbohydrates, anchor = "e")
fat_label_var = ttk.Label(frame, width = 12, textvariable = fat, anchor = "e")
kilojoules_label_var = ttk.Label(frame, width = 12, textvariable = kilojoules, anchor = "e")
# Display the label for the DoubleVars
selected_diet_label_var.grid(column = 4, row = 2, sticky = (N, S, E, W))
protein_label_var.grid(column = 4, row = 3, sticky = (N, S, E, W))
carbohydrates_label_var.grid(column = 4, row = 4, sticky = (N, S, E, W))
fat_label_var.grid(column = 4, row = 5, sticky = (N, S, E, W))
kilojoules_label_var.grid(column = 4, row = 6, sticky = (N, S, E, W))



for child in frame.winfo_children():			
	child.grid_configure(padx = 3, pady = 3)


root.mainloop()