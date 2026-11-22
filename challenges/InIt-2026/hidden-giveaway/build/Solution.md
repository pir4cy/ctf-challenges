# The Solution

To solve this challenge, users will have to review the bit planes of the image.

The QR code is visible on Blue 0. This can be extracted using local tools such as zsteg or online tools [Georgeom - Stegonline](https://georgeom.net/StegOnline)


The QR takes you to https://ctf.pir4cy.com/init-misc1, where participants can recover the flag by decrypting the base64.

Copy the base64 and run `echo "base64_string" | base64 -d` to retrieve the flag.

Flag: `InIt{h1d1ng_1n_b1ue_l1gh7}`

