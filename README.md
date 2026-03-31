# Sweet Danger 🍬💀

**Sweet Danger** is a two-player (or single-player vs computer) terminal-based game where players take turns eating sweets while avoiding the poisonous ones. Choose your character, pick poisoned sweets secretly, and test your luck and strategy!

---

## 🎮 Game Features

- Two-player mode or single-player vs computer 🤖  
- Interactive terminal gameplay with emojis as characters  
- Secret selection of poisonous sweets by each player  
- Turn-based eating of sweets, tracking lives for each player  
- Three lives per player, game ends when one loses all lives  
- Option to replay after a game  

---

## 🕹 How to Play

1. Run the game in a terminal that supports Python 3.  
2. Press Enter to start the game and see the title screen.  
3. Choose your character (emoji) for Player 1 and Player 2.  
4. Decide if Player 2 is human or computer.  
5. Each player secretly selects 3 poisonous sweets from the table.  
6. Players take turns picking a sweet to eat:
   - If the sweet is safe → nothing happens  
   - If the sweet is poisoned by the opponent → lose 1 life  
7. The first player to lose all 3 lives loses the game.  
8. After the game ends, choose to replay or quit.  

---

## ⚡ Controls

- Enter the **number** of the sweet you want to eat.  
- Follow prompts for poison selection.  
- Input **‘h’** for human or **‘c’** for computer when choosing Player 2.  

---

## 🛠 Technologies Used

- Python 3  
- Terminal / Command Line Interface  
- `os` and `time` libraries for clearing the screen and delays  

---

## 🎯 Learning Outcomes

This project helped me to:

- Build an interactive terminal game using Python  
- Handle player input and validation  
- Implement turn-based mechanics and game logic  
- Manage game state (lives, sweets, poison selection)  
- Design a fun, engaging user experience in the terminal  

---

## 📂 How to Run

1. Clone or download this repository:  
git clone https://github.com/anellenkosii/sweet-danger.git


2. Navigate to the project directory:
cd sweet-danger


3. Run the game:
python sweet_danger.py
