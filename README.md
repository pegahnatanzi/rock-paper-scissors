# rock-paper-scissors

## Installation

Clone or download this repo onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```cd my-first-python-app```

## Setup

Setup an virtual environment:

```conda create -n my-rps-game-env python=3.8```
```conda activate my-rps-game-env```


To install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Configuring Environment Variables

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    PLAYER_NAME="Pegah"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means each person who uses our code needs to create their own local ".env" file.


## Usage

To run the script to see the output, i.e. run the rock-paper-scissors game:

```python my_script.py```