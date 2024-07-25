from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_question = Question(question_text, question_answer) #object Class Question()
    question_bank.append(new_question)



#print(len(question_bank))

quiz = QuizBrain(question_bank) #initializing QuizBrain object with list of questions
# quiz.next_question()
#
# print(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!")
print(f"Your final score was {quiz.score} out of {quiz.question_number}.")

#JSON is JavaScript object notation
#object oriented programming