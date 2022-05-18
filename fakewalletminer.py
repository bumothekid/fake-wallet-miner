from pprint import pprint
import time
import contextlib
import random
import secrets
import requests
from colorama import Fore
from tqdm import tqdm

def getCurrentRate() -> float:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    return round(response.json()["bpi"]["USD"]["rate_float"], 2)

def printProgressBar():
    print()

    for _ in tqdm(range(int(9e6)), desc=f"{Fore.RED} Starting Miner {Fore.RESET}"):
        pass

    print()

def searchWallet():
    currentRate = getCurrentRate()
    found = False

    while not found:
        possibleChance = random.randint(1, 100_000_000) <= 10
        walletAdress = secrets.token_hex(20)
        bitcoinAmount = round(random.uniform(0.05, 100) / 50, 2)
        bitcoinUSDValue = round(currentRate * bitcoinAmount, 2)

        if not possibleChance:
            print(f"{Fore.RED} > 0x{walletAdress} > 0.00 BTC ($0.00) {Fore.RESET}")
            continue

        print(f"{Fore.GREEN} > 0x{walletAdress} > {bitcoinAmount} BTC ({bitcoinUSDValue}) {Fore.RESET}\n")
        print(f"{Fore.GREEN} Transferring {bitcoinAmount} Bitcoin (${bitcoinUSDValue}) to your wallet... {Fore.RESET}")

        time.sleep(5)

        print(f"{Fore.GREEN} Successfully transfered {bitcoinAmount} Bitcoin to your wallet! {Fore.RESET}")
        print(f"{Fore.RED} Closing Wallet Miner {Fore.RESET}")
        found = True
        

if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        print(f"""
        {Fore.RED}
        ______    _          _    _       _ _      _    ___  ___                
        |  ___|  | |        | |  | |     | | |    | |   |  \/  |                
        | |_ __ _| | _____  | |  | | __ _| | | ___| |_  | .  . |_ _ __   ___ _ __ 
        |  _/ _` | |/ / _ \ | |/\| |/ _` | | |/ _ \ __| | |\/| | | '_ \ / _ \ '__|
        | || (_| |   <  __/ \  /\  / (_| | | |  __/ |_  | |  | | | | | |  __/ |   
        \_| \__,_|_|\_\___|  \/  \/ \__,_|_|_|\___|\__| \_|  |_/_|_| |_|\___|_|   {Fore.RESET}
        """)

        print(f"{Fore.RED} ----------------------------------------------------------------------------- {Fore.RESET}")
        start = input("Do you want to start the mining? (y/n)\n")

        if start not in ["y", "yes"]:
            print(f"{Fore.RED} Exiting the Wallet miner... {Fore.RESET}")
            time.sleep(3)
            exit()

        printProgressBar()

        searchWallet()