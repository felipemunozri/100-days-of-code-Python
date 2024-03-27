import requests
from prettytable import PrettyTable
from colorama import Fore

x = PrettyTable()
cate_id_offset = 8


class Data:

    def __init__(self):
        self.questions_list = []
        self.error_message = ""

    def get_categories_list(self):
        """Fetches and returns a list of question categories from the Open Trivia Database API."""
        r = requests.get("https://opentdb.com/api_category.php").json()
        categories_list = r["trivia_categories"]
        return categories_list

    def initialize_data(self):
        """Prints a table of question categories and takes user inputs for vars category, difficulty and num_questions.
        Passes those vars to the self.get_data() class method. If the response from self.get_data() is true returns the
        list of questions stored in the self.questions_list class attribute."""
        print()
        category_list = self.get_categories_list()  # call to self.get_categories_list class method
        category_menu = self.format_table(category_list)  # call to self.format_table class method
        print(category_menu)
        print()
        while True:
            while True:
                category = input("Chose a number from the category menu (1-24) or type (0) for mixed categories: ")
                if not category.isdigit():
                    print("Please enter a number.")
                    continue
                elif int(category) < 0 or int(category) > 24:
                    print("Please enter a number between 0 and 24.")
                    continue
                else:
                    category = int(category)
                    break
            # native API catagory ids go from 9-32 instead of 1-24. After getting user input we add cate_id_offset to
            # restore native API category ids except with 0
            if category != 0:
                category += cate_id_offset
            difficulty = input(
                "Type a difficulty level (easy, medium, hard). Press Enter for mixed difficulty 💪: ").lower()
            while True:
                num_questions = input("How many questions do you want?: ")
                if not num_questions.isdigit():
                    print("Please enter a number.")
                    continue
                elif int(num_questions) < 1 or int(num_questions) > 50:  # 50 is the max number of questions per API request
                    print("Please enter a number between 1 and 50.")
                    continue
                else:
                    num_questions = int(num_questions)
                    break     
            if self.get_data(num_questions, category, difficulty):  # call to self.get_data() class method
                break
            else:
                print(Fore.RED, self.error_message, Fore.WHITE)
        return self.questions_list

    def get_data(self, user_num_questions, user_category, user_difficulty):
        """Takes values for number of questions, question category and difficulty level. Fetches a list of questions from
        Open Trivia Database API using those values. If the response code from the API is correct (0) stores the list of
        questions in the self.questions_list class atribute and returns true."""
        payload = {
            "amount": user_num_questions,
            "category": user_category,
            "difficulty": user_difficulty,
            "type": "boolean"  # type boolean means true/false questions. API also has multiple choise questions
        }
        r = requests.get("https://opentdb.com/api.php?", params=payload).json()
        response_code = r["response_code"]
        if response_code == 0: 
            self.questions_list = r["results"]
            return True
        elif response_code == 1:
            self.error_message = "Oops! I don't have that. Try changing the difficulty level, fewer questions, or " \
                                 "try another category."
            return False

    def format_table(self, category_list):
        """Takes a list of question categories and splits it in 3 shorter lists. Then populates 3 tables with 'ID' and
        'Category' headers. Stores those 3 tables in an outer table and returns it."""
        # Split the category_list into three equal parts and store them in a chunks list 
        split_size = len(category_list) // 3
        chunks = [category_list[i:i + split_size] for i in range(0, len(category_list), split_size)]

        # Create three PrettyTable objects
        x1 = PrettyTable()
        x1.field_names = ["ID", "Category"]
        x1.align = "l"
        x2 = PrettyTable()
        x2.field_names = ["ID", "Category"]
        x2.align = "l"
        x3 = PrettyTable()
        x3.field_names = ["ID", "Category"]
        x3.align = "l"

        # Populate the PrettyTables with data from each chunk. We subtract cate_id_offset to data["id"] to show user
        # category ids from 1-24 instead of native API category ids which go from 9-32
        for data in chunks[0]:
            x1.add_row([data["id"] - cate_id_offset, data["name"]])
        for data in chunks[1]:
            x2.add_row([data["id"] - cate_id_offset, data["name"]])
        for data in chunks[2]:
            x3.add_row([data["id"] - cate_id_offset, data["name"]])

        # Concatenate the PrettyTables horizontally
        final_table = PrettyTable()
        final_table.border = False  # Remove the border around the table
        final_table.header = False  # Remove headers from outer table
        final_table.hrules = 0  # Remove horizontal rules
        final_table.add_row([x1, x2, x3])

        return final_table
