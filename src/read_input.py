import argparse


def read_input() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        return f.read()
