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
Learn basic inheritance and how to override methods.
The starter code below provides the base Notification class.
1. Create two subclasses: EmailNotification and SMSNotification.
2. Each subclass should store the destination address/number passed
   to its constructor.
3. Override send(self) so that:
      EmailNotification prints "Sending EMAIL to <address>"
      SMSNotification prints "Sending SMS to <number>"
4. After writing the subclasses, create one of each and call send().
'''

class Notification:
    def send(self):
        print("Generic notification")

# Write your subclasses below this line
