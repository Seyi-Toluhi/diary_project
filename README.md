# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```

```


Nouns
experiences 
speed
time 
todo_list
mobile phone numbers

Verbs
record
reflect
select_reflection_chunk
track_tasks
see_mobile phone numbers


_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        self.experience_store = {}
        self.todo_list = []
        self.contact_list = []

    def record(self, title, experience):
        # Parameters:
        #   title : string for dict key 
        #   experience : string for dict value
        # Side-effects:
        #   Adds the experience to self.experience_store
        pass # No code here yet

    def reflect(self, title):
        # Parameters:
        #   title: string
        # Returns:
        #   A string of the experince held under the key
        pass # No code here yet

    def reflect_in_chunk(self, title, time, speed):
        # Parameters:
        #   title: string
        #   time: integer
        #   speed: integer
        # Returns:
        #   A chunk of the experience held under the key
        pass # No code here yet

    def add_task(self, str):
        # Parameters:
        #   str: string rep an instance of task class
        #Side-effects:
        #   Adds the task to self.todo_list
        pass # No code here yet

    def show_tasks(self):
        # Returns:
        #   A list of the Task list of the task class
        pass # No code here yet

    def add_contact(self, str):
        # Parameters:
        #   str: string rep an instance of contact class
        #Side-effects:
        #   Adds the task to self.contact_list
        pass # No code here yet

    def see_contacts(self):
        # Returns:
        #   A list of the contacts list of the contact class
        pass # No code here yet


class Task:
    # User-facing properties:

    def __init__(self):
        
        # Side-effects:
        
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string
        # Returns:
        #   A string of the form "TASK"
        pass # No code here yet

class Contact:
    # User-facing properties:

    def __init__(self):
        # Side-effects:
        
        pass # No code here yet

    def add(self, contact):
        # Parameters:
        #   contact: string
        # Returns:
        #   A string of the form "TASK"
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a diary
When we add tasks
We see those tasks reflected in the tasks list
"""
my_diary = diary()
task_1 = Task.add("Buy groceries")
task_2 = Task.add("Mop the house")
contact_1 = Contact.add("07563788399")
contact_2 = Contact.add("07584688377")
my_diary.add_task(task_1)
my_diary.add_task(task_2)
my_diary.add_contact(contact_1)
my_diary.add_contact(contact_2)
my_diary.show_tasks # => [task_1, task_2]
my_diary.see_contacts # => [contact_1, contact_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given an experience
its added to diary dict
and can be shown
"""
my_diary = diary()
my_diary.record("Holiday","Holiday_experience")
my_diary.reflect("Holiday") # => Holiday_experience

```
```python
# EXAMPLE

"""
Given an experience
its added to diary dict
and can be shown in chunk
"""
my_diary = diary()
my_diary.record("Holiday","Holiday_experience")
my_diary.reflect_in_chunk("Holiday", 2, 1) # => Holiday_expe

```


_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
