from calculator import CalculatorEngine

calc = CalculatorEngine()
def print_main_menu():
    print("\n==== Main Menu ====")
    print("1. Evaluate Expression (ex., 2+3, sqrt(16), sin(30), log(100), ln(e), exp(1),")
    print("   fact(5), inv(4), abs(-7), pi*r**2, trig: sin/cos/tan/asin/acos/atan/sec/cosc/cot)")
    print("2. Memory Menu")
    print("3. Statistics Menu")
    print("4. View History")
    print("5. Geometry Menu")
    print("6. Integration")
    print("7. Solve Equation")
    print("8. Unit Conversions")
    print("9. View Last Result")
    print("10. Quit")
    
def geometry_menu():
    while True:
        print("\nGeometry Area Menu:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        print("5. Back to Main Menu")

        choice = input("Choose shape: ")

        if choice == "1":
            r = float(input("Enter radius: "))
            print("Area of Circle:", calc.geom.area_circle(r))
        elif choice == "2":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print("Area of Rectangle:", calc.geom.area_rectangle(l, w))
        elif choice == "3":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Area of Triangle:", calc.geom.area_triangle(b, h))
        elif choice == "4":
            s = float(input("Enter side: "))
            print("Area of Square:", calc.geom.area_square(s))
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def memory_menu():
    while True:
        print("\nMemory Menu:")
        print("1. Add to Memory")
        print("2. Subtract from Memory")
        print("3. Recall Memory")
        print("4. Clear Memory")
        print("5. Back to Main Menu")

        choice = input("Choose option: ")

        if choice == "1":
            val = input("Enter value to add: ")
            try:
                calc.mem.memory_add(float(val))
                print("Added to memory.")
            except:
                print("Invalid number.")
        elif choice == "2":
            val = input("Enter value to subtract: ")
            try:
                calc.mem.memory_subtract(float(val))
                print("Subtracted from memory.")
            except:
                print("Invalid number.")
        elif choice == "3":
            print("Memory Value:", calc.mem.memory_recall())
        elif choice == "4":
            calc.mem.memory_clear()
            print("Memory cleared.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def conversion_menu():
    while True:
        print("\nConversion Menu:")
        print("1. Degrees to Radians")
        print("2. Radians to Degrees")
        print("3. Degrees to Gradians")
        print("4. Gradians to Degrees")
        print("5. DMS to Decimal Degrees")
        print("6. Decimal Degrees to DMS")
        print("7. Back to Main Menu")

        choice = input("Choose option: ")

        if choice == "1":
            d = float(input("Enter degrees: "))
            print("Radians:", calc.conv.deg_to_rad(d))
        elif choice == "2":
            r = float(input("Enter radians: "))
            print("Degrees:", calc.conv.rad_to_deg(r))
        elif choice == "3":
            d = float(input("Enter degrees: "))
            print("Gradians:", calc.conv.deg_to_grad(d))
        elif choice == "4":
            g = float(input("Enter gradians: "))
            print("Degrees:", calc.conv.grad_to_deg(g))
        elif choice == "5":
            d = int(input("Enter degrees: "))
            m = int(input("Enter minutes: "))
            s = float(input("Enter seconds: "))
            print("Decimal Degrees:", calc.conv.dms_to_decimal(d, m, s))
        elif choice == "6":
            dec = float(input("Enter decimal degrees: "))
            d, m, s = calc.conv.decimal_to_dms(dec)
            print(f"DMS: {d}° {m}' {s:.2f}\"")
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


def stats_menu():
    print("\nStatistics Menu:")
    nums = input("Enter numbers but separated with comma: ")
    parts = nums.split(',')
    numbers = []
    for item in parts:
        try:
            numbers.append(float(item.strip()))
        except:
            print("Invalid input. Aborting.")
            return

    if not calc.stats.load_data(numbers):
        print("Failed to load data.")
        return

    print("Mean:", calc.stats.mean())
    print("Median:", calc.stats.median())
    print("Mode:", calc.stats.mode())
    
def view_last_result():
    basic = calc.basic.get_last_result()
    sci = calc.sci.get_last_result()

    if basic != 0:
        print("Last Basic Result:", basic)
    if sci != 0:
        print("Last Scientific Result:", sci)

    if basic == 0 and sci == 0:
        print("No result stored yet.")
    

print("Welcome to the Scientific Calculator")

while True:
    print_main_menu()
    choice = input("Choose option: ")

    if choice == "1":
        expr = input("Enter expression: ")
        result = calc.evaluate_expression(expr)
        print("= ", result)

    elif choice == "2":
        memory_menu()

    elif choice == "3":
        stats_menu()

    elif choice == "4":
        print("\nLast 10 History Entries:")
        for entry in calc.hist.get_history():
            print(entry)

    elif choice == "5":
        geometry_menu()

    elif choice == "6":
        expr = input("Enter expression to integrate (e.g., x**2): ")
        var = input("Enter variable of integration (default: x): ") or "x"
        definite = input("Definite integral? (y/n): ").lower()

        if definite == "y":
            lower = float(input("Enter lower limit: "))
            upper = float(input("Enter upper limit: "))
            result = calc.integrate(expr, var, lower, upper)
        else:
            result = calc.integrate(expr, var)

        print("Result:", result)
        
    elif choice == "7":
        equation = input("Enter equation to solve (ex. 2*x + 3 = 7): ")
        var = input("Enter variable to solve for (default: x): ") or "x"
        result = calc.solve_equation(equation, var)
        print("Solution:", result)

    elif choice == "8":
        conversion_menu()

    elif choice == "9":
        view_last_result()

    elif choice == "10":
        break
    
    else:
        print("Invalid option. Try again.")
