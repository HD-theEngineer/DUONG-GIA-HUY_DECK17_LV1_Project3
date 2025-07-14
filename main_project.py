from project_init_procedure import parse_file, project_option_menu


def main():
    data_file_name = parse_file("file_data.ini")
    project_option_menu(data_file_name)


if __name__ == "__main__":
    main()
