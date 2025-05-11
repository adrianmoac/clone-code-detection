import argparse
import diff

def main():
    parser = argparse.ArgumentParser(description="Compare two files for similarity.")
    parser.add_argument("path1", help="Relative path to the first file.")
    parser.add_argument("path2", help="Relative path to the second file.")

    args = parser.parse_args()

    diff.getDiff(args.path1, args.path2)

if __name__ == "__main__":
    main()
