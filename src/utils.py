def connect_to_s3():
    import boto3
    return boto3.client('s3')

def list_bucket_contents(s3, bucket_name):
    contents = []
    paginator = s3.get_paginator('list_objects_v2')
    
    for page in paginator.paginate(Bucket=bucket_name):
        if 'Contents' in page:
            contents.extend(page['Contents'])
    
    return contents

def format_tree_structure(contents):
    tree_structure = {}
    
    for item in contents:
        key = item['Key']
        parts = key.split('/')
        current_level = tree_structure
        
        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
    
    return tree_structure

def print_tree(tree, prefix=''):
    keys = list(tree.keys())
    for i, key in enumerate(keys):
        if i == len(keys) - 1:
            print(prefix + '└── ' + key)
            new_prefix = prefix + '    '
        else:
            print(prefix + '├── ' + key)
            new_prefix = prefix + '│   '
        print_tree(tree[key], new_prefix)