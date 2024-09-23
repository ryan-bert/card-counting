# Blackjack Simulation and Card Counting

## Description
This project is a Python-based simulation of Blackjack, focusing on card counting strategies and game mechanics. It implements both basic strategy and the Zen card counting technique, allowing users to simulate multiple rounds and games while tracking various statistics such as total earnings, bets, and Return on Investment (ROI). The simulator also provides visualization tools for analyzing player performance over time and the impact of different game parameters.

## Features
- **Comprehensive Blackjack Simulation**: Full implementation of Blackjack game mechanics, including player and dealer actions.
- **Basic Strategy and Card Counting**: Incorporates basic strategy and Zen card counting methods.
- **Statistical Tracking**: Records detailed statistics over multiple rounds and games.
- **ROI Analysis and Visualization**: Provides tools for analyzing ROI distributions, time series, and the effect of the number of decks.
- **Customizable Game Parameters**: Allows adjustment of game rules and simulation parameters.

## Installation

To run this project, ensure you have Python 3.x installed on your system. Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/blackjack-simulator.git
cd blackjack-simulator/src
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To run the simulation on a chosen no. of rounds, run:
```bash
python main.py
```

To analyze the ROI distribution, time series or effect of deck size run any of the following scripts:
```bash
python show_roi_dist.py
```
```bash
python show_roi_time_series.py
```
```bash
python show_roi_vs_decks.py
```

## Game Rules

This Blackjack simulator adheres to the following set of rules:

- **Dealer Hits on Soft 17 (H17):** The dealer is required to take additional cards ("hit") until their hand totals 17 or more points, with an ace counted as 11 (a "soft" hand).
- **Double After Split (DAS) Permitted:** Players have the option to double their bet on a hand that has been created through splitting a pair. This is applicable for any pair that is split.
- **Single Split Allowed:** Each hand can only be split once. After splitting a pair, no further splitting is permitted, even if another pair is formed.
- **Blackjack Payout:** If a player achieves Blackjack (an ace and a 10-value card as the initial two cards), the payout is 1.5 times the original bet.
- **No Surrender Option:** Currently, the game does not support the surrender option, where a player can forfeit half their bet to end their participation in a round. However, this feature may be considered for future implementation.

## Output Analysis

Key insights from 500 games of 1000 rounds each:

1. **ROI and Deck Size:**
   - **Declining ROI with More Decks:** As the number of decks increases, ROI generally declines, which aligns with expected behavior. However, there's an unexpected spike at **6 decks**, likely an anomaly in the simulation or card distribution.
   
2. **Convergence of ROI:**
   - **Both Strategies Converge:** Over many rounds, the ROI for both card counting and basic strategy converges toward zero, reflecting diminishing card counting advantages over extended play.

3. **Average ROI Results:**
   - **Zen Card Counting:** Average ROI = **0.0335**, which is plausible and consistent with card counting advantages.
   - **Basic Strategy:** Average ROI = **0.0043**, which should be **negative** due to the house edge. This suggests a possible issue with the basic strategy simulation.

In summary, the card counting simulation is mostly accurate, but the basic strategy results require further investigation.

## Author

Ryan Bertschinger