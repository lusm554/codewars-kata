# https://www.codewars.com/kata/54fe05c4762e2e3047000add/train/python

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        draft_wo_crew = self.draft - (self.crew * 1.5)
        if draft_wo_crew > 20:
            return True
        return False

# second version
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        draft_wo_crew = self.draft - (self.crew * 1.5)
        return draft_wo_crew > 20


