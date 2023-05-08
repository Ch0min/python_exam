import argparse

if __name__ == '__main__':
    # TODO: implement
    parser = argparse.ArgumentParser(description='game data')
    parser.add_argument('--url', help='url to webpage')
    parser.add_argument(
        '-f', '--file', help='name of html file with data')

    args = parser.parse_args()
