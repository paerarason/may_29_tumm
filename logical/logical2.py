class Eletion:
    def __init__(self,candidates) -> None:
        self.candidates={}
        for i in candidates:
             self.candidates[i]=0
    
    def voting(self,candiate):
        if self.candidates.has_key(candiate):
            self.candidates[candiate]+=1
            return True
        return False
    
    def print_winner(self):
            max_vote=0
            winners={}
            for vote in self.candidates.values():
                 max_vote=max(vote,max_vote)
            for vote,candidate in self.candidates.items():
                 if max_vote==vote:
                      winners[candidate]=vote
            return winners
                 
#initialize the class at bottom and add the candidate name as list to the Constructor 
# constructor will initilaize the  dictionary with 0 as  default vote 
