# Pizza Game  
**ICS3U Final Project – Shayaan Shaikh – June 19, 2025**  

A simple arcade-style game built with Python (Tkinter) where you control a character to catch pizzas.  
Good pizzas earn you points, while burnt pizzas will cost you points. Stay above zero points to keep playing!  

---

## How to Play  
- **Controls:**  
  - Left / Right arrows → Move horizontally  
  - Up / Down arrows → Move vertically  

- **Objective:**  
  - Catch good pizzas (red) to gain points.  
  - Avoid bad pizzas (black) or you will lose points.  
  - Your score must stay above 0 to continue.  
  - Game ends when your score drops below 0.  

- **Rounds:**  
  - Two rounds per playthrough.  
  - Select Easy, Mid, or Hard Mode at the start screen:  
    - Easy: 5 pizzas falling  
    - Mid: 10 pizzas falling  
    - Hard: 15 pizzas falling  

---

## Screens & Features  
- Start Screen: Choose difficulty and view instructions.  
- Gameplay:  
  - Random falling pizzas with different speeds.  
  - Moving character image (`man.png`) that you control.  
  - Background with a road and randomized sun position.  
- End Screen: Replay or quit when game over.  

---

## Requirements  
- Python 3.8+  
- Tkinter (comes pre-installed with Python)  
- Image asset:  
  - `man.png` (player sprite)  

---

## How to Run  
1. Clone or download this repository.  
2. Make sure `man.png` is in the same folder as the Python file.  
3. Run the game:  
   ```bash
   python pizza_game.py
