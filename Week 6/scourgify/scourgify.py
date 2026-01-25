import sys, csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        print("Not a CSV file")
        sys.exit(1)
    else:

        students = []
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(row)

            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for i in range(len(students)):
                    last , first = students[i]['name'].strip('"').split(", ")
                    row = writer.writerow({"first": first, "last": last, "house": students[i]['house']})

        except FileNotFoundError:
            print("Could not read", sys.argv[1])
            sys.exit(1)


# first failed logic
# with open("after.csv", "w") as file:
#                 writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
#                 for row in students:
#                     row = writer.writerow({"last": last, "first": first = students['name'].strip('"').split(", "), "house": students['house']})


#second failed logic (unnecessarily raised exception)
# try:
#                 with open(sys.argv[2], "w") as file:
#                     if sys.argv[2] != "after.csv":
#                         raise Exception
#                     writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
#                     writer.writeheader()
#                     for i in range(len(students)):
#                         last , first = students[i]['name'].strip('"').split(", ")
#                         row = writer.writerow({"first": first, "last": last, "house": students[i]['house']})
#             except Exception:
#                 print("Could not write", sys.argv[2], "as AFTER.CSV")
#                 sys.exit(1)
