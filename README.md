# Description
This project is a Python-based simulation of Blackjack card counting. It includes a detailed implementation of the game mechanics, basic strategy, and the Zen card counting technique. The simulator allows users to run multiple rounds and games, tracking various statistics like total earnings, bets, and Return on Investment (ROI).


# Features
- Simulation of Blackjack game mechanics.
- Implementation of basic strategy and card counting.
- Detailed player and dealer actions and decisions.
- Statistical analysis of player performance over multiple games.
- Visualization of ROI distributions.


# Usage

To run the simulation on a chosen no. of rounds, run:
```python main.py```

To analyze the ROI distribution, time series or effect of deck size run any of the following scripts:
```python show_roi_dist.py```
```show_roi_time_series.py```
```show_roi_vs_decks.py```


# Game Rules

This Blackjack simulator adheres to the following set of rules:

- **Dealer Hits on Soft 17 (H17):** The dealer is required to take additional cards ("hit") until their hand totals 17 or more points, with an ace counted as 11 (a "soft" hand).
- **Double After Split (DAS) Permitted:** Players have the option to double their bet on a hand that has been created through splitting a pair. This is applicable for any pair that is split.
- **Single Split Allowed:** Each hand can only be split once. After splitting a pair, no further splitting is permitted, even if another pair is formed.
- **Blackjack Payout:** If a player achieves Blackjack (an ace and a 10-value card as the initial two cards), the payout is 1.5 times the original bet.
- **No Surrender Option:** Currently, the game does not support the surrender option, where a player can forfeit half their bet to end their participation in a round. However, this feature may be considered for future implementation.

# Author

Ryan Bertschinger