"""
Name: King David Olaribigbe
Project: Grocery Store Receipt

Enhancement:
Added a return-by date that automatically calculates a
customer's return deadline 30 days from the purchase date
and displays the deadline at 9:00 PM.
"""

import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    product_dictionary = {}

    with open(filename, "rt") as file:
        readable_file = csv.reader(file)
        next(readable_file)
        for row_list in readable_file:
            key_value = row_list[key_column_index]
            product_dictionary[key_value] = row_list
    return product_dictionary


def main():
    try:
        PRODUCT_NUMBER_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        QUANTITY_INDEX = 1
        PRICE_INDEX = 2

        number_of_items = 0
        subtotal = 0.0

        product_dict = read_dictionary("products.csv", 0)

        with open("request.csv", "rt") as request_file:
            request_file = csv.reader(request_file)
            next(request_file)

            print("\n=====================================")
            print("        King's Grocery Store")
            print("=====================================\n") 

            for row_list in request_file:
                product_number = row_list[PRODUCT_NUMBER_INDEX]
                quantity = int(row_list[QUANTITY_INDEX])

                product_info = product_dict[product_number]
                product_name = product_info[PRODUCT_NAME_INDEX]
                product_price = float(product_info[PRICE_INDEX])

                number_of_items += quantity
                subtotal += product_price * quantity

                print(f"{product_name}: {quantity} @ {product_price}")
           
        print(f"\nNumber of Items: {number_of_items}")
        print(f"Sub Total: {subtotal:.2f}")
        
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        print(f"\nSales Tax: {sales_tax:.2f}")
        print(f"Total: ${total:.2f}")

        time_now = datetime.now()
        formatted_date = time_now.strftime("%a %b %#d %H:%M:%S %Y")
        print(formatted_date)

        #Enhancement: Added a return-by date that shows customers the last date
        # (30 days from purchase) that items may be returned.
        
        return_by_date = datetime.now() + timedelta(days=30)       
        return_by_time = return_by_date.replace(
            hour=21,
            minute=0,
            second=0
        )

        print(f"\nReturn by: {return_by_date.strftime('%a %b %#d %Y')} - {return_by_time.strftime('%I:%M %p')}")

        print("\n===============================================")
        print("Thank you for shopping at King's Grocery Store.")
        print("===============================================\n")

    except FileNotFoundError as e:
        print(f"Error: missing file")
        print(e)

    except PermissionError as e:
        print("Error: permission denied")
        print(e)

    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file")
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()