import argparse
import diff

def main():
    parser = argparse.ArgumentParser(description="Compare two files for similarity.")
    parser.add_argument("path1", help="Relative path to the first file.")
    parser.add_argument("path2", help="Relative path to the second file.")
    parser.add_argument("--preprocess", dest="flag", action="store_true", help="Set flag to True.")
    parser.add_argument("--noPreprocess", dest="flag", action="store_false", help="Set flag to False.")
    parser.set_defaults(flag=False)

    args = parser.parse_args()

    diff.getDiff(args.path1, args.path2, args.flag)

if __name__ == "__main__":
    main()
