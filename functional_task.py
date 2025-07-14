import pandas as pd

pd.options.display.max_rows = 999


def read_csv_info(file_name: str) -> pd.DataFrame:
    """
    Reads a CSV file into a DataFrame and optionally displays info and sample rows.

    Args:
        file_name (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    df = pd.read_csv(file_name)

    while True:
        proceed = input("Do you want to see the info? (Y/N): ").strip().lower()
        if proceed in ("y", "n"):
            break
        print("Invalid input. Please enter 'Y' or 'N'.")

    if proceed == "y":
        print("\n********************************************************")
        print("The table general info is as below: \n")
        print(
            df.info(verbose=True, show_counts=True)
        )  # all the necessary info about the table
        print("\n********************************************************")
        print("Here is a peek at the data: \n")
        print(df.head())  # print the first and last 5 rows for visualization
        print("\n********************************************************")
    return df


def sort_release_date(data_table: pd.DataFrame) -> pd.DataFrame:
    """
    Arrange the data in the table by the specified column.
    Args:
    data_table (pd.DataFrame): The table to be arranged.
    column_name (str): The name of the column to arrange by.
    Returns:
    pd.DataFrame: The arranged table.
    """
    temp_table = data_table.copy()
    temp_table["release_date"] = pd.to_datetime(
        temp_table["release_date"], errors="coerce"
    )
    sorted_data = temp_table.sort_values(by="release_date", ascending=False)
    sorted_data.to_csv("1.sorted_data.csv", index=False)
    return sorted_data


def filter_rating(data_table: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the data in the table by vote_average.
    Args:
    data_table (pd.DataFrame): The table to be filtered.
    Returns:
    pd.DataFrame: The filtered table.
    """
    temp_table = data_table.copy()
    filtered_data = temp_table[temp_table["vote_average"] > 7.5]
    filtered_data.to_csv("2.filtered_data.csv", index=False)
    return filtered_data


def top_revenue(data_table: pd.DataFrame) -> None:
    """
    Find the movie with highest and lowest revenue (that is not 0).
    Args:
    data_table (pd.DataFrame): The table to be searched.
    Returns:
    None
    """
    temp_table = data_table.copy()
    temp_table = temp_table[temp_table["revenue"] > 0]
    highest_revenue = temp_table.loc[temp_table["revenue"].idxmax()]
    lowest_revenue = temp_table.loc[temp_table["revenue"].idxmin()]
    print("\n********************************************************")
    print("\nHighest revenue movie:")
    print(
        f"Name: {highest_revenue['original_title']}, Revenue: ${highest_revenue['revenue']:,.2f}"
    )
    print("\nLowest revenue movie (not 0):")
    print(
        f"Name: {lowest_revenue['original_title']}, Revenue: ${lowest_revenue['revenue']:,.2f}"
    )
    print("\n********************************************************")
    return None


def total_revenue(data_table: pd.DataFrame) -> None:
    """
    Calculate the total revenue of all movies in the table.
    Args:
    data_table (pd.DataFrame): The table to be searched.
    Returns:
    None
    """
    temp_table = data_table.copy()
    total_revenue = temp_table["revenue"].sum()
    print("\n********************************************************")
    print(f"\nTotal revenue: ${total_revenue:,.2f}")
    print("\n********************************************************")
    return None


def top_10(data_table: pd.DataFrame) -> pd.DataFrame:
    """
    Find the top 10 movies with the highest revenue.
    Args:
    data_table (pd.DataFrame): The table to be searched.
    Returns:
    pd.DataFrame: The top 10 movies with the highest revenue.
    """
    temp_table = data_table.copy()
    top_10_movies = temp_table.nlargest(10, "revenue_adj")
    print("\n********************************************************")
    print(top_10_movies)
    print("********************************************************")
    top_10_movies.to_csv("5.top_10_revenue.csv", index=False)
    return top_10_movies


def most_active(data_table: pd.DataFrame) -> None:
    """
    Find the Director with most movies and Actor/Actress join the most movies.
    Args:
    data_table (pd.DataFrame): The table to be searched.
    Returns:
    None
    """
    temp_table = data_table.copy()

    director_count = temp_table["director"].value_counts()

    cast_table = data_table["cast"].str.split("|", expand=True)
    # cast_table = pd.DataFrame(cast_table, index=data_table["original_title"])
    cast_table = pd.Series(cast_table.values.ravel())
    most_active_actor = cast_table.value_counts().idxmax()

    print("\n********************************************************")
    print(
        f"Director with most movies: {director_count.idxmax()} with {director_count.max()} movies."
    )
    print(
        f"Actor/Actress with most movies: {most_active_actor} with {cast_table.value_counts().max()} movies."
    )
    print("********************************************************")
    return None


def genre_stat(data_table: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the numbers of movies in each genre (including sub-genres).
    Args:
    data_table (pd.DataFrame): The table to be searched.
    Returns:
    pd.DataFrame: The table with genre statistics.
    """
    temp_table = data_table.copy()
    genre_count = "|".join(temp_table["genres"].astype(str))
    genre_list = genre_count.split("|")
    genre_stat = pd.Series(genre_list).value_counts()
    print("\n********************************************************")
    print(genre_stat)
    print("********************************************************")
    genre_stat.to_csv("7.genre_stat.csv", index=False)
