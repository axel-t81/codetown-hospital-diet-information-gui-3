#!/usr/bin/env python3
"""
This module takes allows users to select one of the standardised diets.
When that diet is selected, the amount of protein, carbohydrates, fat, and kilojoules is displayed.
All of this is done with a GUI.
"""
# Program Details
__author__ = "Axel Tracy"
__version__ = "0.1.1"


# Initialise Dictionaries with Standardised Diets plus Kilojoules
normal_diet = {
    "protein": 32.5,
    "carbohydrates": 60.0,
    "fat": 40.86
}
oncology_diet = {
    "protein": 35.0,
    "carbohydrates": 52.5,
    "fat": 37.63
}
cardiology_diet = {
    "protein": 32.5,
    "carbohydrates": 30.0,
    "fat": 26.88
}
diabetes_diet = {
    "protein": 20.0,
    "carbohydrates": 27.5,
    "fat": 27.95
}
kidney_diet = {
    "protein": 15.0,
    "carbohydrates": 55.0,
    "fat": 23.65
}