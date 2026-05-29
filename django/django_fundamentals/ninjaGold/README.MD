# 🥷 Django Ninja Gold Game

An interactive, web-based mini-game built using the **Django** framework. Players control a ninja exploring various locations to accumulate gold, utilizing Django Sessions to manage the game state, track movements, and log activities securely.

---

## 🚀 Features

### 1. Core Game Logic
* Players can visit four unique locations: **Farm**, **Cave**, **House**, and **Casino**.
* Each location yields a different range of gold (positive or negative).
 * **Farm:** Earns 10 - 20 gold.
  * **Cave:** Earns 5 - 10 gold.
  * **House:** Earns 2 - 5 gold.
  * **Casino:** Earns or Loses up to 50 gold (`-50` to `50`).
* All actions are logged in real-time within an interactive activity log box.

### 2.(Dynamic URLs)=>/process_money/str:building/
*like:`<form action="/process_money/cave/" method="post">`
* Completely eliminated the hidden form inputs (`<input type="hidden">`).
* Routes are processed dynamically through the URL structure using Django paths:

### 3. Custom Game Conditions
* Added a dedicated **Setup Page** before the game begins.
* Allows the user to dynamically set their own winning conditions:
* **Target Gold Goal** (e.g 500 gold)
* **Maximum Allowed Moves** (e.g 20 moves)

* Real-time validation checks after every move to determine:
* **Win:** Reaching the target gold within the allowed moves.
* **Lose:** Running out of moves before hitting the target, or going bankrupt (gold < 0).

---

## 🛠️ Technologies Used

* **Backend:** Python 3.x, Django Framework
* **Frontend:** HTML5, CSS3 (Flexbox layout), Django Template Language (DTL), Bootstrap 5
* **Security & Filters:** Django CSRF Protection Tokens & DTL `safe` filters for secure backend-rendered HTML.

---
 Author
  Dania Isead 
