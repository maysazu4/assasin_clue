# Assassin/Clue Party Game

This is a Python implementation of an "assassin"/clue party game where players try to identify the murderer based on clues provided.

## Description

The game involves:
- 20 place names
- 10 weapons
- Each player has a name, a list of last visited places, and a list of favorite weapons
- Each round, a murder occurs at a specific place with a specific weapon
- The assassin visits the murder place and the murder weapon is one of his/her favorites
- Players can suspect other players based on randomly selected visited places and a favorite weapon
- Players can accuse other players of being the murderer

## Setup

To set up the game, ensure you have Python installed on your system. You can then run the game script by executing the `main()` function.

## Points of Failure

The game may fail if:
- Incorrect input types are provided
- Insufficient number of players, places, or weapons are provided
- Errors occur during random selections
- Accusations are not handled correctly

## Error Handling

The game script includes error handling to catch and handle exceptions that may occur during gameplay. If an error occurs, an error message will be displayed, and the game will continue to run.

## Input Validation

Input validation is performed to ensure that valid inputs are provided for player actions, setup parameters, and other game components. Invalid inputs are rejected with appropriate error messages.
