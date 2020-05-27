

def find_name(name,phone_book):
    for person inphone_book:
        if name == person:
            return True

name="Kim"
phone_book = ["Tim","Dan","Oliver","Kim"]

O(1 + 1)
# The reason this is O(n) is because as you add on to the list 
# the for loop will have to loop through the same amount of times, 
# refered to as linear space and time complexity.


