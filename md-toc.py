import sys
import re


def convert_to_md(name):
	return re.sub(r'[^a-z0-9_-]+', '', name)


# Get file content

if len(sys.argv) != 2:
	print('Usage: python3 md-toc.py target.md')

md_file = sys.argv[1]

with open(md_file, 'r') as in_file:
	content = in_file.read()


# Get the sections
all_secs = re.findall(r'\n(#.*)\n', content)
sections = re.findall(r'\n# (.*)\n', content)
challenges = re.findall(r'\n## (.*)\n', content)

structure = {}
actual_section = ''


# Create a dict with the sections and subsections

for item in all_secs:

	section_result = re.search(r'^# (.*)', item)

	if section_result:
		
		actual_section = '### {}'.format(section_result.group(1))
		structure[actual_section] = []


	chall_result = re.search(r'^## (.*)', item)

	if chall_result:

		actual_chall = chall_result.group(1)

		preprocess = actual_chall.replace(' ', '-').replace('_', '-').lower()
		anchor = convert_to_md(preprocess)
		
		structure[actual_section].append('- [{}](#{})'.format(actual_chall, anchor))


# Print result


for section in structure:
	if not len(structure[section]):
		continue
	print(section)
	for chall in structure[section]:
		print(chall)
	print('\n')
print('<small><i><a href="https://github.com/kashmir54/md-toc">Table of contents generated with md-toc</a></i></small>')