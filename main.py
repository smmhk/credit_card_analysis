from controller.main_controller import MainController
from config.constants import FILE_NAME


def main():
    file_path = "data/categorized_credit_card_data.csv"
    controller = MainController(file_path)
    controller.start()


if __name__ == "__main__":
    main()