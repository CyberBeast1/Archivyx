"""
🎭 CLI Prompt Utilities – Archivyx

This module provides **interactive command-line prompts** using Rich & Keyboard.
It includes **vertical and horizontal selection menus** similar to interactive CLI tools.

🔹 Features:
- **Vertical selection prompts** (like menus)
- **Horizontal selection prompts** (Yes/No, Option selectors)
- **Customizable key bindings**
- **Smooth animations & real-time terminal updates**

📜 Inspired by modern CLI tools like `npm create vite`.

🛠 Example Usage:
```python
from archivyx.cli_prompts import vert_prompt, hori_prompt

choice = vert_prompt(["Option 1", "Option 2"], "🔽 Choose an option:")
print(f"You selected: {choice}")
"""

import keyboard
from rich.console import Console
from rich.live import Live
import time

console = Console()

def vert_prompt(options: list[str],prompt: str, wrap: bool = True , selectors: tuple[str,str] = ('●','○'), speed: float = 0.2, keymap: tuple[str,str,str]=("up", "down", "enter")):
    '''
    this function requires root privilages to handle low level inputs
    you can use my custom created script `rootpython`
    ```
    rootpython <python_file>.py
    ```
    '''
    time.sleep(0.15)
    index = 0  # Track selected option
    key_up, key_down, key_enter = keymap  # Custom key bindings
    def render():
        """Renders the menu with highlighting"""
        output = ""
        if prompt: output+= prompt
        selectedEmoji = selectors[0]
        NotSelectedEmoji = selectors[1]
        for i, option in enumerate(options):
            if i == index:
                output += f"[bold cyan]{selectedEmoji}[/] [bold cyan]{option}[/bold cyan]\n"  # Highlight selection
            else:
                output += f"[bold cyan]{NotSelectedEmoji}[/] [dim]{option}[/dim]\n"
        return output
    with Live(render(), refresh_per_second=100) as live:
        while True:
            key = keyboard.read_event().name

            if key == key_down:
                index = (index + 1) % len(options) if wrap else min(index + 1, len(options) - 1)
            elif key == key_up:
                index = (index - 1) % len(options) if wrap else max(index - 1, 0)
            elif key == key_enter:
                break

            live.update(render())  # Update UI
            time.sleep(speed)
    return options[index]

def hori_prompt(options: list[str],prompt: str, sep: str = ", ", bracs: int = 1, speed: float = 0.2, keymap: tuple[str,str,str] = ("left", "right", "enter")):
    '''
    this function requires root privilages to handle low level inputs
    you can use my custom created script `rootpython`
    ```
    rootpython <python_file>.py
    ```
    '''
    time.sleep(0.15) # gosh this is dumb this is for bcoz if you entered just before it registers it and not ask for options selection
    index = 0
    key_left, key_right, key_enter = keymap  # Custom key bindings
    def yesNoRender():
        """Renders the menu with highlighting"""
        output = ""
        if prompt: output+= prompt
        if bracs: output += "[bold yellow]([/]"
        for i, option in enumerate(options):
            if i == index:
                output += f"[bold yellow]{option}[/bold yellow]"  # Highlight selection
                if i != len(options)-1:
                    output += sep
            else:
                output += f"[dim]{option}[/dim]"
                if i != len(options)-1:
                    output += sep
        if bracs: output += "[bold yellow])[/]"
        return output
    # yes no prompt animate and kandle key inputs
    with Live(yesNoRender(), refresh_per_second=100) as live:
        while True:
            key = keyboard.read_event().name

            if key == key_right and index < len(options) - 1:
                index += 1
            elif key == key_left and index > 0:
                index -= 1
            elif key == key_enter:
                break  # Finalize selection

            live.update(yesNoRender())  # Update UI
            time.sleep(speed)
    return options[index]

if __name__ == "__main__":
    options = ["yes", "no"]
    choosed = vert_prompt(options, speed=0.5)
    choosed = hori_prompt(options,"Do you wanna exit:", speed=0.5,sep=", ",bracs=1)

    console.print(f"You selected: [bold cyan]{choosed}[/bold cyan]")
