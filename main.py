from project.app import App
import argparse

class TwitchVideoCompiler:
    def __init__(self):
        pass

    def parse_and_run_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-g', '--game', help='Game name', required=True)
        parser.add_argument('-a', '--amount', help='Amount of clips', required=True)
        parser.add_argument('-l', '--languages', help='Languages', nargs='+', required=False)
        args = parser.parse_args()

        args.languages = args.languages or []

        app = App()
        app.run(args.game, int(args.amount), args.languages)
    
if __name__ == '__main__':
    main = TwitchVideoCompiler()
    main.parse_and_run_args()