# 🎯 Great Number Game

## Overview

A simple Flask web app where users guess a random number between 1 and 100.

## Features

* Random number generation
* Feedback: Too High / Too Low / Correct
* Attempts counter
* Max 5 attempts (lose condition)
* play again 
 
 
## 🔗 Routes

### '/' (Home)

* Initializes the game (random number, attempts, game state)
* Displays the main page and result message

 

### '/guess' (POST)

* Handles user input (number guess)
* Compares guess with the correct number
* Updates result (Too High / Too Low / Correct)
* Increments attempts
* Checks win/lose conditions

 
### '/restart'

* Clears the session
* Starts a new game

## Author

Dania Isead
