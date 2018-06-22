scrobbet
========

Unofficial command-line scrobbler for Last.fm

Building
--------

Install dependencies. On Ubuntu:

    sudo apt-get install python3 python3-taglib python3-docopt python3-bs4
    
On Fedora 27+:

    sudo dnf install taglib-devel
    pip3 install --user BeautifulSoup4 pytaglib docopt

Then add the folder for this project to your `PATH`:

    export PATH="$PATH":"/path/to/scrobbet"

Usage
-----

To begin with, run `scrobbet --authorize`. This pops up a window in your default browser and asks you to authorize scrobbet to access your last.fm account. Once authorization is done, scrobbet saves a session key to your home folder.

You can now scrobble!

### Scrobbling from music on disk

Use `scrobbet -s` to scrobble all songs in the current directory. You can use optional args like `--album=<album>` and `--title=<title>` to ensure that only certain tracks are scrobbled.

### Scrobbling from a file

You can also scrobble from a file containing song data, provided it is in the format consumed by `scrobbet`. Run `write-tags.py` in a directory to see an example of the output.

Given such a file, you can scrobble the songs in it by running `scrobbet -f /path/to/tags/file`.
