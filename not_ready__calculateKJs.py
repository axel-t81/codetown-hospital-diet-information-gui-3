### What's your thinking here with this puzzle?
# Must pass in standardised diets
# Return the Kilojoules for each diet
# Append/Overwrite the returned kJs into the Dictionaries
# 
# https://www.geeksforgeeks.org/python-passing-dictionary-as-keyword-arguments/
# https://www.reddit.com/r/Python/comments/jp0x4d/taking_a_dictionary_as_an_argument_is_the_root_of/ 




# Calculate Kjs for each diet, that will be displayed
def calc_kjs()
       
kilojoules_unrounded = (4.18 * (4 * protein + 4 * carbs + 9.30 * fat))
# Using the round() function to handle complex float; 
# Setting precision to 4 to not lose data within calculations, even though the output is later formatted to 2 decinal places
kilojoules = round(kilojoules_unrounded, 4)
all_kjs.append(kilojoules)