import json
import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def register_user(users):
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists! Try another.")
        return
    password = input("Choose a password: ")
    users[username] = password
    save_users(users)
    print("Registration successful!")

def login_user(users):
    username = input("Username: ")
    password = input("Password: ")
    if users.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials. Please try again.")
        return None

def show_result(score, total_questions):
    print(f"Your final score is: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"You scored: {percentage:.2f}%")
    
    if percentage == 100:
        print("Perfect score!")
    elif percentage >= 75:
        print("Well done!")
    elif percentage >= 50:
        print("A little more practice will help.")
    else:
        print("Keep trying! Don't give up.")

def run_quiz(questions):
    # Randomly select 5 questions from the list
    selected_questions = random.sample(questions, 5)
    score = 0
    for question in selected_questions:
        print(question.prompt)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == question.answer.lower():
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {question.answer}\n")
    
    show_result(score, len(selected_questions))

def main():
    users = load_users()

    # Define questions for different subjects
    dbms_questions = [
        Question("What does DBMS stand for?\n(a) DataBase Management System\n(b) Data Model System\n(c) Database Multiple System\n", "a"),
        Question("Which of these is a type of DBMS model?\n(a) Hierarchical\n(b) Linear\n(c) Static\n", "a"),
        Question("Which SQL command is used to retrieve data from a table?\n(a) SELECT\n(b) INSERT\n(c) UPDATE\n", "a"),
        Question("Which of these is a type of normalization?\n(a) First Normal Form\n(b) Second Normal Form\n(c) Both\n", "c"),
        Question("Which of the following is a type of join in SQL?\n(a) Left Join\n(b) Right Join\n(c) Both\n", "c"),
        Question("What is the primary purpose of a DBMS?\n(a) To store data\n(b) To manage hardware\n(c) To manage databases\n", "c"),
        Question("Which of these is an example of a relational DBMS?\n(a) MySQL\n(b) MongoDB\n(c) Hadoop\n", "a"),
        Question("Which of the following is not a DBMS operation?\n(a) Insertion\n(b) Deletion\n(c) Printing\n", "c"),
        Question("Which command is used to modify existing records in a database?\n(a) UPDATE\n(b) MODIFY\n(c) CHANGE\n", "a"),
        Question("What is a foreign key in DBMS?\n(a) A key that uniquely identifies records\n(b) A key used to establish relationships between tables\n(c) A key for indexing data\n", "b")
    ]
    
    oops_questions = [
        Question("What does OOPs stand for?\n(a) Object-Oriented Programming\n(b) Object-Oriented Process\n(c) Operator-Oriented Programming\n", "a"),
        Question("Which of these is not a core concept of OOPs?\n(a) Encapsulation\n(b) Abstraction\n(c) Compilation\n", "c"),
        Question("Which OOP concept is used to hide the internal details of an object?\n(a) Encapsulation\n(b) Polymorphism\n(c) Inheritance\n", "a"),
        Question("Which OOP concept allows methods to have the same name but different parameters?\n(a) Encapsulation\n(b) Polymorphism\n(c) Overloading\n", "c"),
        Question("Which OOP concept allows one class to inherit the properties of another class?\n(a) Encapsulation\n(b) Polymorphism\n(c) Inheritance\n", "c"),
        Question("Which of these is used to achieve abstraction in Java?\n(a) Interface\n(b) Class\n(c) Method\n", "a"),
        Question("Which is not a type of polymorphism?\n(a) Compile-time\n(b) Run-time\n(c) Pre-time\n", "c"),
        Question("Which OOP concept allows objects to take on multiple forms?\n(a) Abstraction\n(b) Polymorphism\n(c) Encapsulation\n", "b"),
        Question("Which keyword is used to create a new object in Java?\n(a) new\n(b) this\n(c) create\n", "a"),
        Question("Which of these is an access modifier in Java?\n(a) public\n(b) visible\n(c) accessible\n", "a")
    ]
    
    data_structure_questions = [
        Question("Which of the following is a linear data structure?\n(a) Stack\n(b) Tree\n(c) Graph\n", "a"),
        Question("Which sorting algorithm has the best average case time complexity?\n(a) Bubble Sort\n(b) Merge Sort\n(c) Quick Sort\n", "b"),
        Question("What does a hash table store?\n(a) Keys and Values\n(b) Only Values\n(c) Only Keys\n", "a"),
        Question("Which data structure is used in Depth First Search (DFS)?\n(a) Stack\n(b) Queue\n(c) Tree\n", "a"),
        Question("Which is not a type of linked list?\n(a) Doubly Linked List\n(b) Singly Linked List\n(c) Triply Linked List\n", "c"),
        Question("Which of the following is a characteristic of a queue?\n(a) First In, First Out (FIFO)\n(b) Last In, First Out (LIFO)\n(c) Random Access\n", "a"),
        Question("Which data structure uses nodes and pointers?\n(a) Stack\n(b) Linked List\n(c) Array\n", "b"),
        Question("Which operation is not performed on a tree data structure?\n(a) Insert\n(b) Delete\n(c) Sort\n", "c"),
        Question("Which algorithm is used to find the shortest path in a graph?\n(a) Dijkstra's\n(b) QuickSort\n(c) Merge Sort\n", "a"),
        Question("Which data structure is used for breadth-first search (BFS)?\n(a) Stack\n(b) Queue\n(c) Tree\n", "b")
    ]
    
    os_questions = [
        Question("What does OS stand for?\n(a) Operating System\n(b) Optical Sensor\n(c) Open Source\n", "a"),
        Question("Which of these is an example of an OS?\n(a) Windows\n(b) Google\n(c) Facebook\n", "a"),
        Question("What is the main function of an operating system?\n(a) Manage hardware resources\n(b) Store data\n(c) Provide internet access\n", "a"),
        Question("Which of these is a type of OS?\n(a) Embedded OS\n(b) Free OS\n(c) Internet OS\n", "a"),
        Question("Which system call is used to create a new process?\n(a) fork()\n(b) exec()\n(c) open()\n", "a"),
        Question("Which OS is open-source?\n(a) Windows\n(b) Linux\n(c) macOS\n", "b"),
        Question("Which of these is a process scheduling algorithm?\n(a) FIFO\n(b) LIFO\n(c) Both\n", "a"),
        Question("What does virtual memory allow?\n(a) It allows programs to use more memory than physically available\n(b) It reduces the size of memory\n(c) It prevents memory fragmentation\n", "a"),
        Question("Which of these is an example of a batch OS?\n(a) UNIX\n(b) MS-DOS\n(c) Windows\n", "b"),
        Question("What is the purpose of a kernel in an operating system?\n(a) Manage hardware\n(b) Manage software\n(c) Manage input/output operations\n", "a")
    ]
    
    # Combine all questions
    all_questions = {
        "DBMS": dbms_questions,
        "OOPs": oops_questions,
        "Data Structures": data_structure_questions,
        "Operating Systems": os_questions
    }

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            register_user(users)
        elif choice == '2':
            username = login_user(users)
            if username:
                while True:
                    print("\nChoose a subject:")
                    print("1. DBMS")
                    print("2. OOPs")
                    print("3. Data Structures")
                    print("4. Operating Systems")
                    print("5. Exit")
                    subject_choice = input("Enter choice: ")
                    
                    if subject_choice == '5':
                        break
                    subjects = {
                        '1': "DBMS",
                        '2': "OOPs",
                        '3': "Data Structures",
                        '4': "Operating Systems"
                    }
                    
                    subject_name = subjects.get(subject_choice)
                    if subject_name:
                        print(f"\nStarting quiz for {subject_name}")
                        run_quiz(all_questions[subject_name])
                        exit_choice = input("Would you like to exit the quiz or go back to subject selection? (exit/go back): ").strip().lower()
                        if exit_choice == 'exit':
                            break
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
