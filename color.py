def color(col):
	if col == 'yellow':
		return '\033[93m'
	if col == 'red':
		return '\033[91m'
	if col == 'green':
		return '\033[32m'
	if col == 'cyan':
		return '\033[36m'
	if col == 'magenta':
		return '\033[35m'
	if col == 'end':
		return '\033[0m'