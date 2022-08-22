from model import Person


def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:
        print(item.name())


def start_menu_view():
    print('\n*** MVC - the simplest example ***')
    print('\ninput the desired method')
    print('     1. Do you want to see everyone in my db?')
    print('     2. Do you want to add someone to my db?')
    print('     3. Do you want to remove someone from my db? (sends them to the gulag)')
    print('     4. Exit')


def update_view(method, return_Code):
    if method == 'insert':
        if return_Code == 0:
            print("*** person appended successfully to db.json ***")
        elif return_Code == 1:
            print("*** person already in db.json, safe from gulag ***")
        else:
            print('incorrect update_view() usage')

    elif method == 'delete':
        if return_Code == 0:
            print("*** person deleted successfully from db.json, now in gulag ***")
        elif return_Code == 1:
            print("*** person not found in db.json, must be in gulag ***")
        else:
            print('incorrect update_view() usage')

    else:
        print('incorrect update_view() usage')


def end_view():
    print('Goodbye!')
