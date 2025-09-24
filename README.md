# Introduction
I am trying to figure out the best strategy to play filler. To do this, I am going to simulate many random games and determine the best strategy to win

## What is filler
Filler is a very simple game. A player selects a color to expand their area on the board. The player with the highest score at the end wins. 
There were a few things I had to note when I implemented Filler.py
1. We cannot just assign a random color to each square. That makes the game not work.
2. Squares that are beside each other (horizontally or vertically) cannot be the same color. Squares that are diagnoal from eachother can be the same color.

# Minimax algorithm
Minmax is a very simple algorithm to determine the next best step

# Observations
It seems like the best way to play is to control an entire axis
i.e. Go up or go right as much as possible then continue.
This is just a crude observation. I need to run more simulations to determine this

# Conclusion
The best strategy can be broken down into 3 sections:
1. Early game (turn 1-10)
Choose for maximum immediate gain
Push towards the opponent's corner quickly to limit their space
Avoid spreading too wide horizontally early and instead focus on climbing the board.

2. Mid game (turn 11-20)
Cut off the opponent
    * Aim to surround or isolate their territory
Think 1-2 moves ahead
    * Before you choose, think if you pick this, what will the opponent pick next. Will choosing this color let them select something even better

3. Late game (turn 21+)
By now most of the board is 2 territories. Choose colors that connect to unclaimed areas even if small to prevent the opponent from filling them.

Select perimiter cells that block off the opponents path to other cells

