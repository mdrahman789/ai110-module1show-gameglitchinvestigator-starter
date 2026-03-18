# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- **Restart Function Issue**  
  - **Expected**: The game should fully restart with a fresh state after all attempts are used and the player chooses to play again.  
  - **Actual**: The game does not reset properly and continues with leftover data from the previous round.

- **Incorrect Hint System**  
  - **Expected**: The hints should accurately reflect the relationship between the player’s guess and the correct answer.  
  - **Actual**: The game sometimes provides incorrect or misleading hints during gameplay.

- **Difficulty Range Issue**  
  - **Expected**: Each difficulty mode (Easy, Normal, Hard) should have its correct number range.  
  - **Actual**: The ranges are not set correctly, causing the difficulty levels to behave incorrectly.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT and the AI built into Cursor as my main tools for this project. A correct suggestion from AI was that the restart bug came from the game state not being fully reset, especially things like attempts, status, and history. I verified this by playing until I lost all my attempts, clicking “New Game,” and checking that those values actually reset and the game started a clean round. A misleading suggestion was about the hint logic, where AI initially made it sound like the problem was only about comparing the guess and the secret. When I watched the hints during real gameplay and looked more closely at the logic structure, I saw that the issue was also about how the conditions were organized, not just a single comparison.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by running the game again and checking if the behavior now matched what I expected, instead of just trusting the code changes. For example, I tested restarting after using all attempts to confirm that the secret, attempts, and game status all reset while the score stayed consistent. I also checked the hints during gameplay by intentionally guessing too low, too high, and exactly right and seeing whether the messages lined up with those guesses. AI helped by pointing out which parts of the code controlled restart and hint behavior and suggesting simple tests I could run, both manually in the app and with pytest.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit basically reruns the whole script from top to bottom every time the user interacts with the app, like pressing a button or entering a guess. If we didn’t do anything special, that would mean all our variables reset on every click. Session state is Streamlit’s way of remembering important values, like the current secret number, the number of attempts, and the game status, across those reruns. By storing things in `st.session_state`, the game can feel continuous to the player even though the script is starting over in the background each time.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is fixing one bug at a time and testing right away instead of piling up a bunch of changes and hoping they all work. Next time I work with AI, I want to be more specific with my prompts and then immediately verify each suggestion in the running app or with tests. This project made me see AI-generated code as something useful but not automatic truth. AI is a helpful teammate for ideas and guidance, but I still have to double‑check everything and make sure the final behavior actually matches what I want.
