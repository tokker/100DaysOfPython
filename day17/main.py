from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []

for q in question_data:
	questions.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(questions)

while quiz.still_has_questions():
	quiz.next_question()

print("You've completed the quiz, your final score is: " + str(quiz.score) + "/" + str(quiz.question_number))
