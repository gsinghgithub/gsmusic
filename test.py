#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('arg_num', nargs = '?')
args = parser.parse_args()
print args.arg_num