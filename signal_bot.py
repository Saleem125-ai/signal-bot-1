import random
import time
from datetime import datetime

# Signal generator with approx 80% accuracy simulation
class SignalBot:
    def __init__(self, accuracy=0.8):
        self.accuracy = accuracy

    def generate_signal(self):
        # Randomly decide the correct signal: 'CALL' or 'PUT'
        correct_signal = random.choice(['CALL', 'PUT'])
        # Simulate if the bot's prediction is correct based on accuracy
        is_correct = random.random() < self.accuracy
        # If correct, signal = correct_signal, else opposite
        signal = correct_signal if is_correct else ('PUT' if correct_signal == 'CALL' else 'CALL')
        return signal, is_correct

def main():
    bot = SignalBot(accuracy=0.8)
    print("Starting signal bot... Press Ctrl+C to stop.")
    try:
        while True:
            pair = "BTC/USD OTC"  # You can modify or randomize this
            signal, is_correct = bot.generate_signal()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            accuracy_percent = "80%" if is_correct else "20%"
            print(f"{now} | Pair: {pair} | Signal: {signal} | Expected accuracy: {accuracy_percent}")
            time.sleep(5)  # Wait 5 seconds before next signal
    except KeyboardInterrupt:
        print("\nBot stopped by user.")

if __name__ == "__main__":
    main()
