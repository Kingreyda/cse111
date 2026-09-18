def main():
    """
    This is the main function for the Miles Per Gallon program.
    """
    start_miles = float(input("\nEnter the first odometer reading (miles): "))
    end_miles = float(input("Enter the second odometer reading (miles): "))
    fuel_gallons = float(input("Enter the amount of fuel used (gallons): "))
    
    #miles per gallon function call
    def miles_per_gallon(start_miles, end_miles, fuel_gallons):
        """
        This function calculates the miles per-gallon based
        on the starting miles, the ending miles and the gallons 
        of fuel used.
        """
        mpg = (end_miles - start_miles) / fuel_gallons
        return mpg

    #liters per 100 kilometers function call
    def get_1p100k(mpg):
        """
        This function calculates the liter per 100 kilometers based
        on the miles per gallon value.

        """
        l_per_100k = 235.215 / mpg
        return l_per_100k

    mpg = miles_per_gallon(start_miles, end_miles, fuel_gallons)
    l_per_100k = get_1p100k(mpg)

    print(f"\n{mpg:.1f} miles per gallon")
    print(f"{l_per_100k:.2f} liters per 100 kilometers\n")
     
main()