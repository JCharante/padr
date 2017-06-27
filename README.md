# padr

Python 3 Padding Library

## Install

It's on PyPi, install with

```bash
$ pip install padr
```

## Example

(Using a monospace font is necessary for the demonstration)

With padr you can go from:

```
ID - Resolution (Type)| Extension - Filesize
139 - audio only (DASH audio) | .m4a - ?
140 - audio only (DASH audio) | .m4a - ?
160 - 256x144 (DASH video) | .mp4 - ?
133 - 426x240 (DASH video) | .mp4 - ?
134 - 640x360 (DASH video) | .mp4 - ?
135 - 854x480 (DASH video) | .mp4 - ?
136 - 1280x720 (DASH video) | .mp4 - ?
17 - 176x144 (small) | .3gp - ?
36 - 320x180 (small) | .3gp - ?
43 - 640x360 (medium) | .webm - ?
18 - 640x360 (medium) | .mp4 - ?
22 - 1280x720 (hd720) | .mp4 - ?
```

To

```
ID  - Resolution (Type)       | Extension - Filesize
139 - audio only (DASH audio) | .m4a      - ?
140 - audio only (DASH audio) | .m4a      - ?
160 - 256x144    (DASH video) | .mp4      - ?
133 - 426x240    (DASH video) | .mp4      - ?
134 - 640x360    (DASH video) | .mp4      - ?
135 - 854x480    (DASH video) | .mp4      - ?
136 - 1280x720   (DASH video) | .mp4      - ?
17  - 176x144    (small)      | .3gp      - ?
36  - 320x180    (small)      | .3gp      - ?
43  - 640x360    (medium)     | .webm     - ?
18  - 640x360    (medium)     | .mp4      - ?
22  - 1280x720   (hd720)      | .mp4      - ?
```

In just three lines!
