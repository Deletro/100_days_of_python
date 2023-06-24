class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_list = question_list
        self.question_nr = 0

    def next_question(self):
        question = self.question_list[self.question_nr]
        self.question_nr += 1
        answer = input(f"Q.{self.question_nr}: {question.text} (True/False): ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        if self.question_nr >= len(self.question_list):
            return False
        return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong!")

        print(f"Your current score is: {self.score}\n")
