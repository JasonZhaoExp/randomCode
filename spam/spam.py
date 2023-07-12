import time
import pyautogui

def send_text(text):
    pyautogui.typewrite(text)
    pyautogui.press('enter')

def main():
    file_name = "spam.txt"
    messages_sent = 0

    with open(file_name, 'r') as file:
        lines = file.readlines()

    start_time = time.time()  # Record the start time

    time.sleep(5)

    for line in lines:
        send_text(line.strip())
        messages_sent += 1

    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time - 5  # Calculate the execution time in seconds

    print("Execution time:", execution_time, "seconds")
    print("Number of messages sent:", messages_sent)

if __name__ == '__main__':
    main()
