import pyperclip
import time
import openai
import os
import pyautogui


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    pyperclip.copy("")

    while True:
        print("Waiting for clipboard...")
        clipboard = wait_for_clipboard()
        print("Found clipboard: " + clipboard)

        if clipboard[:7] != "askgpt ":
            print("Invalid prefix")
            continue

        prompt = clipboard[7:]

        if prompt == "":
            print("Invalid prompt")
            continue

        pyautogui.press("right")
        print("Waiting for response...")
        
        history = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        res = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=history
        )

        pyperclip.copy(res.choices[0].message.content)
        pyautogui.hotkey("ctrl", "v")
        print(res.choices[0].message.content)


def wait_for_clipboard():
    last_clipboard = pyperclip.paste()

    while True:
        if pyperclip.paste() != last_clipboard:
            return pyperclip.paste()
        
        time.sleep(1)


def debug():
    test = "Hello, world!"

    print(test[3:])
    exit()


if __name__ == "__main__":
    main()