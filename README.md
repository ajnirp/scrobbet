scrobbet
========

Unofficial scrobbler for Last.fm

Building
--------

Install dependencies:

    sudo apt-get install python3 python3-taglib python3-docopt python3-bs4

Then add the folder for this project to your `PATH`:

    export PATH="$PATH":"/path/to/scrobbet"

Usage
-----

1. To begin with, run `scrobbet --authorize`. This pops up a window in your default browser and asks you to authorize scrobbet to access your last.fm account. Once authorization is done, scrobbet saves a session key to your home folder.
2. You can now scrobble! Use `scrobbet -s` to scrobble all songs in the current directory. You can use optional args like `--album=<album>` and `--title=<title>` to ensure that only certain tracks are scrobbled.