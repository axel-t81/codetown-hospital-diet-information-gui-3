def set_vars(diet_choice):

    # Create the DoubleVars
    protein = DoubleVar(frame)
    carbohydrates = DoubleVar(frame)
    fat = DoubleVar(frame)
    kilojoules = DoubleVar(frame)

    # Set the DoubleVars
    kilojoules.set(f'{calc_kjs(diet_choice["protein"], diet_choice["carbohydrates"], diet_choice["fat"]):.2f}')
    protein.set(f'{diet_choice["protein"]:.2f}')
    carbohydrates.set(f'{diet_choice["carbohydrates"]:.2f}')
    fat.set(f'{diet_choice["fat"]:.2f}')

    return protein, carbohydrates, fat, kilojoules