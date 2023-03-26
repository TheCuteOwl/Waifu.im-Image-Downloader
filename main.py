import requests
import json
import sys
import subprocess
import time
import os
import colorama
from colorama import init, Fore
import shutil, subprocess
colorama.init()
Yellow = Fore.YELLOW
Reset = Fore.RESET
def print_centered(text):
    console_width, _ = shutil.get_terminal_size()
    padding = (console_width - len(text)) // 2
    print(' ' * padding + text)

def input_centered(prompt):
    console_width, _ = shutil.get_terminal_size()
    prompt_lines = prompt.split('\n')
    padding = (console_width - max(len(line) for line in prompt_lines)) // 2
    centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
    user_input = input(centered_prompt)
    return user_input

def clear_console():
    if sys.platform.startswith('win'):
        _ = subprocess.call('cls', shell=True)
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        _ = subprocess.call('clear', shell=True)
    else:
        print('Unsupported platform. Cannot clear console.')

def main():
    while True:
        x = 0
        print_centered(f"""
        {Yellow}Tags{Reset} : 
        [{Yellow}1{Reset}] {Yellow}Maid{Reset}
        [{Yellow}2{Reset}] {Yellow}Waifu{Reset}
        [{Yellow}3{Reset}] {Yellow}Marin-Kitagawa{Reset}
        [{Yellow}4{Reset}] {Yellow}Mori-Calliope{Reset}
        [{Yellow}5{Reset}] {Yellow}Raiden-Shogun{Reset}
        [{Yellow}6{Reset}] {Yellow}Oppai{Reset}
        [{Yellow}7{Reset}] {Yellow}Selfies{Reset}
        [{Yellow}8{Reset}] {Yellow}Uniform{Reset}
        [{Yellow}9{Reset}] {Yellow}Lewd category{Reset}""")
        choice = input_centered('-> ')
        if choice == '1':
            url = "https://api.waifu.im/search/?included_tags=Maid"
            category = "Maid"
        elif choice == '2':
            url = "https://api.waifu.im/search/?included_tags=Waifu"
            category = "Waifu"
        elif choice == '3':
            url = "https://api.waifu.im/search/?included_tags=Marin-Kitagawa"
            category = "Marin-Kitagawa"
        elif choice == '4':
            url = "https://api.waifu.im/search/?included_tags=Mori-Calliope"
            category = "Mori-Calliope"
        elif choice == '5':
            url = "https://api.waifu.im/search/?included_tags=Raiden-Shogun"
            category = "Raiden-Shogun"
        elif choice == '6':
            url = "https://api.waifu.im/search/?included_tags=Oppai"
            category = "Oppai"
        elif choice == '7':
            url = "https://api.waifu.im/search/?included_tags=Selfies"
            category = "Selfies"
        elif choice == '8':
            url = "https://api.waifu.im/search/?included_tags=Uniform"
            category = "Uniform"
        elif choice == '9':
            clear_console()
            print(f'''
            {Yellow}Lewd{Reset} category :
            [{Yellow}1{Reset}] {Yellow}Ass{Reset}
            [{Yellow}2{Reset}] {Yellow}Hentai{Reset}
            [{Yellow}3{Reset}] {Yellow}Milf{Reset}
            [{Yellow}4{Reset}] {Yellow}Oral{Reset}
            [{Yellow}5{Reset}] {Yellow}Paizuri{Reset}
            [{Yellow}6{Reset}] {Yellow}Ecchi{Reset}
            [{Yellow}7{Reset}] {Yellow}Ero{Reset}''')
            choice2 = input('-> ')
            if choice2 == '1':
                url = "https://api.waifu.im/search/?included_tags=Ass"
                category = "Lewd/Ass"
            elif choice2 == '2':
                url = "https://api.waifu.im/search/?included_tags=Hentai"
                category = "Lewd/Hentai"
            elif choice2 == '3':
                url = "https://api.waifu.im/search/?included_tags=Milf"
                category = "Lewd/Milf"
            elif choice2 == '4':
                url = "https://api.waifu.im/search/?included_tags=Oral"
                category = "Lewd/Oral"
            elif choice2 == '5':                   
                url = "https://api.waifu.im/search/?included_tags=Paizuri"
                category = "Lewd/Paizuri"
            elif choice2 == '6':
                url = "https://api.waifu.im/search/?included_tags=Ecchi"
                category = "Lewd/Ecchi"
            elif choice2 == '7':
                url = "https://api.waifu.im/search/?included_tags=Ero"
                category = "Lewd/Ero"
            else:
                print("Invalid choice.")
                clear_console()
                continue

        else:
            print("Invalid choice.")
            clear_console()
            continue

        clear_console()
        print(f'{Yellow}Category{Reset} : {Yellow}{category}{Reset}')
        print(f'''{Yellow}How many {Yellow}images{Reset} do you want to {Yellow}download?{Reset}''')
        num_images = int(input(f"{Yellow}->{Reset} "))

        # Create folder for category if it doesn't exist
        if not os.path.exists(category):
            os.makedirs(category)

        for i in range(num_images):
            time.sleep(0.23)
            response = requests.get(url)
            data = json.loads(response.content)

            try:
                image_url = data["images"][0]["url"]
            except IndexError:
                print(f"No {Yellow}more{Reset} images to {Yellow}download.{Reset}")
                break

            filename = os.path.join(category, os.path.basename(image_url))
            response = requests.get(image_url)

            if response.status_code == 200:
                with open(filename, "wb") as f:
                     f.write(response.content)
                x += 1
                print_centered(f"{Yellow}Image{Reset} saved as {Yellow}{filename}{Reset} | {Yellow}{x}{Reset}/{Yellow}{num_images}{Reset}")
            else:
                print(f"{Yellow}Failed{Reset} to download image. Error code: {Yellow}{response.status_code}{Reset}")
        input_centered(f'{Yellow}Downloaded{Reset} press any {Yellow}key{Reset} to go back')
        clear_console()

main()
