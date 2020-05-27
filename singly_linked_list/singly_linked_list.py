1. find first node if current is the head 
2. follow through to the next node until 
create two pointers and the first moves once at a time and the second moves 2 at a time 
once the 2nd reaches the end the first reaches the middle 



def find_middle(self):
    middle=self.head #declaring starting point basically
    end=self.head

    while end !=None:
        end = end.next
        if end !=None:
            end = end.next
            middle = middle.next

    print(middle)
    return middle