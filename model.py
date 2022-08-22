import json
import os


class Person(object):

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name, ex: John Doe
    def name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @classmethod
    # returns all people inside db.json as list of Person objects
    def get_all(cls):
        result = list()
        with open('db.json', 'r') as json_outFile:
            data = json.load(json_outFile)
            for p in data['employees']:
                person = Person(p['first_name'], p['last_name'])
                result.append(person)
        return result

    @classmethod
    # appends person into last position of db.json
    def insert(cls, first_Name, last_Name):
        with open('db.json', 'r') as json_File:
            data = json.load(json_File)

            for person in data['employees']:
                if person["first_name"] == first_Name and person["last_name"] == last_Name:
                    # print("*** person already in db.json ***")
                    return 1

        with open('db.json', 'a+') as json_File:  # a+ -> append mode
            json_File.truncate(json_File.tell() - 4)  # resizes file to remove "]}" and go back one line
            json_File.write(",\n")
            json_File.writelines(['\t{"first_name":"', first_Name, '", "last_name":"', last_Name, '"}'])
            json_File.write("\n]}")

            return 0
            # print("*** person appended successfully to db.json ***")

    @classmethod
    # deletes a person from db.json
    def delete(cls, first_Name, last_Name):
        with open('db.json', 'r') as json_File:
            data = json.load(json_File)

        not_found = True

        for person in data['employees']:
            if person["first_name"] == first_Name and person["last_name"] == last_Name:
                data['employees'].remove(person)
                not_found = False

        if not_found:
            # print("*** person not found in db.json, must be in gulag ***")
            return 1

        with open('db.json', 'a+') as json_File:
            json_File.truncate(17)
            for person in data['employees']:
                json_File.writelines(
                    ['\t{"first_name":"', person["first_name"], '", "last_name":"', person["last_name"], '"}'])
                json_File.write(",\n")
            json_File.truncate(json_File.tell() - 3)
            json_File.write("\n]}")

        return 0
        # print("*** person deleted successfully from db.json, now in gulag ***")
