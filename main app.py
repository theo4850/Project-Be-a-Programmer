print("Hello, this is the Be a programmer app, \n")
print("the first algorithm that gives the user personalised advices and recommendations \n")
print("about which path you should follow, based on the user's responses!")

def main_func():

    user_input = input("What type of developer you want to be? Please answer here: ")

    # Check the user's answer and suggest a learning path
    if user_input.lower() == "frontend":

        print("Great choice! For frontend development, you should learn HTML, CSS, and JavaScript.")
        print("For JavaScript, we recommend searching for online resources like MDN Web Docs or W3Schools to learn the basics. Then, try building simple projects like a calculator or a todo list to practice your skills.")

    elif user_input.lower() == "backend":
    
        print("Awesome! For backend development, you should learn a programming language like Python, Java, or Ruby, and also learn about databases and server-side frameworks.")
        print("For Python, we recommend starting with the book 'Automate the Boring Stuff with Python' by Al Sweigart, which is available online for free. You can also try online courses like Codecademy or Udemy to learn the basics. Once you're comfortable with Python, try learning a web framework like Flask or Django to build web applications.")
        print("For Java, we recommend starting with the book 'Head First Java' by Kathy Sierra and Bert Bates. You can also try online courses like Codecademy or Udemy to learn the basics. Once you're comfortable with Java, try learning a web framework like Spring or Struts to build web applications.")
        print("For Ruby, we recommend starting with the book 'Learn Ruby the Hard Way' by Zed Shaw. You can also try online courses like Codecademy or Udemy to learn the basics. Once you're comfortable with Ruby, try learning a web framework like Ruby on Rails to build web applications.")

    elif user_input.lower() == "fullstack":

        print("Excellent! For fullstack development, you should learn both frontend and backend technologies. Start with HTML, CSS, and JavaScript, and then move on to a programming language like Python or Ruby and a server-side framework like Flask or Ruby on Rails.")
        print("For JavaScript, we recommend searching for online resources like MDN Web Docs or W3Schools to learn the basics. Then, try building simple projects like a calculator or a todo list to practice your skills.")
        print("For Python, we recommend starting with the book 'Automate the Boring Stuff with Python' by Al Sweigart, which is available online for free. You can also try online courses like Codecademy or Udemy to learn the basics. Once you're comfortable with Python, try learning a web framework like Flask or Django to build web applications.")
        print("For Ruby, we recommend starting with the book 'Learn Ruby the Hard Way' by Zed Shaw. You can also try online courses like Codecademy or Udemy to learn the basics. Once you're comfortable with Ruby, try learning a web framework like Ruby on Rails to build web applications.")
        print("For databases, we recommend learning SQL, which is a language used to interact with databases. You can try online courses like Codecademy or Udemy to learn SQL basics.")

    else:

        print("Sorry, I didn't understand your answer. Please choose either Frontend, Backend, or Fullstack.")

main_func()