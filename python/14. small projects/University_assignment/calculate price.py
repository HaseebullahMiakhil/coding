def calculate_price(item_a, item_b, item_c, purchase):
    price_item_a = item_a
    price_item_b = item_b
    price_item_c = item_c
    
    if purchase == "a":
        total_price = price_item_a
    elif purchase == "b":
        total_price = price_item_b
    elif purchase == "c":
        total_price = price_item_c
    elif purchase == "combo":
        total_price = (price_item_a + price_item_b) * 0.90  
    elif purchase == "gift":
        total_price = (price_item_a + price_item_b + price_item_c) * 0.75 
    else:
        return "Invalid purchase type"

    return f"The total price for your purchase is: ${total_price:.2f}"


item_a = 20.00  
item_b = 30.00 
item_c = 25.00  

# Sample outputs
print(calculate_price(item_a, item_b, item_c, "a"))      # Purchase of Item A
print(calculate_price(item_a, item_b, item_c, "combo"))  # Purchase of Item A and B combo
print(calculate_price(item_a, item_b, item_c, "gift"))   # Purchase of all items (gift pack)