# 🎩 Hat Probability Calculator

This project simulates drawing balls of different colors from a hat and estimates the **probability** of drawing a desired combination.

It was built as part of my **Scientific Computing with Python Certification** to practice simulation and randomness in Python.
👉 [View my certification here](https://freecodecamp.org/certification/lucawaldvogel/scientific-computing-with-python-v7)

---

## ✨ Features
- 🎩 **Hat class**
  - Initialize with any number of colored balls (`Hat(red=3, blue=2, green=5)`)
  - Reset and draw a given number of balls at random
  - Handles cases where more balls are drawn than available
- 🧪 **Experiment function**
  - Runs repeated random draws
  - Checks how often the drawn sample matches the expected outcome
  - Returns the **empirical probability**  

---

## 📖 Example Usage

```python
hat = Hat(black=6, red=4, green=3)

# Draw 5 random balls
print(hat.draw(5))
# e.g. ['red', 'green', 'black', 'black', 'red']

# Run experiment
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)
# ~0.35 (varies due to randomness)
```

---

## ⚙️ How It Works

# 1. Hat Initialization
Creates a "hat" filled with the specified numbers of balls of each color.
```python
hat = Hat(black=6, red=4, green=3)
# hat.contents = ['black','black',...,'red','red',...,'green','green',...]
```

# 2. Draw
Removes a specified number of random balls from the hat (without replacement).

# 3. Experiment
Repeats the draw process a given number of times and measures how often the desired set of balls was drawn.
