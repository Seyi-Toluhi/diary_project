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
        self.experience_store[title] = experience

    def reflect(self, title):
        # Parameters:
        #   title: string
        # Returns:
        #   A string of the experince held under the key
        return self.experience_store[title]

    def reflect_in_chunk(self, title, time, speed):
        # Parameters:
        #   title: string
        #   time: integer
        #   speed: integer
        self.time = time
        self.speed = speed
        reading_length = self.time * self.speed
        # Returns:
        #   A chunk of the experience held under the key
        full_experience = self.experience_store[title]
        return full_experience[:reading_length]

    def add_task(self, task):
        # Parameters:
        #   str: string rep an instance of task class
        #Side-effects:
        #   Adds the task to self.todo_list
        self.todo_list.append(task)

    def show_tasks(self):
        # Returns:
        #   A list of the Task list of the task class
        return self.todo_list

    def add_contact(self, contact):
        # Parameters:
        #   str: string rep an instance of contact class
        #Side-effects:
        #   Adds the task to self.contact_list
        self.contact_list.append(contact)

    def see_contacts(self):
        # Returns:
        #   A list of the contacts list of the contact class
        return self.contact_list

class Task:
    # User-facing properties:

    def __init__(self):
        
        # Side-effects:
        
        pass # No code here yet

    def add(task):
        # Parameters:
        #   task: string
        # Returns:
        #   A string of the form "TASK"
        return task

class Contact:
    # User-facing properties:

    def __init__(self):
        # Side-effects:
        
        pass # No code here yet

    def add(contact):
        # Parameters:
        #   contact: string
        # Returns:
        #   A string of the form "TASK"
        return contact