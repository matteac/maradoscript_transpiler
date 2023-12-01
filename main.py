import argparse
from parser import Parser

def main():
    arg_parser = argparse.ArgumentParser(
        prog="Maradoscript transpiler",
        description="Transpile PeleScript to MaradoScript",
    )
    arg_parser.add_argument(
        "-i", 
        "--input",
        type=str,
        help="Input PeleScript file",
        default="in.ps",
    )
    arg_parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output MaradoScript file",
        default="out.ms",
    )
    args = arg_parser.parse_args()

    code = ""
    with open(args.input, "r") as f:
        code = f.read()
    output = Parser(code).parse()
    with open(args.output, "w") as f:
        f.write(output)



if __name__ == "__main__":
    main()

