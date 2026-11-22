# The Solution

This is a classic matryoshka challenge. The idea is that there are layers of archives.

The initial PDF file is actually a zip file, which users can find using `file`.

Using the provided outer_wordlist.txt and john the ripper, users will crack the password of the zip.

1. Rename the pdf to .zip
2. Use `zip2john` to generate hash for zip.
3. Using the `outer_wordlist.txt` for the initial zip, we reveal an image, a wordlist and a hint for the layer.
4. Each layer contains the following: 1 image, 1 wordlist, 1 hint.
5. Players are expected to follow these steps:
- `file <image>.jpg` & `binwalk -e <image.jpg>` 
- `zip2john <zip_recovered_from jpg> > recovered-hash`
- `john --wordlist=<recovered_wordlist> recovered-hash`
- `unzip` or `tar` to extract the archive.

6. Final PDF has the flag.


Flag: `InIt{j0urney_4cr0ss_1ndia}`
 
