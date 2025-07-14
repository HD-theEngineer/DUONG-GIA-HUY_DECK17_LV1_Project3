from functional_task import (
    read_csv_info,
    sort_release_date,
    filter_rating,
    top_revenue,
    total_revenue,
    top_10,
    most_active,
    genre_stat,
)
import configparser as cp


def parse_file(file_data):
    config = cp.ConfigParser()
    with open(file_data, "r") as f:
        config.read_file(f)

    # Access the data by section & key
    file_name = config.get("files", "datafile")
    print(f"Imported {file_name} into main project.")
    print("Proceeding the file...")
    print("\n********************************************************")
    return file_name


def project_option_menu(data_file_name):
    data_table = read_csv_info(data_file_name)

    # Define operations mapping: option number -> (description, function)
    operations = {
        "1": ("Arrange movies by release_date", sort_release_date),
        "2": ("Filter out only movies with rating over 7.5", filter_rating),
        "3": ("Print the movies highest and lowest revenue (not 0)", top_revenue),
        "4": ("Total revenue of all movies", total_revenue),
        "5": ("Filter out the top highest revenue", top_10),
        "6": ("Most active Director and Actor/Actress", most_active),
        "7": ("Movies count in each genre", genre_stat),
        "e": ("Exit", None),
    }

    while True:
        print("\nChoose an operation to perform on the data:")
        for key, (desc, _) in operations.items():
            print(f"{key}. {desc}")

        choice = (
            input(f"Enter your choice (1-{len(operations) - 1} or e): ").lower().strip()
        )

        if choice == "e":
            print("Exiting.")
            break
        elif choice not in operations:
            print(
                f"Invalid choice. Please enter a number between 1 and {len(operations)}."
            )
            continue
        elif choice in ["1", "2"]:
            _, func = operations[choice]
            result = func(data_table)
            print(result.head(10))
        else:
            _, func = operations[choice]
            func(data_table)

            # if result is not None:
            #     data_table = result
