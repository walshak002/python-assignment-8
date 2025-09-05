"""
TASK: Create a VotingSystem class.

Requirements:
1. The class should allow registering candidates.
2. Each candidate should start with 0 votes.
3. The class should allow voters (using voter IDs) to cast votes.
   - Ensure one voter cannot vote more than once.
4. Provide a method to display election results.

Example Usage:
    election = VotingSystem()
    election.register_candidate("Alice")
    election.register_candidate("Bob")
    election.vote("Voter1", "Alice")
    election.vote("Voter2", "Bob")
    election.vote("Voter3", "Alice")
    print(election.results())  # {"Alice": 2, "Bob": 1}
    print(election.winner()) # Alice
"""

class VotingSystem:
    def __init__(self):
        self.candidate = {}
        self.voters = {}
    def register_candidate(self, name):
        if name in self.candidate:
            print(f"Candidate {name} already registered")
        else:
            self.candidate[name] = 0
            print(f"Candidate {name} register successfully")
    


election = VotingSystem()
election.register_candidate("Alice")
election.register_candidate("Bob")