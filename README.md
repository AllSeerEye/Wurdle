# Wurdle
Have you heard of the game Wordle? It was made by a software engineer by the name of Josh Wardle. 

I was introduced to it by my parents. They'd been playing it a lot. It isn't too hard to recreate and you can do it in an afternoon. One of the most time-consuming parts was trying to figure out how to add the words. I tried many different ways, even using a pip package called [Random-Word](https://pypi.org/project/Random-Word/). Although I might use this package another time, I didn't like the words that it was spitting out. I ended up going on Google and searching for "five letter words." I then made a curated list of five letter words. 117 words. It took about 20 minutes to get the 117 words. You can see my final code in `src/wurdle.py`.

## Usage
```
usage: wurdle.py [-h] [-t TRIES]

options:
  -h, --help            show this help message and exit
  -t TRIES, --tries TRIES
                        change the amount of tries you can have (from 1 to 20)
```

## Features
* Set number of tries with command-line flag
* Shows what letters you have guessed wrong
* Tells you if you enter a word that is not five letters long.

## Running
```
python3 wurdle.py [-t TRIES]
```
or
```
chmod +x wurdle.py
./wurdle.py [-t TRIES]
```

## Dependencies
```
pip install colorama pyfiglet
```
You might need to use `pip3` instead of pip.