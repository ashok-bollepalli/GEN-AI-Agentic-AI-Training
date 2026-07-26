class ChatBot:
    def welcome_user(self):
        print("Welcome to ChatBot")

    def ask_question(self, question):
        print("User Question : ", question)

class CustomerSupportBot(ChatBot):
    def solve_customer_issue(self):
        print("Solving Customer issue using AI")

class CourseCounsellingBot(ChatBot):
    def suggest_course(self):
        print("Suggesting Best Course Using AI")

bot1 = CustomerSupportBot()
bot1.welcome_user()
bot1.ask_question("Why my outlookig in not working ?")
bot1.solve_customer_issue()

print("--------------------------------")

bot2 = CourseCounsellingBot()
bot2.welcome_user()
bot2.ask_question("What is the best course for me?")
bot2.suggest_course()

