import argparse
from config import APP_NAME, VERSION


def parse_args():
    parser = argparse.ArgumentParser(description=APP_NAME)

    parser.add_argument(
        "--area",
        type=str,
        required=False,
        help="Nome da area de analise"
    )

    parser.add_argument(
        "--periodo",
        type=str,
        required=False,
        help="Periodo da analise"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print(APP_NAME)
    print("Versao:", VERSION)

    if args.area:
        print("Area:", args.area)

    if args.periodo:
        print("Periodo:", args.periodo)


if __name__ == "__main__":
    main()