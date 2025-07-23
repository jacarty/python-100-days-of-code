"""
Day Seven Content - Hangman Game

This will reenforce the concepts covered so far:
-- For/while loops
-- If/Else
-- Lists
-- Strings
-- Range
-- Modules
"""

"""

The hangman logic:

                    ┌─────────────┐
                    │    START    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Generate a │
                    │ random word │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │Generate as  │
                    │many blanks  │
                    │as letters   │
                    │in word      │
                    └──────┬──────┘
                           │
                           ▼
         ┌─────────►┌─────────────┐◄─────────┐
         │          │Ask the user │          │
         │          │to guess a   │          │
         │          │letter       │          │
         │          └──────┬──────┘          │
         │                 │                 │
         │                 ▼                 │
         │          ┌─────────────┐          │
         │          │Is the       │          │
         │          │guessed      │          │
         │          │letter in    │          │
         │          │the word?    │          │
         │          └──┬──────┬───┘          │
         │             │      │              │
         │         Yes │      │ No           │
         │             ▼      ▼              │
         │      ┌──────────┐ ┌──────────┐    │
         │      │Replace   │ │Lose a    │    │
         │      │the blank │ │life      │    │
         │      │with the  │ │          │    │
         │      │letter    │ │          │    │
         │      └────┬─────┘ └────┬─────┘    │
         │           │            │          │
         │           ▼            ▼          │
         │    ┌──────────┐ ┌──────────┐      │
         │    │Are all   │ │Have they │      │
         │    │the blanks│ │run out   │      │
         │    │filled?   │ │of lives? │      │
         │    └──┬───┬───┘ └──┬───┬───┘      │
         │       │   │        │   │          │
         │    No │   │ Yes    │   │ No       │
         └───────┘   │    Yes │   └──────────┘
                     │        │
                     └────┬───┘
                          │
                          ▼
                   ┌─────────────┐
                   │ GAME OVER   │
                   └─────────────┘
"""

