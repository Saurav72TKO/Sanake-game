# Snake Game 🐍

A simple Snake game made with Python. It has a background image, a score counter, and three sounds (background music, eating, and game over).

## What you need

- Python 3
- Two extra libraries (Tkinter comes with Python, so you don't need to install it)

Install them by running this in your terminal or command prompt:

```
pip install pygame pillow
```

## Files you need in the same folder

Put all of these together in one folder:

| File | What it is |
|------|-----------|
| `snake-game-version1.py` or `snake-game-version2.py` | The game |
| `Snake_bg.jpg` | Background image |
| `game-music.mp3` | Background music |
| `eat-food.mp3` | Sound when the snake eats |
| `game-over.mp3` | Sound when the game ends |

## How to run

1. Open a terminal in the game folder.
2. Run one of these:

```
python snake-game-version1.py
```
or
```
python snake-game-version2.py
```

(You can also open the file in Thonny and press Run. Make sure the files above are in the same folder.)

## How to play

- Use the **arrow keys** to move the snake.
- Eat the **red food** to grow and earn 1 point.
- Don't run into your own body!

## Two versions

- **Version 1:** The snake goes through the walls and comes out the other side. The game ends only if you hit yourself.
- **Version 2:** The game ends if you hit a wall or yourself.

## Problems?

- **"No module named pygame" or "No module named PIL":** run `pip install pygame pillow` again.
- **"No such file or directory":** one of the image or sound files is missing, or it is not in the same folder as the game.
