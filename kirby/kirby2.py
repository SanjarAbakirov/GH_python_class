import sys


def colored_kirby():
    pink = "\033[95m"
    red = "\033[91m"
    reset = "\033[0m"

    kirby = [
        f"{pink}    **********    {reset}",
        f"{pink}  **************  {reset}",
        f"{pink} **************** {reset}",
        f"{pink}******************{reset}",
        f"{pink}*****{reset}        {pink}*****{reset}",
        f"{pink}****{reset}   {red}####{reset}   {pink}****{reset}",
        f"{pink}***{reset}   {red}#    #{reset}   {pink}***{reset}",
        f"{pink}***{reset}   {red}#    #{reset}   {pink}***{reset}",
        f"{pink}****{reset}   {red}####{reset}   {pink}****{reset}",
        f"{pink}*****{reset}        {pink}*****{reset}",
        f"{pink}******************{reset}",
        f"{pink} **************** {reset}",
        f"{pink}  **************  {reset}",
        f"{pink}    **********    {reset}",
        f"{pink}     ****  ****   {reset}",
        f"{pink}      **    **    {reset}"
    ]

    for line in kirby:
        print(line)


if __name__ == "__main__":
    if sys.platform != "win32" or "ANSICON" in os.environ:
        colored_kirby()
    else:
        # Для Windows без поддержки ANSI
        kirby = [
            "    **********    ",
            "  **************  ",
            " **************** ",
            "******************",
            "*****        *****",
            "****   ####   ****",
            "***   #    #   ***",
            "***   #    #   ***",
            "****   ####   ****",
            "*****        *****",
            "******************",
            " **************** ",
            "  **************  ",
            "    **********    ",
            "     ****  ****   ",
            "      **    **    "
        ]
        for line in kirby:
            print(line)
