from rich.prompt import Prompt
from rich import print
import os

input = Prompt.ask

class CLI:
    @classmethod
    def log(cls, content = ""):
        os.system("cls")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("> [blue][[b]log[/b]][/blue] ", content)

    @classmethod
    def error(cls, content = ""):
        os.system("cls")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("> [error][[b]error[/b]][/error] ", content)

    @classmethod
    def input_str(cls, prompt: str = ""):
        os.system("cls")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        result = input("> [blue][[b]input[/b]][/blue] [red][i](string)[/i][/red] [green]" + prompt + "[/green]")

        if result.strip() == "":
            return cls.input_str(prompt)

        return result
    
    @classmethod
    def input_int(cls, prompt: str = "", min: int = None, max: int = None):
        os.system("cls")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        result = input("> [blue][[b]input[/b]][/blue] [red][i](integer number)[i/][/red] [green]" + prompt + "[/green]")

        if not result.strip().isnumeric():
            return cls.input_int(prompt, min, max)

        integer = int(result)

        if min:
            if integer < min:
                return cls.input_int(prompt, min, max)

        if max:
            if integer > max:
                return cls.input_int(prompt, min, max)

        return integer

    @classmethod
    def input_yes_no(cls, prompt: str = ""):
        os.system("cls")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        result = input("> [blue][[b]input[/b]][/blue] [red][i](yes/no)[i/][/red] [green]" + prompt + "[/green] [purple][b](Y/n)[/b][/purple]")

        yes = ["yes", "y"]
        no = ["no", "n"]

        result = result.lower()

        if not result in [*yes, *no]:
            return cls.input_yes_no(prompt)

        return result in yes

__all__ = [ CLI ]