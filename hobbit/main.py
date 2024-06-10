import json
import datetime
import os


def main() -> None:
    # Check if config.json exists
    if not os.path.exists("config.json"):
        print("config.json not found. Please create a config.json file.")
        return
    
    # Check if orders directory exists, create if it doesn't
    if not os.path.exists("orders/"):
        os.makedirs("orders/")

    # Load prices from config.json
    prices = json.load(open("config.json"))
    order = []
    print("Welcome to Hobbit, user!")
    
    while True:
        print()
        print_services()
        print()
        # Prompt user to select a service
        service = get_int_input("Please enter the service you want to order (0-3): ", 0, 3)
        # Handle the service selection
        item = handle_service_selection(service, prices)
        order.append(item)
        print()
        # Ask if the user wants to order another service
        do_another = get_yes_no_input("Would you like to order another service? (y/n): ")

        if not do_another:
            break

    # Finalize the order
    finalize_order(order, prices)


def handle_service_selection(service: int, prices: dict) -> dict:
    # Get the dimensions of the item
    width = get_int_input("Enter the width in inches: ")
    height = get_int_input("Enter the height in inches: ")
    
    # Based on the service type, handle the specific order
    if service == 0:
        return handle_poster_order(width, height, prices)
    elif service == 1:
        return handle_sticker_order(width, height, prices)
    elif service == 2:
        return handle_mousepad_order(width, height, prices)
    elif service == 3:
        return handle_playmat_order(width, height, prices)
    
    raise Exception("Something went wrong")


def handle_poster_order(width: int, height: int, prices: dict) -> dict:
    # Calculate the total price for the poster
    base_price = prices['services']['poster']['base_price']
    size = width * height
    rate = prices['services']['poster']['rate']
    total_price = round(base_price + (size * rate), 2)
    print()
    print(f"You have added a Poster of size {width}x{height} inches. The price is calculated as follows:")
    print(f"Base Price: {base_price}")
    print(f"Size in sq. inches: {size}")
    print(f"Rate per sq. inch: {rate}")
    print(f"Total Price: {base_price} + ({size} * {rate}) = {total_price}")
    
    return {
        "type": "poster",
        "size": f"{width}x{height}",
        "price": total_price
    }


def handle_sticker_order(width: int, height: int, prices: dict) -> dict:
    # Get additional inputs specific to stickers
    quantity = get_int_input("Enter the quantity: ")
    shape, is_custom_shape = get_shape_input()
    waterproof = get_yes_no_input("Would you like waterproof stickers? (y/n): ")
    # Calculate the total price for the stickers
    base_price = prices['services']['sticker']['base_price']
    size = width * height
    rate = prices['services']['sticker']['rate']
    shape_multiplier = prices['services']['sticker']['shapes']['custom'] if is_custom_shape else prices['services']['sticker']['shapes'][shape]
    waterproof_option_cost = prices['services']['sticker']['waterproof'] if waterproof else 0
    total_price = round((base_price + (size * rate)) * quantity * shape_multiplier + waterproof_option_cost, 2)
    print()
    print(f"You have added Stickers of size {width}x{height} inches, quantity {quantity}, shape {shape}{', waterproof' if waterproof else ''}. The price is calculated as follows:")
    print(f"Base Price: {base_price}")
    print(f"Size in sq. inches: {size}")
    print(f"Rate per sq. inch: {rate}")
    print(f"Shape Multiplier ({shape}): {shape_multiplier}")

    if waterproof:
        print(f"Waterproof Option Cost: {prices['services']['sticker']['waterproof']}")

    print(f"Total Price: ({base_price} + ({size} * {rate})) * {quantity} * {shape_multiplier} {f'+ {waterproof_option_cost}' if waterproof else ''} = {total_price}")
    
    return {
        "type": "sticker",
        "size": f"{width}x{height}",
        "quantity": quantity,
        "shape": shape,
        "waterproof": "yes" if waterproof else "no",
        "price": total_price
    }


def handle_mousepad_order(width: int, height: int, prices: dict) -> dict:
    # Get additional inputs specific to mouse pads
    surface = get_surface_input()
    # Calculate the total price for the mouse pad
    base_price = prices['services']['mousepad']['base_price']
    size = width * height
    rate = prices['services']['mousepad']['rate']
    surface_option_cost = prices['services']['mousepad']['surfaces'][surface]
    total_price = round(base_price + (size * rate) + surface_option_cost, 2)
    print()
    print(f"You have added Mouse Pads of size {width}x{height} inches, surface options {surface}. The price is calculated as follows:")
    print(f"Base Price: {base_price}")
    print(f"Size in sq. inches: {size}")
    print(f"Rate per sq. inch: {rate}")
    print(f"Surface Option Cost: {surface_option_cost}")
    print(f"Total Price: {base_price} + ({size} * {rate}) + {surface_option_cost} = {total_price}")
    
    return {
        "type": "mousepad",
        "size": f"{width}x{height}",
        "surface": surface,
        "price": total_price
    }


def handle_playmat_order(width: int, height: int, prices: dict) -> dict:
    # Get additional inputs specific to play mats
    thickness = get_int_input("Enter the thickness in millimeters: ")
    # Calculate the total price for the play mat
    base_price = prices['services']['playmat']['base_price']
    size = width * height
    rate = prices['services']['playmat']['rate']
    thickness_price = thickness * prices['services']['playmat']['thickness_rate']
    total_price = round(base_price + (size * rate) + thickness_price, 2)
    print()
    print(f"You have added Playmats of thickness {thickness} millimeters. The price is calculated as follows:")
    print(f"Base Price: {base_price}")
    print(f"Size in sq. inches: {size}")
    print(f"Rate per sq. inch: {rate}")
    print(f"Thickness Cost: {thickness_price}")
    print(f"Total Price: {base_price} + ({size} * {rate}) + {thickness_price} = {total_price}")
    
    return {
        "type": "playmat",
        "thickness": thickness,
        "price": total_price
    }


