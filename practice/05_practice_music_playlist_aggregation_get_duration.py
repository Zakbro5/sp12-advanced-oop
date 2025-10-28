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
Another look at aggregation, collecting independent objects.
1. Create a Track class storing title and duration_seconds.
2. Create a Playlist class that keeps a list of Track objects.
3. add_track(self, track) appends a Track to the list.
4. total_duration(self) loops through tracks (no list comprehension)
   to sum seconds, then returns the result as minutes:seconds text.
5. Make three tracks, add them, then print total_duration().
'''

class Track:
    def __init__(self, title, duration_seconds):
        self.title = title
        self.duration_seconds = duration_seconds

class Playlist:
    def __init__(self):
        self.tracks = []
    def add_track(self, track):
        self.tracks.append(track)
    def total_duration(self):
        total = 0
        for t in self.tracks:
            total += t.duration_seconds
            minutes = total // 60
            seconds = total % 60
            return f"{minutes}:{seconds}"
        
play_list = Playlist()
track_1 = Track("Song 1", 230)
track_2 = Track("Song 2", 156)
track_3 = Track("Song 3", 190)

play_list.add_track(track_1)
play_list.add_track(track_2)
play_list.add_track(track_3)
print("Total Duration:", play_list.total_duration())