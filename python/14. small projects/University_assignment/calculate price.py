def calculate_prices():
    # Define the prices of individual items
    price_item_1 = 200.00
    price_item_2 = 400.00
    price_item_3 = 300.00

    # Calculate combo prices with discounts
    combo_1 = price_item_1 + price_item_2
    combo_2 = price_item_1 + price_item_3
    combo_3 = price_item_2 + price_item_3
    combo_gift_pack = price_item_1 + price_item_2 + price_item_3

    # Apply discounts
    combo_1_with_discount = combo_1 * 0.90  # 10% discount
    combo_2_with_discount = combo_2 * 0.90  # 10% discount
    combo_3_with_discount = combo_3 * 0.90  # 10% discount
    gift_pack_with_discount = combo_gift_pack * 0.75  # 25% discount

    # Output the results
    print("Output of Online Store")
    print("-----------------------")
    print(f"Product 1                 ${price_item_1:.2f}")
    print(f"Product 2                 ${price_item_2:.2f}")
    print(f"Product 3                 ${price_item_3:.2f}")
    print(f"Combo 1 (Item 1 + Item 2) ${combo_1_with_discount:.2f}")
    print(f"Combo 2 (Item 1 + Item 3) ${combo_2_with_discount:.2f}")
    print(f"Combo 3 (Item 2 + Item 3) ${combo_3_with_discount:.2f}")
    print(f"Combo 4 (Item 1 + Item 2 + Item 3) ${gift_pack_with_discount:.2f}")
    print("\nFor delivery Contact: 98764678989")

# Call the function to see the output
calculate_prices()