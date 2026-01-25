from tabulate import tabulate
import sys, csv

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        
        pizzas = []
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    pizzas.append({"pizzatype": row[0], "smallrate": row[1], "largerate": row[2]})

            print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
