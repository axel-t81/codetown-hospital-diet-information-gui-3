#!/usr/bin/env python3
"""
This module takes allows users to select one of the standardised diets.
When that diet is selected, the amount of protein, carbohydrates, fat, and kilojoules is displayed.
All of this is done with a GUI.
"""
# Program Details
__author__ = "Axel Tracy"
__version__ = "0.1.1"

from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Codetown Hospital: Diet Information")

frame = ttk.Frame(root, padding = "3 3 12 12", borderwidth = 5, relief = FLAT)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#frame.grid(column = 0, row = 0, sticky = (N, W, E, S))
frame.grid(sticky=(N,S,E,W))

for i in range(1, 10):
    frame.rowconfigure(i, weight=1)

for i in range(1, 6):
    frame.columnconfigure(i, weight=1)



normal_button = ttk.Button(frame, width = 8, text = "Normal")

normal_button.configure()