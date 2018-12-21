import argparse
parser = argparse.ArgumentParser()
#parser.parse_args()

parser._action_groups.pop()  # To list the required component first
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('--required_arg')
optional.add_argument('--optional_arg')
print parser.parse_args()
