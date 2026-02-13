# Student Marks File Processor

total_marks = 0
valid_count = 0
invalid_count = 0

try:
    file = open("marks.txt", "r")
    lines = file.readlines()

    if not lines:
        raise Exception("File is empty.")

    for line in lines:
        try:
            parts = line.strip().split(",")

            if len(parts) != 2:
                raise Exception("Incorrect format")

            name, marks = parts
            marks = int(marks)   # May raise ValueError

            print(f"Student: {name}, Marks: {marks}")

            total_marks += marks
            valid_count += 1

        except:
            print(f"Skipping invalid record: {line.strip()}")
            invalid_count += 1

    if valid_count > 0:
        average = total_marks / valid_count
        print("\nAverage Marks:", average)

    print("Valid Records:", valid_count)
    print("Invalid Records:", invalid_count)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)