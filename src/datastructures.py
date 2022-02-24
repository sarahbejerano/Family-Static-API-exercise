
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self._members = []
        self._last_name = last_name



    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        return self._members.append({
            "id": member["id"],
            "first_name": member["first_name"],
            "last_name": self._last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        })


    def delete_member(self, id):
        for element in self._members:
            if element["id"] == id:
                self._members.remove(element)
                return True
        return False


    def get_member(self, id):
        for element in self._members:
            if element["id"] == id:
                return element
        return None


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
