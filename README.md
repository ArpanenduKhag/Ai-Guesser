# 🎯 AI Number Guesser

A fun **Python GUI game** where the computer tries to guess the number you are thinking of!  
This app uses a **binary search algorithm** to guess your number between 1 and 100, built with **Tkinter**.

---

## 📌 Features
- 🧠 **AI-powered guessing** using binary search.
- 🎨 **Simple GUI** with Tkinter.
- 🔄 Restart anytime.
- 📈 Efficient guessing — the AI will find your number in at most **7 tries**.

---

## 🛠 Requirements
- Python 3.x  
- Tkinter (comes pre-installed with Python on most systems)

---

## 🚀 How to Run
1. **Clone or Download** this repository.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python ai_guesser.py
   ```
4. Think of a number between **1 and 100**.
5. Use the buttons:
   - **Higher** → if your number is greater than the guess.
   - **Lower** → if your number is smaller than the guess.
   - **Correct** → when the AI guesses your number.
6. Click **Restart** to play again.

---

## 📚 How It Works
The AI starts with the full range (1–100) and repeatedly guesses the middle value:
1. If you click **Higher**, the lower bound increases.
2. If you click **Lower**, the upper bound decreases.
3. This continues until the AI finds your number.

---

## 🏗 Future Improvements
- Add **custom range** selection.
- Track **number of guesses taken**.
- Implement **difficulty levels**.


---
💡 *Enjoy playing and see how quickly the AI can guess your number!*
