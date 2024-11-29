# Matrix-based Battleship Game Assignment

## Overview

In this assignment, you will implement a **text-based Battleship game** in Python, where players take turns to guess the location of their opponent’s ships on two 5x5 grids. The game will also allow players to place their own ships on their own board, adding a layer of strategy.

You will implement two main modes of play:
- **Single Player**: You will play against the computer.
- **Multiplayer**: Two players can take turns playing against each other.

The game will feature **turn-based gameplay**. If a player successfully hits a ship, they will get **another turn**. If they miss, the turn will switch to the opponent.

---

## Game Rules

### 1. Board Setup
- The game board of each player is represented by a **5x5 matrix** (grid).
- Initially, each position on the grid is filled with `0` (water), and ships will be placed on the board using `1` to indicate the ship's location.
  
### 2. Ships
- Each player (either human or computer) has **three ships** to place:
  - A **large ship** of size **4**.
  - A **medium ship** of size **3**.
  - A **small ship** of size **2**.
- Ships can be placed **horizontally** or **vertically** on the grid.

### 3. Gameplay
- Players take turns to **guess** the opponent’s ship locations.
- If a guess hits a ship, the player will get **another turn** to continue guessing.
- If a guess is a miss, the turn changes to the opponent.
  
### 4. Ending the Game
- The game ends when one player successfully sinks **all** of the opponent’s ships.
- The winner is the player who sinks all of the opponent’s ships first.

---

## How to Play

### 1. Game Setup
- At the beginning of the game, the player will choose between **Single Player** or **Multiplayer** mode:
  - **Single Player**: You will play against the computer.
  - **Multiplayer**: Two players will take turns guessing the opponent’s ship locations.

### 2. Ship Placement
- Each player must place their ships on the grid.
  - The player will place ships of sizes **4**, **3**, and **2**.
  - For each ship, the player will provide:
    - The **starting row and column** for the ship.
    - The **direction** (either "horizontal" or "vertical") for placing the ship.
  - Ensure that ships do not **overlap** and stay within the **grid boundaries**.

### 3. Taking Turns
- Players take turns guessing the coordinates of their opponent's ships.
  - For example, you would input a guess such as `(row: 3, column: 2)`.
  - If the guess is **correct (hit)**, the player gets **another turn**.
  - If the guess is **incorrect (miss)**, the turn switches to the opponent.
  
### 4. Winning the Game
- The game continues until one player has successfully sunk all the opponent’s ships.
- The player who sinks all the ships first is declared the **winner**.

---

## Steps to Implement the Game

### 1. Create the Game Board
- The game board will be one **5x5 grid** (a 2D list in Python) for each player, initially filled with zeros (`0`).
- The ships will be placed in this grid, and their locations will be marked with `1` when placed.

### 2. Ship Placement
- The player will place each of their three ships (of sizes 4, 3, and 2) by specifying the starting position and direction.
  - **Horizontal** ships will occupy consecutive columns in the same row.
  - **Vertical** ships will occupy consecutive rows in the same column.
- The player cannot place ships **outside the grid** or overlap existing ships.

### 3. Opponent Ship Placement (Single Player Mode)
- In **Single Player** mode, the opponent's ships will be placed **randomly**.
  - The opponent's ships should not overlap or go out of bounds of the grid.

### 4. Player Input
- Players will input their guesses in the form of **row** and **column** numbers (from 1 to 5).
- The system will check whether the guessed location is a hit or a miss and return the appropriate response.

### 5. Game Loop
- The game will alternate between the two players, allowing each player to guess the location of the opponent's ships.
- If a ship is hit, the player will get an extra turn.
- If a player misses, the turn will switch to the opponent.

---

## Example Game Flow

### 1. Game Start
The game will first prompt the user to select between **Single Player** or **Multiplayer**.

```
Welcome to Battleship!

Choose game mode:

1. singleplayer
2. multiplayer

> 1
```

### 2. Ship Placement
After selecting the game mode, players will be prompted to place their ships one by one. For each ship, the player will need to provide:
- The **starting row and column** for the ship.
- The **direction** (horizontal or vertical).

```
Place your large ship (size 4)
Enter the starting row and column: 
> 2 3 
Enter direction (horizontal/vertical): 
> horizontal
```

This process is repeated for the medium (size 3) and small (size 2) ships.

### 3. Taking Turns
Once the ships are placed, players will take turns guessing coordinates.

```
Enter your guess (row 1-5, column 1-5):
> 3 2
Hit! (You hit an opponent's ship)
```
If a player hits a ship, they are allowed to take another guess. By each hit, that part of ship will be destroyed.

```
Enter your guess (row 1-5, column 1-5):
> 4 4 
Miss! (No ship at this location)
```

The game continues, alternating turns until all ships of one player are sunk.

### 4. Game End
The game ends when all of a player's ships have been sunk. The winner is the player who sinks all of their opponent's ships first.

```
Congratulations! You have sunk all the opponent’s ships! You win!
```

---

## Challenge Extensions (Optional)

After completing the basic game, you can add the following features to enhance the game:

1. **AI for Single Player**:
   - The computer’s moves can be made more strategic, targeting areas around previously hit ships.

2. **Multiple Grid Sizes**:
   - Allow the player to choose the size of the grid (e.g., 6x6, 10x10) and adjust the number of ships accordingly.

3. **Advanced Multiplayer**:
   - Create a server-client architecture to allow two players to play remotely over the internet.

4. **Ship Health**:
   - Instead of instantly removing a part of ship when it is hit, track the health of each ship and display the health of ship too.

---

## Submission Instructions

1. Implement the **Battleship game** as described in this README.
2. Submit your **Python file** (`battleship.py`) containing the completed game logic.
3. If you have added any extra features or enhancements, include those as well.
4. Ensure that your code is **well-commented**, clearly explaining your approach and logic.

---

## Grading Criteria

Your assignment will be graded based on the following criteria:
- Correct implementation of the **game rules** (ship placement, guessing, turn-based system, etc.).
- User interaction: Clear and appropriate **input prompts** and responses (hits, misses).
- Correct handling of **edge cases** (e.g., invalid input, ship overlap, grid boundaries).
- **Code readability**: Well-commented code with appropriate variable names and structure.
- Bonus points for adding **extra features** like AI, multiple grid sizes, or advanced multiplayer.

---

## Conclusion

This assignment will help you develop a deeper understanding of **matrix manipulation** in Python, improve your ability to manage **game logic**, and enhance your skills with **conditional checks** and **loops**. It’s a fun way to learn programming while building a classic game like Battleship.

Good luck, and enjoy coding!
