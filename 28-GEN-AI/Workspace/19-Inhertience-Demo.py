class ChatBot:

    def welcome_user(self):
        print("Welcome to Gen AI Chatbot")

    def collect_question(self, question):
        print("User Question:", question)


class CustomerSupportBot(ChatBot):

    def solve_customer_issue(self):
        print("Solving customer issue using AI")


class CourseCounsellingBot(ChatBot):

    def suggest_course(self):
        print("Suggesting best course using AI")


bot = CourseCounsellingBot()

bot.welcome_user()
bot.collect_question("Which course is best for Gen AI?")
bot.suggest_course()

print("-------------------------------")

bot = CustomerSupportBot()

bot.welcome_user()
bot.collect_question("My Outlook Not working")
bot.solve_customer_issue()