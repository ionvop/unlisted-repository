import json
import datetime
import os


def main() -> None:
    if not os.path.exists("config.json"):
        print("config.json not found. Please create a config.json file.")
        return
    
    if not os.path.exists("orders/"):
        os.makedirs("orders/")

    prices = json.load(open("config.json"))
    order = []
    print("Welcome to Hobbit, user!")
    
    while True:
        print()
        print("Services offered:")
        print("0. Posters")
        print("1. Stickers")
        print("2. Mouse Pads")
        print("3. Playmats")
        print()
        service = input("Please enter the service you want to order (0-3): ")
        service = int(service)

        if service not in range(0, 4):
            print("Invalid service. Please try again.")
            continue

        width = input("Enter the width in inches: ")
        width = int(width)
        height = input("Enter the height in inches: ")
        height = int(height)
        item = {}

        if service == 0:
            base_price = prices['services']['poster']['base_price']
            size = width * height
            rate = prices['services']['poster']['rate']
            total_price = base_price + (size * rate)
            total_price = round(total_price, 2)
            print()
            print(f"You have added a Poster of size {width}x{height} inches. The price is calculated as follows:")
            print(f"Base Price: {base_price}")
            print(f"Size in sq. inches: {size}")
            print(f"Rate per sq. inch: {rate}")
            print(f"Total Price: {base_price} + ({size} * {rate}) = {total_price}")
            
            item = {
                "type": "poster",
                "size": f"{width}x{height}",
                "price": total_price
            }
        elif service == 1:
            quantity = input("Enter the quantity: ")
            quantity = int(quantity)

            while True:
                shape = input("Enter the shape (0: round, 1: square, 2: custom): ")
                shape = int(shape)
                is_custom_shape = False

                if shape == 0:
                    shape = "round"
                elif shape == 1:
                    shape = "square"
                elif shape == 2:
                    shape = input("Enter the custom shape of your choice: ")
                    is_custom_shape = True
                else:
                    print("Invalid shape, try again.")
                    continue
    
                break

            while True:
                waterproof = input("Would you like waterproof stickers? (y/n): ")

                if waterproof == "y":
                    waterproof = True
                elif waterproof == "n":
                    waterproof = False
                else:
                    print("Invalid input, try again.")
                    continue

                break

            base_price = prices['services']['sticker']['base_price']
            size = width * height
            rate = prices['services']['sticker']['rate']

            if is_custom_shape:
                shape_multiplier = prices['services']['sticker']['shapes']['custom']
            else:
                shape_multiplier = prices['services']['sticker']['shapes'][shape]

            waterproof_option_cost = prices['services']['sticker']['waterproof'] if waterproof else 0
            total_price = (base_price + (size * rate)) * quantity * shape_multiplier + waterproof_option_cost
            total_price = round(total_price, 2)
            print()
            print(f"You have added Stickers of size {width}x{height} inches, quantity {quantity}, shape {shape}{', waterproof' if waterproof else ''}. The price is calculated as follows:")
            print(f"Base Price: {base_price}")
            print(f"Size in sq. inches: {size}")
            print(f"Rate per sq. inch: {rate}")
            print(f"Shape Multiplier ({shape}): {shape_multiplier}")

            if waterproof:
                print(f"Waterproof Option Cost: {prices['services']['sticker']['waterproof']}")
            
            print(f"Total Price: ({base_price} + ({size} * {rate})) * {quantity} * {shape_multiplier} {f'+ {waterproof_option_cost}' if waterproof else ''} = {total_price}")

            item = {
                "type": "sticker",
                "size": f"{width}x{height}",
                "quantity": quantity,
                "shape": shape,
                "waterproof": "yes" if waterproof else "no",
                "price": total_price
            }
        elif service == 2:
            surface = input("Enter the surface options (0: cloth, 1: hard, 2: gel): ")
            surface = int(surface)

            while True:
                if surface == 0:
                    surface = "cloth"
                elif surface == 1:
                    surface = "hard"
                elif surface == 2:
                    surface = "gel"
                else:
                    print("Invalid surface, try again.")
                    continue

                break

            base_price = prices['services']['mousepad']['base_price']
            size = width * height
            rate = prices['services']['mousepad']['rate']
            surface_option_cost = prices['services']['mousepad']['surfaces'][surface]
            total_price = base_price + (size * rate) + surface_option_cost
            total_price = round(total_price, 2)
            print()
            print(f"You have added Mouse Pads of size {width}x{height} inches, surface options {surface}. The price is calculated as follows:")
            print(f"Base Price: {base_price}")
            print(f"Size in sq. inches: {size}")
            print(f"Rate per sq. inch: {rate}")
            print(f"Surface Option Cost: {surface_option_cost}")
            print(f"Total Price: {base_price} + ({size} * {rate}) + {surface_option_cost} = {total_price}")

            item = {
                "type": "mousepad",
                "size": f"{width}x{height}",
                "surface": surface,
                "price": total_price
            }
        elif service == 3:
            thickness = input("Enter the thickness in millimeters: ")
            thickness = int(thickness)
            base_price = prices['services']['playmat']['base_price']
            size = width * height
            rate = prices['services']['playmat']['rate']
            thickness_price = thickness * prices['services']['playmat']['thickness_rate']
            total_price = base_price + (size * rate) + thickness_price
            total_price = round(total_price, 2)
            print()
            print(f"You have added Playmats of thickness {thickness} millimeters. The price is calculated as follows:")
            print(f"Base Price: {base_price}")
            print(f"Size in sq. inches: {size}")
            print(f"Rate per sq. inch: {rate}")
            print(f"Thickness Cost: {thickness_price}")
            print(f"Total Price: {base_price} + ({size} * {rate}) + {thickness_price} = {total_price}")

            item = {
                "type": "playmat",
                "thickness": thickness,
                "price": total_price
            }

        order.append(item)
        print()
        do_another = False

        while True:
            user_in = input("Would you like to order another service? (y/n): ")

            if user_in.lower() == "y":
                do_another = True
            elif user_in.lower() == "n":
                do_another = False
            else:
                print("Invalid input, try again.")
                continue

            break

        if do_another:
            continue

        print()
        print("Here is your current order:")
        print_order(order)
        print()
        do_revise = False

        while True:
            user_in = input("Would you like to revise your order? (y/n): ")

            if user_in.lower() == "y":
                do_revise = True
            elif user_in.lower() == "n":
                do_revise = False
            else:
                print("Invalid input, try again.")
                continue

            break

        action = -1

        if do_revise:
            while True:
                print()

                while True:
                    user_in = input("Would you like to remove or add an item? (0: remove, 1: add, 2: done): ")
                    user_in = int(user_in)

                    if user_in in range(0, 3):
                        action = user_in
                    else:
                        print("Invalid input, try again.")
                        continue

                    break

                if action == 0:
                    remove_item = -1

                    while True:
                        user_in = input("Type the number of the item you want to remove (enter blank to cancel): ")
                        if user_in == "":
                            action = -1
                            break

                        remove_item = int(user_in)

                        if remove_item < 1 or remove_item > len(order):
                            print("That item does not exist.")
                            continue

                        break

                    if action == 0:
                        order.pop(remove_item - 1)
                        print()
                        print("Here is your current order:")
                        print_order(order)
                        print()
                else:
                    break

            if action == 1:
                continue

        print()
        print("Please enter your personal information.")
        name = input("Name: ")
        phone = input("Phone Number: ")
        address = input("Address: ")
        total_price = 0

        for item in order:
            total_price += item['price']

        total_price = round(total_price, 2)
        print()
        print(f"Your total order amount is {total_price}.")
        print()
        print("Shipping prices: ")

        for country in prices['shipping_prices']:
            print(f"{country.capitalize()}: {prices['shipping_prices'][country]}")

        print()
        shipping_fee = 0

        while True:
            country = input("Enter your country: ")
            
            if country.lower() in prices['shipping_prices']:
                shipping_fee = prices['shipping_prices'][country]
            else:
                print("That country is not supported.")
                continue

            break

        print()
        print(f"Shipping cost for {country.capitalize()}: {shipping_fee}")

        if total_price >= 2000:
            shipping_fee = 0
            print("Since you have spent more than Php 2,000.00 on the store, you will have free shipping.")
        else:
            print("Since your total order is less than Php 2,000.00, shipping cost will be applied.")

        receipt = ""
        receipt += f"Name: {name}\n"
        receipt += f"Phone: {phone}\n"
        receipt += f"Address: {address}\n\n"
        receipt += "Order Details:\n"
        i = 1

        for item in order:
            line = ""

            for key in item:
                if key == "type":
                    line += f"{i}. {item[key]} - "
                    continue
               
                if key == "price":
                    line += f"Price: {item[key]}\n"
                    break

                line += f"{key.capitalize()}: {item[key]}, "

            receipt += line
            i += 1

        receipt += f"\nSubtotal: {total_price}\n"
        receipt += f"Shipping: {shipping_fee}\n"
        receipt += f"Total: {total_price + shipping_fee}\n"
        print()
        print("Here is your receipt:")
        print(receipt)
        open(f"orders/{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt", "w").write(receipt)
        do_another = False

        while True:
            user_in = input("Thank you for your order! Would you like to make another transaction/order? (y/n): ")

            if user_in.lower() == "y":
                do_another = True
            elif user_in.lower() == "n":
                do_another = False
            else:
                print("Invalid input, try again.")
                continue

            break

        if do_another:
            order = []
            continue

        break

    print()
    print("Thank you for ordering at Hobbit.")


def print_order(order: list) -> None:
    i = 1

    for item in order:
        line = ""

        for key in item:
            if key == "type":
                line += f"{i}. {item[key]} - "
                continue
            
            if key == "price":
                line += f"Price: {item[key]}"
                break

            line += f"{key.capitalize()}: {item[key]}, "

        print(line)
        i += 1


if __name__ == "__main__":
    main()