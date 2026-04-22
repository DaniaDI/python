🐾 Zoo Management System (Python OOP)
 🧠 Overview:-

   * This project is a simple Zoo Management System built using Object-Oriented Programming (OOP) in Python.

    It demonstrates the use of:

 Classes and Objects:-
    Inheritance
    Method Overriding
    Encapsulation of animal behavior

    The system simulates animals in a zoo with different attributes and behaviors.

🧩 Project Structure:-
    🔹 Animal (parent Class)

    Represents a general animal in the zoo.

  Attributes:

    name
    age
    health level
    happiness level

    Methods:

    display_info() → shows animal details
    feed() → increases health and 
    
🦁 Lion (Child Class)

    Inherits from Animal.

    Default values: age=5, health=80, happiness=80
    Overrides feed():
    Health increases by 15
    Happiness increases by 5

🐯 Tiger (Child Class)

    Inherits from Animal.

    Default values: age=6, health=60, happiness=90
    Overrides feed():
    Health increases by 10
    Happiness increases by 15

* Zoo Class:-

    Manages all animals in the zoo.

    Attributes:

    zoo name
    list of animals

    Methods:

    add_animal(animal) → adds any animal object
    add_lion(name) → adds a lion
    add_tiger(name) → adds a tiger
    print_all_info() → displays all animals information
    
💡 What I Learned:-
        -Object-Oriented Programming concepts in Python
        -How to use inheritance and method overriding
        -How to structure real-world systems using classes
        -Managing collections of objects inside another class
    
    
 👩‍💻 Author:-

    -Computer Engineering Dania | Full Stack Developer
    -Focused on backend development, OOP design, and building structured systems in Python