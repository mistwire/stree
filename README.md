# stree
stree is a command line application that mimics the functionality of the `tree` command, specifically for listing the contents of S3 buckets in a tree-like format.

## Project Structure

```
s3-tree-app
├── src
│   ├── main.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the application, use the following command:

```
python src/main.py [bucket_name] [prefix]
```

Replace `[bucket_name]` with the name of the S3 bucket you want to traverse, and `[prefix]` with the optional prefix to filter the results. If no prefix is provided, the entire bucket will be listed.

## Examples

```
python src/main.py my-bucket
python src/main.py my-bucket my/prefix/
```

## Dependencies

This project requires the following Python packages:

- boto3: For interacting with AWS S3.