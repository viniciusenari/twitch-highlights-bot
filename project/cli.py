from app import App
import argparse

class CLI:
    def __init__(self):
        pass

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-g', '--game', help='Game name', required=True)
        parser.add_argument('-a', '--amount', help='Amount of clips', required=True)
        parser.add_argument('-l', '--languages', help='Languages', nargs='+', required=False)
        args = parser.parse_args()

        app = App()
        app.run(args.game, int(args.amount), args.languages)