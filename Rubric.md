### MAX SCORE: 100
### YOUR SCORE:  
## Grader's Notes:
- TAs: Put any notes on points lost here.
---
## Rubric

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>#</th>
      <th>Requirement</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Move class works as specified in previous assignment</td>
      <td>5</td>
    </tr>
    <tr>
      <td>2</td>
      <td>All 9 Move objects are created, and their get_info method is printed out.</td>
      <td>5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Pokémon class works as specified in previous assignment, but with list_of_moves instance variable added</td>
      <td>5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>All 3 Pokémon objects created</td>
      <td>5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2 Move objects assigned to each Pokémon object, according to stated rules</td>
      <td>15</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Pokémon and their assigned Moves printed out</td>
      <td>2</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Pokémon printed out and user can select 2 Pokémon</td>
      <td>8</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Pokémon class: display_choices</td>
      <td>10</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Pokémon class: attack</td>
      <td>20</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Custom function: pokemon_battle</td>
      <td>20</td>
    </tr>
    <tr>
      <td>11</td>
      <td>includes comments: name and description at the top, and comments throughout</td>
      <td>3</td>
    </tr>
    <tr>
      <td>12</td>
      <td>File uploaded properly to GitHub</td>
      <td>2</td>
    </tr>
    <tr>
      <td colspan="2">Total</td>
      <td>100</td>
    </tr>
  </tbody>
</table>

## TA Guide:

1. #### `Move` class works as specified in previous assignment
    - 5 points

2. #### All 9 `Move` objects are created, and their `get_info` method is printed out.
    - 5 points
        - -1 for each object not created
        - -2 if `get_info` not printed out for each object
3. #### Pokémon class works as specified in previous assignment, but with list_of_moves instance variable added
    - 5 points
        - -2 if list_of_moves isn't added
4. #### All 3 Pokémon objects created
    - 5 points
5. #### 2 Move objects assigned to each Pokémon object, according to stated rules
    - 5 points
        - -3 if more or fewer than 2 moves are added.
        - -5 if the assigned move isn't either Normal type or matches the elemental type of the Pokémon
        - -2 if the move can be added twice to any Pokémon
6. #### Pokémon and their assigned Moves printed out
    - 2 points
7. #### Pokémon printed out and user can select 2 Pokémon
    - 8 points
        - -4 if you can't select 2 pokemon using an inputted number
        - -3 if it doesn't print out by like the example
8. #### Pokémon class: display_choices
    - 10 points
        - -5 if it doesn't print each move's get_info and a number 1 or 2
        - -2 if it doesn't print a line for healing.
        - -2 if it references global variables
9. #### Pokémon class: attack
    - 20 points
        - -3 if an error in generating the base attack value
        - -7 if the logic for calculating type advantage just isn't there or is wildly wrong
        - -2 if the logic for calculating type advantage is mostly correct but has small errors
        - -4 if logic is missing for 6% chance of a critical hit.
        - -5 if the final value for attack value isn't correctly calculated for reasons not already mentioned  (e.g. the logic of type advantages and critical hits was correct, but they did something wrong after or before)
        - -1 if the calculated attack value isn't rounded
        - -2 if the calculated attack value isn't subtracted from the opponent hit points
        - -2 for each message in the message table that doesn't print correctly
        - -4 if it references global variables
10. #### Custom function: pokemon_battle
    - 20 points
        - -2 if it doesn't print out the opening lines
        - -3 if it doesn't repeatedly print out the results of get_info after each pokemon does an option.
        - -5 if missing the option for the user to choose an attack/heal or it doesn't work properly
        - -1 if it doesn't make the user press enter to proceed after each pokemon does their options.
        - -5 if the opposing Pokémon doesn't randomly choose among their 3 options and do one of those options
        - -5 if it doesn't continually repeat until one pokemon reaches 0 or below on their hit points
        - -5 if it doesn't end once a pokemon reaches 0 hit points
        - -1 if it doesn't print out which pokemon was defeated and which won.
        - -4 if it references global variables

11. #### includes comments: name and description at the top, and comments throughout
    - 3 points
        - -1 if it didn't include their name
        - -2 if it didn't include general comments. Err on the side of leniency

12. #### File uploaded properly to GitHub
    - 2 points
