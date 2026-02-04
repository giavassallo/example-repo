class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    head_office = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def office_location(self):
        print("The head office location is ", self.head_office)

    class OOPCourse(Course):
        def __init__(self, description, trainer):
            self.description = "OOP Fundamentals"
            self.trainer = "Mr Anon A. Mouse"

        def trainer_details(self):
            print(f"Course: ",self.name)
            print(f"Description: ",self.description)
            print(f"Trainer: ",self.trainer)

        def show_course_id(self):
            print("Course ID: #12345")

# Create an instance of the Course class
course_1 = Course()

# Call the contact_details method to display contact information
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