def get_int_input(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    # Get integer input from the user, with optional min and max bounds
    while True:
        try:
            value = int(input(prompt))

            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Input must be between {min_value} and {max_value}.")
                continue

            return value
        except ValueError:
            print("Invalid input, please enter an integer.")


def get_yes_no_input(prompt: str) -> bool:
    # Get yes or no input from the user
    while True:
        user_input = input(prompt).lower()

        if user_input in ["y", "n"]:
            return user_input == "y"
        
        print("Invalid input, please enter 'y' or 'n'.")


def get_shape_input() -> tuple[str, bool]:
    # Get shape input from the user for stickers, with an option for custom shape
    while True:
        shape = get_int_input("Enter the shape (0: round, 1: square, 2: custom): ", 0, 2)

        if shape == 0:
            return "round", False
        elif shape == 1:
            return "square", False
        elif shape == 2:
            return input("Enter the custom shape of your choice: "), True


def get_surface_input() -> str:
    # Get surface input from the user for mouse pads
    while True:
        surface = get_int_input("Enter the surface options (0: cloth, 1: hard, 2: gel): ", 0, 2)
        if surface == 0:
            return "cloth"
        elif surface == 1:
            return "hard"
        elif surface == 2:
            return "gel"


def finalize_order(order: list, prices: dict) -> None:
    # Print the current order
    print()
    print("Here is your current order:")
    print_order(order)
    print()

    # Ask if the user wants to revise the order
    if get_yes_no_input("Would you like to revise your order? (y/n): "):
        order = revise_order(order, prices)
    
    # Get user personal information
    print()
    print("Please enter your personal information.")
    name = input("Name: ")
    phone = input("Phone Number: ")
    address = input("Address: ")
    total_price = sum(item['price'] for item in order)
    total_price = round(total_price, 2)
    print()
    print(f"Your total order amount is {total_price}.")
    print()
    print("Shipping prices: ")

    # Print shipping prices for each country
    for country, price in prices['shipping_prices'].items():
        print(f"{country.capitalize()}: {price}")
    
    print()
    # Calculate the shipping fee
    shipping_fee = get_shipping_fee(prices, total_price)
    # Generate the receipt
    receipt = generate_receipt(name, phone, address, order, total_price, shipping_fee)
    print()
    print("Here is your receipt:")
    print(receipt)
    # Save the receipt to a file
    open(f"orders/{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt", "w").write(receipt)
    
    # Ask if the user wants to make another transaction/order
    if get_yes_no_input("Thank you for your order! Would you like to make another transaction/order? (y/n): "):
        print()
        main()
    else:
        print()
        print("Thank you for ordering at Hobbit.")


def revise_order(order: list, prices: dict) -> list:
    # Allow the user to revise their order
    while True:
        action = get_int_input("Would you like to remove or add an item? (0: remove, 1: add, 2: done): ", 0, 2)

        if action == 0:
            # Remove an item from the order
            remove_item = get_int_input("Type the number of the item you want to remove (enter blank to cancel): ", 1, len(order))
            order.pop(remove_item - 1)
            print()
            print("Here is your current order:")
            print_order(order)
            print()
        elif action == 1:
            # Add a new item to the order
            print()
            print_services()
            print()
            service = get_int_input("Please enter the service you want to order (0-3): ", 0, 3)
            item = handle_service_selection(service, prices)
            order.append(item)
            print()
            print("Here is your current order:")
            print_order(order)
            print()
        elif action == 2:
            break

    return order


def get_shipping_fee(prices: dict, total_price: float) -> float:
    # Calculate the shipping fee based on the user's country and total price
    country = input("Enter your country: ").lower()

    if country in prices['shipping_prices']:
        shipping_fee = prices['shipping_prices'][country]
        print()

        if total_price >= 2000:
            shipping_fee = 0
            print("Since you have spent more than Php 2,000.00 on the store, you will have free shipping.")
        else:
            print(f"Shipping cost for {country.capitalize()}: {shipping_fee}")

        return shipping_fee
    else:
        print("That country is not supported.")
        return get_shipping_fee(prices, total_price)


def generate_receipt(name: str, phone: str, address: str, order: list, total_price: float, shipping_fee: float) -> str:
    # Generate a receipt for the order
    receipt = f"Name: {name}\n"
    receipt += f"Phone: {phone}\n"
    receipt += f"Address: {address}\n\n"
    receipt += "Order Details:\n"
    
    for i, item in enumerate(order, 1):
        line = f"{i}. {item['type']} - "

        for key in item:
            if key != 'type' and key != 'price':
                line += f"{key.capitalize()}: {item[key]}, "

        line += f"Price: {item['price']}\n"
        receipt += line
    
    receipt += f"\nSubtotal: {total_price}\n"
    receipt += f"Shipping: {shipping_fee}\n"
    receipt += f"Total: {total_price + shipping_fee}\n"
    return receipt


def print_order(order: list) -> None:
    # Print the current order
    for i, item in enumerate(order, 1):
        line = f"{i}. {item['type']} - "

        for key in item:
            if key != 'type' and key != 'price':
                line += f"{key.capitalize()}: {item[key]}, "

        line += f"Price: {item['price']}"
        print(line)


def print_services() -> None:
    # Print the available services
    print("Services offered:")
    print("0. Posters")
    print("1. Stickers")
    print("2. Mouse Pads")
    print("3. Playmats")


if __name__ == "__main__":
    main()