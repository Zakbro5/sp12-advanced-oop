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
This problem explores composition, where one object creates and owns another.
1. Create a Battery class that stores charge_percent (0–100).
2. Create a Robot class whose __init__ method creates its own Battery
   object starting at 100% and stores it in self.battery.
3. Add a check_power(self) method that returns a string such as:
   "Battery at 100% — ready for action!"
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

class Battery:
    def __init__(self, charge_percent=100):
        self.charge_percent = charge_percent

class Robot:
    def __init__(self):
        self.battery = Battery()
    def check_power(self):
        return f"Battery at {self.battery.charge_percent}% — ready for action!"

bot = Robot()
print(bot.check_power())
