class QuizBrain:
	def __init__(self, questions):
		self.questions = questions
		self.question_number = 0
		self.score = 0

	def still_has_questions(self):
		return len(self.questions) > self.question_number

	def check_answer(self, user_answer, question):
		if user_answer == question.answer:
			self.score += 1
			print("You got it right!")
		else:
			print("That's wrong.")
		print(f"The correct answer was: {question.answer}")
	
	def next_question(self):
		answer = input(f"Q{self.question_number + 1}. {self.questions[self.question_number].text} (True/False): ")
		self.check_answer(answer, self.questions[self.question_number])
		self.question_number += 1
		print("Your current score is: " + str(self.score) + "/" + str(self.question_number) + "\n")