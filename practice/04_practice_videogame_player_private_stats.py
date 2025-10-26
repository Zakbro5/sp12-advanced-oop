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
Work with private variables (double-underscore) and simple getters and setters.
1. Write a Player class with private __health that starts at 100.
2. Provide get_health(self) and set_health(self, value).
   - set_health should refuse values below 0 and print
     "Invalid health value" if attempted.
3. Create a Player, lower health to 60, then try to set to -10, and
   finally print current health.
'''

class Player:
    def __init__(self):
        self.__health = 100
    def get_health(self):
        return self.__health
    def set_health(self, value):
        if value < 0:
            print("Invalid health value")
        else:
            self.__health = value

player_1 = Player()
player_1.set_health(60)
player_1.set_health(-10)
print(player_1.get_health())
        

