'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Combine inheritance with aggregation.
Starter code gives the base Exhibit class.
1. Write subclasses Painting and Sculpture that each override
   describe(self) and include medium information.
2. Write a Museum class that stores a list of exhibits.
   - add_exhibit(self, exhibit) appends to the list.
   - print_all(self) loops over exhibits, prints describe() for each,
     then prints "Total exhibits: <count>".
3. After writing classes, create a museum, add one painting and one
   sculpture, then call print_all().
'''

class Exhibit:
    def __init__(self, title):
        self.title = title
    def describe(self):
        return f"Exhibit: {self.title}"

class Painting(Exhibit):
    def describe(self):
        return f"Painting: {self.title}"
    
class Sculpture(Exhibit):
    def describe(self):
        return f"Sculpture: {self.title}"
    
class Museum:
    def __init__(self):
        self.exhibit = []
    def add_exhibit(self, exhibit):
        self.exhibit.append(exhibit)
    def print_all(self):
        for ex in self.exhibit:
            print(ex.describe())
        print("Total exhibits:", len(self.exhibit))

museum_1 = Museum()
museum_1.add_exhibit(Painting("Mona Lisa"))
museum_1.add_exhibit(Sculpture("Michaelangelo's David"))
museum_1.print_all()

