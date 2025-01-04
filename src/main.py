import boto3
import sys
from utils import list_bucket_contents, format_tree_structure, print_tree


def main():
    if len(sys.argv) > 1:
        bucket_name = sys.argv[1]
    else:
        print("Usage: python src/main.py [bucket_name]")
        sys.exit(1)

    s3 = boto3.client("s3")

    try:
        contents = list_bucket_contents(s3, bucket_name)
        tree = format_tree_structure(contents)
        print_tree(tree)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
