#!/usr/bin/env python3

import sys

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print('Please passe arguments! '+sys.argv[0]+' REGEX', file=sys.stderr)
		sys.exit(1)
import re

compiled=None
if __name__ == '__main__':
	try:
		compiled = re.compile(sys.argv[1])
		#print(f"DEBUG compiled regex: '{sys.argv[1]}' successuflly")
	except:
		print('Could not compile regex', file=sys.stderr)
		sys.exit(2)

def get_regex_match(regex, line):
	res = regex.match(line)
	if res is None:
		return None
	r = res.groupdict()
	del res
	return r

def clean_string(s):
	if s is None:
		return ""
	else:
		return s.strip()


if __name__ == '__main__':
	for line in sys.stdin:
		res = get_regex_match(compiled, line)
		if res is None:
			print("NO MATCH")
			continue
		print(" ".join([ f"{k}=\"{clean_string(v)}\"" for k,v in res.items()] ))
