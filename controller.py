from model import Person
import view


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


def update_msg(method, return_Code):
    return view.update_view(method, return_Code)  # calls proper update msg view


def insert_person():
    # calls Person.insert() and sends update_msg code to view
    update_msg('insert', Person.insert(input("Input First Name: "), input("Input Last Name: ")))


def delete_person():
    # calls Person.delete() and sends update_msg code to view
    update_msg('delete', Person.delete(input("Input First Name: "), input("Input Last Name: ")))


def start():
    while True:
        view.start_menu_view()
        input_var = int(input())  # updated raw_input() -> input
        if input_var == 1:
            show_all()
        elif input_var == 2:
            insert_person()
        elif input_var == 3:
            delete_person()
        elif input_var == 4:
            return view.end_view()


if __name__ == "__main__":
    # running controller function
    start()
