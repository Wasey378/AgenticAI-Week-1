from .Services.Calculate import calculate_grade
from .Utils.Validate import validate_marks, validate_name
from .logger import logger


def main():
    logger.info("Application started")
    name = input("Enter student name: ")
    if not validate_name(name):
        logger.warning("Empty student name entered")
        print("Error: Name cannot be empty.")
        return

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        logger.error("Invalid marks entered")
        print("Error: Marks must be a number.")
        return

    if not validate_marks(marks):
        logger.warning("Invalid marks entered: %s", marks)
        print("Error: Marks must be between 0 and 100.")
        return

    grade = calculate_grade(marks)

    print()
    print("Student Report")
    print("----------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
