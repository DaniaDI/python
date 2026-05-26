# 🏆 Django Guessing Game 

A fun, interactive web-based number guessing game built using the **Django** framework. The application utilizes Django Sessions to manage game states, track user attempts, and maintain a persistence-free leaderboard for winners.

---

## 🚀 Features

* **Random Number Generation:** Automatically picks a secret number between 1 and 100 for each new game session.
* **Dynamic Feedback:** Gives the user immediate hints (`Too High` or `Too Low`) after each guess with Bootstrap-styled alerts.
* **Sensei Limit:** Restricts the user to a maximum of **5 attempts**. If they fail on the 5th try, a "You Lose" screen appears.
* **Winner's Leaderboard:** If the user wins, they can submit their name. The game records and sorts the winners based on the minimum number of attempts (Ascending Order).
* **Smart Reset:** The "Play Again" functionality resets the game data (attempts, results, secret number) while **safely preserving** the leaderboard scores.

---

## 🛠️ Technologies Used

* **Backend:** Python 3.x, Django Framework
* **Frontend:** HTML5, Jinja/Django Template Language, Bootstrap 5 
* **State Management:** Django Sessions (Session Middleware)

👤 Author
  Dania Isead 



