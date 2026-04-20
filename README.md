# Pay to Paint Project

## Overview
Pay to Paint is a spin off of "Color by Numbers" that I made for my 15-112 CMU CS class.
In the game, players earn coins to purchase paints and power-ups, and complete 3 color by numbers pictures: a present, a flower, and a tree.

---

## Features

## Play Screen
- In order to gain coins, players play a minigame
- Use the left and right arrow keys to move your basket and catch the coins
- Beware of the bombs! Catch 3 and the minigame ends.

## Shop Screen
- Players use arrow keys to navigate between different shop pages.
- Coins can be used to purchase paints and minigame power-ups.
- Once an item is purchased, it is marked with an “X” to indicate it is no longer available.

---

## Color Screen
- Colors are initially locked and displayed with a lock icon.
- Players unlock colors through gaining coins and buying paints in the shop.
- Clicking an unlocked color highlights all matching cells on the board.
- Players can click and hold, moving their mouse to fill up all of the cells of the correct color.
- Once a color is fully used, its label disappears.
- Completing a picture updates the home screen preview.
- After all three pictures are completed, the game transitions to a final conclusion screen.

---

## Grading Shortcuts

These shortcuts are included to simplify testing:

- Press **`c`** → Gain 500 coins instantly
- Press **`1`** → Automatically complete Picture 1
- Press **`2`** → Automatically complete Picture 2
- Press **`3`** → Automatically complete Picture 3

Each completion shortcut:
- Updates the home screen image
- Grays out completed colors
- Marks purchased paints as used for that picture

---

## How to Run

1. Clone the repository: git clone https://github.com/shreyam79/Pay-to-Paint-Project.git
2. Navigate into the folder: cd Pay-to-Paint-Project
3. Run the game: py main.py
