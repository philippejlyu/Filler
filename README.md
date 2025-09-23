# Introduction
I am trying to figure out the best strategy to play filler. To do this, I am going to simulate many random games and determine the best strategy to win

## What is filler
Filler is a very simple game. A player selects a color to expand their area on the board. The player with the highest score at the end wins. 
There were a few things I had to note when I implemented Filler.py
1. We cannot just assign a random color to each square. That makes the game not work.
2. Squares that are beside each other (horizontally or vertically) cannot be the same color. Squares that are diagnoal from eachother can be the same color.

# Minimax algorithm
In minimax, we implement a very simple algorithm to determine the next best step

# Observations
It seems like the best way to play is to control an entire axis
i.e. Go up or go right as much as possible then continue.
This is just a crude observation. I need to run more simulations to determine this

# Conclusion