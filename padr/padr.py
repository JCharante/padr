def pad(lines, delim):
	"""
	Right Pads text split by their delim.
	:param lines: 
	:param delim: 
	:return: 
	"""
	"""
	Populates text into chunks. If the delim was & then
	['12 & 344', '344 & 8', '8 & 88'] would be stored in chunks as
	[['12', '344', '8'], ['344', '8', '88']]
	"""
	chunks = []
	for i in range(len(lines)):
		line = lines[i]
		sections = line.split(delim)
		for j in range(len(sections)):
			if len(chunks) <= j:
				chunks.append([])
			chunks[j].append(sections[j])

	"""
	Calculates & Stores the max length of chunks
	"""
	max_lengths = []
	for i in range(len(chunks)):
		_max = max([len(j) for j in chunks[i]])
		max_lengths.append(_max)

	"""
	Pads the children of chunks according to the chunk's max length" \
	"""
	for i in range(len(chunks)):
		for j in range(len(chunks[i])):
			chunks[i][j] += (max_lengths[i] - len(chunks[i][j])) * ' '
	new_lines = ['' for i in range(len(lines))]

	for i in range(len(chunks)):
		for j in range(len(chunks[i])):
			new_lines[j] += chunks[i][j]
	return new_lines
