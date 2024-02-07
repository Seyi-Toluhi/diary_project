from lib.diary import *

"""
Given a diary
When we add tasks
We see those tasks reflected in the tasks list
"""

def test_diary_adds_task():
    my_diary = Diary()
    task_1 = Task.add("Buy groceries")
    task_2 = Task.add("Mop the house")
    my_diary.add_task(task_1)
    my_diary.add_task(task_2)
    assert my_diary.show_tasks() == ["Buy groceries", "Mop the house"]

"""
Given a diary
When we add contacts
We see those contacts reflected in the contact list
"""
def test_diary_adds_contacts():
    my_diary = Diary()
    contact_1 = Contact.add("07563788399")
    contact_2 = Contact.add("07584688377")
    my_diary.add_contact(contact_1)
    my_diary.add_contact(contact_2)
    assert my_diary.see_contacts() == ["07563788399", "07584688377"] 

"""
Given an experience
its added to diary dict
and can be shown
"""
def test_diary_adds_and_shows_experience():
    my_diary = Diary()
    my_diary.record("Holiday","Holiday_experience")
    assert my_diary.reflect("Holiday") == "Holiday_experience"


"""
Given an experience
its added to diary dict
and can be shown in chunk
"""
def test_diary_adds_and_shows_experience_in_chunk():
    my_diary = Diary()
    my_diary.record("Holiday","Holiday_experience")
    assert my_diary.reflect_in_chunk("Holiday", 5, 1) == "Holid"
