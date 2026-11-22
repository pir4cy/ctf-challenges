# ctf.pir4cy.com
CTF Challenges

These are the CTF challenges that I have created for fun and/or for CTFs.

Public Challenges are stored in the main folder while challenges for specific competitions are stored in their respective folders.

## Running the challenge site

Install Flask with `python -m pip install -r requirements.txt`, then start the app with `python app/app.py`. The challenge board is available at `http://localhost:5000/challenges`.

The InIt 2026 board presents each challenge's README and downloadable challenge file. Submitted flags are checked on the server against the `Flag:` entry in each challenge's `build/Solution.md`; solution files are not offered as downloads.

For production, run the app with a WSGI server and configure the web server or hosting platform to route `ctf.pir4cy.com/challenges` to this Flask app.
