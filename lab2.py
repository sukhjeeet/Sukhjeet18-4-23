shoppingCart = {}

while True:
    print("\nWELCOME TO THE AMANDO SHOPPING SITE\n")
    print("A. Add product to the cart.")
    print("B. Search the product.")
    print("C. Delete the product from the cart.")
    print("D. Quit.")
    
    choice = input("Enter your choice: ").upper()
    
    if choice == 'A':
        if len(shoppingCart) < 5:
            product = input("Enter product name: ")
            brand = input("Enter brand name: ")
            shoppingCart[product] = brand
            print("Product added to the cart successfully.")
        else:
            print("Cart is full.")
    
    elif choice == 'B':
        product = input("Enter product name to search: ")
        if product in shoppingCart:
            print(f"{product} is found in the cart. Brand name: {shoppingCart[product]}")
        else:
            print("No product exists with this name.")
    
    elif choice == 'C':
        product = input("Enter product name to delete: ")
        if product in shoppingCart:
            del shoppingCart[product]
            print(f"{product} is deleted from the cart successfully.")
        else:
            print("No product exists with this name.")
        
        if len(shoppingCart) == 0:
            print("Cart is empty, no item is found.")
    
    elif choice == 'D':
        print("Thank you for shopping with us.")
        break
    
    else:
        print("Invalid choice. Please enter a valid choice.")
