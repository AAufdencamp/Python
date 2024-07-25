class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


#these two attributes should be initialized with a value when a new question object is created from this class.

#if we want to create an attribute, we have to use this syntax, self. and then the name of the attribute,
#because eventually when we create a new object from this class say a new question object, then we're going
# to be passing in these two items, a piece of text which is going to be the question, and then either true or false
# as the answer. And then later on if we wanted to access the text, then we would say new_q.text.
#example:
#new_q = Question("saffa", "False")
#new_q.text

# new_q = Question("Red and Blue are complimentary colors?", "False")
# print(new_q.text)
# print(new_q.answer)