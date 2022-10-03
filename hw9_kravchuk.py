def cats_with_hat_function (cats: int) -> list:
    #binary: 0 - wo hat, 1 - with hat
    circle_with_cats = list(0 for i in range(cats+1))
    number_of_cat_with_hat = []

    # plus 1 extra cat - to skip the zero index
    for iteration in range(1, cats+1):
        for cat in range(1, cats+1):
            if cat % iteration == 0:
                if circle_with_cats[cat] == 0:
                    circle_with_cats[cat] = 1
                elif circle_with_cats[cat] == 1:
                    circle_with_cats[cat] = 0                  
    
    for cat in range(1, cats+1):
        if circle_with_cats[cat] == 1:
            number_of_cat_with_hat.append(cat)
    
    return number_of_cat_with_hat

print(cats_with_hat_function(100))          