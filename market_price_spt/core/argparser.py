import argparse


def loadArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mode",
        default="server",
        type=str,
        help="Application mode",
    )
    parser.add_argument(
        "-a",
        "--adapter",
        type=str,
        help="Exchange adapter",
    )
    return parser.parse_args()
