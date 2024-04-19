#TASK 1
#---All updates incorporated

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu['Beverages'] = {'Coke': 1.99, 'Horchata': 2.99}  #adds 'Beverages' to the menu
restaurant_menu["Main Course"]['Steak'] = 17.99   #strings together keys in otder to tap into the nested value of 'Steak'
restaurant_menu['Starters'] = {'Soup': 5.99}    #since keys cant be doubled in dictionaries, rewriting 'Starters' works

print(restaurant_menu)


    
        


