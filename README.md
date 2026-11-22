# ctf.pir4cy.com
CTF Challenges

These are the CTF challenges that I have created for fun and/or for CTFs.

Public Challenges are stored in the main folder while challenges for specific competitions are stored in their respective folders.

## Running the challenge site

Install the dependencies with `python -m pip install -r requirements.txt`, then start the app locally with `python app/app.py`. The challenge board is available at `http://localhost:5000/challenges`.

The InIt 2026 board presents each challenge's README and downloadable challenge file. Submitted flags are checked on the server against the `Flag:` entry in each challenge's `build/Solution.md`; solution files are not offered as downloads.

For production, the existing `ctf-web` systemd service can run the app with Gunicorn. If its virtual environment needs to be recreated, from the repository root run:

```sh
python3 -m venv /opt/ctf/venv
/opt/ctf/venv/bin/python -m pip install --upgrade pip
/opt/ctf/venv/bin/python -m pip install -r requirements.txt
systemctl restart ctf-web
systemctl status ctf-web
```

If creating the virtual environment fails because `venv` is unavailable, install the OS package that provides `python3-venv` first. The repository, including the `challenges/` directory, should be deployed at `/opt/ctf/app` so the app can read challenge files. The existing web server should continue proxying requests to Gunicorn at `127.0.0.1:8080`.
