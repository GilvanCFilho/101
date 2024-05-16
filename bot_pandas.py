import pandas as pd

from botcity.core import DesktopBot

    


class Bot(DesktopBot):
    def action(self, execution=None):

        self.browse('www.youtube.com')

        ...
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
                    