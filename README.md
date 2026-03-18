# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This project is a Streamlit number guessing game where the player tries to guess a secret number within a limited number of attempts. The game provides hints after each guess and includes different difficulty levels.

The main bugs I found were:
- The game did not restart properly after all attempts were used.
- The hints were sometimes incorrect or misleading during gameplay.
- The difficulty ranges for Easy, Normal, and Hard were not set correctly.

To fix these issues, I reviewed the game state logic, corrected the hint behavior, and updated the difficulty range handling so that each mode matched its intended settings. I also tested the game after each change to make sure the fixes worked as expected.

## 📸 Demo

<img src="gamewin.png" alt="Winning Game Screenshot" />

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
