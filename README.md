## Worddle solver
interactive simple wordler solver wriiten in python.
the solver will guess the english word in your mind.
## Usage 
- think of an 6 letter english word ( or use this program against websites like wordle2.in
- run ```python wordle.py```
    - the program will make a guess , you should input result
    - in the result, 1 means correct, 0 means wrong, X means this letter exist but at another position.
        - e.g. for word:second, guess: decode, result should be X11100.  
        - e.g. for word:pastry, guess: polite, result should be 1000X0. 
    - the program will get your word after a few guesses.
    - P.S. if the program give an invalid word(not recognized by some website), just input x, and it will make another guess.
- anyway, use it as you like.

