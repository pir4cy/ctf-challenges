# The Solution

This one is quite straightforward, the only twist is the URL which will giveaway the flag.

The URL is hiding in the ImageDescription of one image from a bunch of images. 

`exiftool -ImageDescription *.jpg | grep -i "ctf"` 

URL: https://ctf.pir4cy.com/exif-flag

Copy the base64 and run `echo "base64_string" | base64 -d` to retrieve the flag.

Flag: `InIt{h1d1ng_1n_m3tad4t4}`
