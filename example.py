from padr import pad

lines = [
	'ID - Resolution (Type)| Extension - Filesize',
	'139 - audio only (DASH audio) | .m4a - ?',
	'140 - audio only (DASH audio) | .m4a - ?',
	'160 - 256x144 (DASH video) | .mp4 - ?',
	'133 - 426x240 (DASH video) | .mp4 - ?',
	'134 - 640x360 (DASH video) | .mp4 - ?',
	'135 - 854x480 (DASH video) | .mp4 - ?',
	'136 - 1280x720 (DASH video) | .mp4 - ?',
	'17 - 176x144 (small) | .3gp - ?',
	'36 - 320x180 (small) | .3gp - ?',
	'43 - 640x360 (medium) | .webm - ?',
	'18 - 640x360 (medium) | .mp4 - ?',
	'22 - 1280x720 (hd720) | .mp4 - ?'
]

delim = ',̆'

delimitered_lines = [line.replace('-', f'{delim}-').replace('|', f'{delim}|').replace('(', f'{delim}(') for line in lines]

padded_lines = pad(delimitered_lines, delim)

print('With padr you can go from: \n')
print('\n'.join(lines))
print('\nTo\n')
print('\n'.join(padded_lines))
print('\nIn just three lines!')
