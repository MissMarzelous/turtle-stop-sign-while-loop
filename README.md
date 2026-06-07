# 🛑 Turtle Graphics — Stop Sign (WHILE Loop Version)

A Python turtle graphics program that draws an interactive stop sign using a **WHILE loop** — the user enters how many sides the shape should have, and the loop draws each side one at a time.

---

## Features

- Draws a customizable red polygon (enter number of sides at runtime)
- Writes "STOP" in large white bold text on the sign
- Draws a thick pole below the sign
- Uses a **WHILE loop** to repeat the drawing steps
- Light green canvas background for contrast

---

## How It Works

1. User is prompted for the number of sides
2. The turtle fills a red shape using a `while` loop:
   - Each iteration: move forward 100px, turn left 45°, increment counter
   - Loop ends when `count > how_many`
3. "STOP" is written in white at position (-55, 74)
4. A thick pole is drawn downward from position (50, 0)

---

## Example — 8 sides (octagon stop sign)

```
Enter the number of sides for the design:
8
```

---

## Screenshots

| Start | Finished |
|---|---|
| ![Start](start.png) | ![Finished](finished.png) |

---

## Technologies Used

- Python 3
- `turtle` — Python's built-in graphics module
- `while` loop — loop control with manual counter variable
- `fillcolor`, `begin_fill`, `end_fill` — shape filling
- `write()` — drawing text on the canvas
- `goto()` — absolute canvas positioning

---

## WHILE Loop vs FOR Loop

| Feature | WHILE Loop (this project) | FOR Loop |
|---|---|---|
| Loop structure | `while count <= how_many` | `for count in range(1, how_many+1, 1)` |
| Counter management | Manual (`count = count + 1`) | Automatic (range handles it) |
| Same visual result | ✅ Yes | ✅ Yes |

> See the companion repo `A4-FOR-Loop-Design` for the FOR loop version of this same design.

---

## Learning Outcomes

- WHILE loop syntax and structure
- Loop control variables (initialize → condition → update)
- Turtle graphics with user input
- Drawing filled shapes with `begin_fill` / `end_fill`
- Writing text and drawing compound designs (sign + pole)

---

## How to Run

1. Make sure Python 3 is installed: https://www.python.org/downloads/
2. Clone or download this repo
3. Open a terminal in the repo folder
4. Run: `python turtle_stop_sign_while.py`
5. Enter a number of sides when prompted (try **8** for a classic stop sign shape)

---

## Folder Structure

```
turtle-stop-sign-while-loop/
├── turtle_stop_sign_while.py
├── start.png
├── finished.png
├── README.md
├── LICENSE
└── .gitignore
```

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

*Written by Marlena Fabrick — Computer Programming, Fall 2020*
