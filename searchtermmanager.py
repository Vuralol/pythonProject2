import EbscoRoute
import re


class SearchManager:
    def __init__(self):
        self.result_dict = {}

    def get_user_input(self):
        ui_flag = True
        print("1 text_tx,"
              "2 author_au,"
              "3 title_ti,"
              "4 subject_term_tu,"
              "5 source_so,"
              "6 abstract_ab,"
              "7 issn_is,"
              "8 isbn_is")

        while ui_flag:
            user_input = input(
                "Enter the numbers 1 to 8 separated by commas for the specific fields you want to search for:")
            if user_input.strip() == "":
                print("Nothing entered. Please enter numbers from 1 to 8 separated by commas.")
            elif re.match(r'^[1-8](,[1-8])*$|^$', user_input):
                ui_flag = False
            else:
                print("Invalid input. Please enter numbers from 1 to 8 separated by commas.")

        return user_input

    def perform_search(self):
        user_input = self.get_user_input()
        numbers = [int(num) for num in user_input.split(',')]

        function_mapping = {
            1: EbscoRoute.text_tx,
            2: EbscoRoute.author_au,
            3: EbscoRoute.title_ti,
            4: EbscoRoute.subject_term_su,
            5: EbscoRoute.source_so,
            6: EbscoRoute.abstract_ab,
            7: EbscoRoute.issn_is,
            8: EbscoRoute.isbn_is,
        }

        for number in numbers:
            if 1 <= number <= 8:
                self.result_dict[number] = function_mapping[number]()
            else:
                print(f"Ignoring {number} as it is not between 1 and 8.")

    def display_results(self):
        print("Results:")
        for key, value in self.result_dict.items():
            print(f"Field {key}: {value}")


if __name__ == "__main__":
    def main():
        search_manager = SearchManager()
        search_manager.perform_search()
        search_manager.display_results()
