
import io
import os
import sys
import json
import yaml
import random
import hashlib
import logging
import argparse
import requests

from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.logging import RichHandler

from yaml.loader import SafeLoader
from typing import Optional, Any
from datetime import datetime

from resources import (
    VISA,
    MASTER, 
    m_COUNTRIES_
)

if os.name == 'nt':
    CLEAN_cmd = "cls"
else:
    CLEAN_cmd = "clear"

CUSTOM_THEME = Theme(
    {
        "z3bol": "red3 bold",
        "t7shT": "dodger_blue2",
        "mok": "green1",
        "kinga": "bright_magenta",
        "symbol_m": "blue"
    }
)

FORMAT = "%(message)s"

console = Console(theme=CUSTOM_THEME)

class BinGen_: 
    
    def __init__(self, type_: int, count_: int, country_: Optional[str]) -> None:

        self.count = count_

        if country_ != "RANDOM": self.country = country_
        else: self.country = random.choice([k for k, _ in m_COUNTRIES_.items()][0]) 

        self.type_ = type_
        self.alpha2 = m_COUNTRIES_[self.country.replace('_', ' ').title()].upper()

        self.bin_list = [] # 123456, 123457 ...
        self.valid_bins = [] # {bin: bin_, result: response (bin_lookup_response_json)}
        self.save_out = None

    def generate_bins(self) -> None:
        
        for _ in range(self.count):
            bin_ = ''
            for _ in range(5):
                bin_ += str(random.randint(0, 9))
            self.bin_list.append(str(self.type_) + bin_)
    
    def bin_lookup(self, bin_: str) -> dict:

        r_ = requests.get(f"https://lookup.binlist.net/{bin_}", headers={"Accept-Version": "3"})
        # return r_.json() # FIXME: JSONDECODE... error sometimes idk

        try:
            return {
                "message": r_.json(),
                "op": True
            }
        except Exception:
            return {
                "message": "exception occurred",
                "op": False
            }
    
    def process_data(self) -> None:
        
        for i in self.bin_list:
            response = self.bin_lookup(bin_=i)
            if response["op"]:
                r_country_a = response["message"]["country"]["alpha2"]
                r_country = response["message"]["country"]["name"]
                # response["message"]["country"]["alpha2"] == self.alpha2
                # XXX! V
                if r_country_a == self.alpha2:
                    logger_.info(f"[VALID]: {i} | Country: {r_country}")
                    response["message"]["country"]["emoji"] = "XD"
                    self.valid_bins.append(
                        {
                            "bin": i,
                            "response": response["message"]
                        }
                    )
                else:
                    logger_.error(f"[UNVALID]: {i} | Country: {r_country}")
    
    def save_data(self) -> bool:

        iS_Saved = False

        if not os.path.exists('output'):
            os.mkdir('output')
            self.save_data()
        else:
            save_file = str(datetime.now().strftime("%H-%M-%S")) + '_' + hashlib.md5(str(datetime.now()).encode("utf-8")).hexdigest() + ".json"
            
            with io.open(file=f"output/{save_file}", mode='w') as fstream:
                fstream.write("[")
                for data_ in self.valid_bins:
                    buffer = json.dumps(data_)
                    fstream.write(buffer)
                    if data_ != self.valid_bins[-1]:
                        fstream.write(",")
                fstream.write("]") 

            self.save_out = save_file

        iS_Saved = not (self.valid_bins.__len__() == 0)
        return iS_Saved
    
    def _quit(self):
        os.system(CLEAN_cmd)
        console.print(f" - You're Valid Generated Bin's SavedTo: '{self.save_out}'\n\n\t- Thanks For You're Time\n\t\t ♥ cya :3 ♥ .\n\n")
    
    @staticmethod
    def bannerWhoTf():
        console.print("\n\n")
        console.print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠠⠤⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
        console.print("⠀⠀⠀⠀⣀⢤⡒⠉⠁⠀⠒⢂⡀⠀⠀⠀⠈⠉⣒⠤⣀⠀⠀⠀⠀")
        console.print("⠀⠀⣠⠾⠅⠈⠀⠙⠀⠀⠀⠈⠀⠀⢀⣀⣓⡀⠉⠀⠬⠕⢄⠀⠀")
        console.print("⠀⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠶⢦⡀⠑⠀⠀⠀⠀⠈⢧⠀ ")
        console.print("⠀⡇⠀⠀⠀⠀⠀⢤⣀⣀⣀⣀⡀⢀⣀⣀⠙⠀⠀⠀⠀⠀⠀⢸⡄")
        console.print("⠀⢹⡀⠀⠀⠀⠀⡜⠁⠀⠀⠙⡴⠁⠀⠀⠱⡄⠀⠀⠀⠀⠀⣸⠀")
        console.print("⠀⠀⠱⢄⡀⠀⢰⣁⣒⣒⣂⣰⣃⣀⣒⣒⣂⢣⠀⠀⠀⢀⡴⠁⠀")
        console.print("⠀⠀⠀⠀⠙⠲⢼⡀⠀⠙⠀⢠⡇⠀⠛⠀⠀⣌⣀⡤⠖⠉⠀⠀")
        console.print("⠀⠀⠀⠀⠀⠀⢸⡗⢄⣀⡠⠊⠈⢦⣀⣀⠔⡏⠀⠀⠀⠀⠀⠀⠀")
        console.print("⠀⠀⠀⠀⠀⠀⠈⡇⠀⢰⠁⠀⠀⠀⢣⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀")
        console.print("⠀⠀⠀⠀⣠⠔⠊⠉⠁⡏⠀⠀⠀⠀⠘⡆⠤⠿⣄⣀⠀⠀⠀⠀⠀")
        console.print("⠀⠀⠀⠀⣧⠸⠒⣚⡩⡇⠀⠀⠀⠀⠀⣏⣙⠒⢴⠈⡇⠀⠀⠀⠀")
        console.print("⠀⠀⠀⠀⠈⠋⠉⠀⠀⢳⡀⠀⠀⠀⣸⠁⠈⠉⠓⠚⠁⠀⠀⠀⠀")
        console.print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠛⠛              [kinga]@made_by:[/kinga] [mok]LHAJ ok ??[/mok][symbol_m]#[/symbol_m][z3bol]1096[/z3bol]\n\n")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        type_str = ["VISA" if self.type_ == 4 else "MASTER"][0] + " CARD"
        console.print(f" - [mok]ANYWAYS![/mok] [t7shT]TYPE:[/t7shT] [z3bol]{type_str}[/z3bol] [mok]@[/mok] [t7shT]COUNT:[/t7shT] [z3bol]{self.count}[/z3bol] [mok]@[/mok] [t7shT]COUNTRY[/t7shT]: [z3bol]{self.country}[/z3bol]\n\n")

        self.generate_bins()
        self.process_data()
        
        # TODO: add those
        if self.save_data():
            self._quit()
        else:
            os.system(CLEAN_cmd)
            print("FOUND NOTHING ... CHECK AGAIN OR INCREASE THE COUNT IT's FREE")

if __name__ == "__main__":

    with open('config.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    
    l_level = data['LoggingLevel']
    if l_level == '' or l_level == ' ' or not l_level: l_level = "INFO"

    # TODO: initiate logger
    logging.basicConfig(level=l_level, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])
    logger_ = logging.getLogger("rich")
    
    
    # TODO: parse args
    parser = argparse.ArgumentParser(
        description=" (˶˃ᆺ˂˶) A Simple BinLookup/BinGenerator Using Requests & Makin in beautiful using rich lib (˶˃ᆺ˂˶) ",
        epilog="Thanks for your time CHAD *** XD",
    )
    subparser = parser.add_subparsers(dest='command')
    start = subparser.add_parser('start')
    help_ = subparser.add_parser('help')

    start.add_argument("--count", type=int, required=True)
    start.add_argument("--type", type=str, required=True)
    start.add_argument("--country", type=str, required=False, default="UNITED_STATES")

    help_.add_argument("--countries", action="store_true", required=False)

    args = parser.parse_args()

    if args.command == 'help':
        os.system(CLEAN_cmd)
        print('\n')
        for k, v in m_COUNTRIES_.items():
            m_country_ = "_".join(k.split(' '))
            console.print(f" > [mok]{m_country_}[/mok]")
        exit(0)
    elif args.command == 'start':

        # TODO: check if type isn't VISA | MASTER
        if not (args.type == "VISA" or args.type == "MASTER"): 
            # print("--type should be either VISA or MASTER")
            logger_.error("type error !")
            console.print("\t   [z3bol][!][/z3bol]\t    [kinga]--type[/kinga] should be either [mok]VISA[/mok] or [mok]MASTER[/mok]")
            sys.exit(-1)
        else:
            
            if args.type == "VISA": args.type = VISA
            if args.type == "MASTER": args.type = MASTER

            # NOTE: i don't think a MAX_COUNT is needed | i hate limits 'MATH NERD KHO TSHAPISTA dw'
            # TODO: check the country if valid
            bladzPi_ = str(args.country).title().replace('_', ' ')
            if bladzPi_ in [k for k, _ in m_COUNTRIES_.items()]:
                os.system(CLEAN_cmd)
                BinGen_.bannerWhoTf()
                BinGen_(type_=args.type, count_=args.count, country_=args.country).__call__()
            else:
                logger_.error(f" {bladzPi_} ? BRO THIS PLACE DOESN'T EXIST ?! LMAO")
        
        # TODO: add logging leve NOTSET | DEBUG | INFO