#### Project 1
# Pokémon Battle
- This is a group project. Through GitHub Classroom you should have created a shared GitHub repository with your group members, so as long as you upload your finished code to that group repository, each member in your team will get credit. You will also need to fill out a peer review survey on Learning Suite to recieve credit.
- I do not provide automated tests for projects. You will need to determine yourself whether the code meets the requirements provided in the rubric. After you turn in your code, your code will be manually graded (meaning partial credit may be given for certain requirements). The TAs will update the `Rubric.md` file with your grade and any comments that they have.

- You will expand on the work you did in the “Pokémon and Move Classes” assignment. In that assignment you created 3 `Pokemon` objects and 9 `Move` objects. You’ll reuse the 9 `Move` objects exactly as you already made them. Then, you’ll expand on the 3 `Pokemon` objects so that each `Pokemon` object stores a list of `Move` objects. Then, you’ll choose 2 `Pokemon` to “battle” with their `Moves` until one of them runs out of hit points.
  - As with the previous assignment, you don’t have to have any prior knowledge of Pokémon, but if you didn't watch this short video last time, it may help you to <a href="https://www.youtube.com/clip/Ugkx_pVqGoZu4Vx3ux5fjGtyF28lin6_e-qW">watch this clip</a> for an idea of what Pokémon interactions are like.
  - You’ll be doing a simplified version of the logic going on in the previous video. <a href="https://www.youtube.com/watch?v=1zNEoJeFW9E">Here is an example of me running the program </a> (without showing the code) so you can see what running it looks like.

- Place your code in the `p1_pokemon_battle.py` file. Optionally, you can create any new .py files you want to place functions or classes in. If you do so, just make sure you import those files into `p1_pokemon_battle.py`
- This project is meant to be a challenge and is a **significant** jump in difficulty from past assignments. It requires a solid understanding of object-oriented programming, storing objects in lists, using loops, conditionals, and passing data in and out of functions. I’m confident you can do this. Please reach out to the TAs or professor when you come across any significant roadblock.


## Libraries Required:
- random

## Classes Required:
I list out all the classes here for reference. However, I recommend you just start with the "Logical Flow" section of the instructions and update/write your classes as you go, rather than trying to write all your classes before any of the other logic. But do whatever feels natural to you.

#### Move
> *NOTE: This class is the EXACT same as in your previous assignment.*
- Instance Variables:
  - `move_name` (string)
    - the name of the move
  - `elemental_type` (string)
    - will have value of either “Water”, “Fire”,  “Grass”, or “Normal”
  - `low_attack_points` (int)
    - the lowest number of points that can be generated for the move
  - `high_attack_points` (int)
    - the highest number of points that can be generated for the move
- Methods:
  - `__init__`
    - The constructor / initializer!
  - `get_info`
    - returns a string with the move_name, elemental_type, and the low_attack_points and high_attack_points.
  - `generate_attack_value`
    - returns an int of a randomly generated number between the low_attack_points, and the high_attack_points of the move.

#### Pokemon
>*NOTE: This class has some new variables and methods compared to your previous assignment. New variables/methods have ***NEW*** next to them.*
- Instance Variables:
  - `name` (string)
    - the Pokemon’s name
  - `elemental_type` (string)
    - will have value of either “Water”, “Fire”, or “Grass”
  - `hit_points` (integer)
    - represents the health of the pokemon
  - ***NEW*** `list_of_moves` (list) 
    - Stores an empty list by default, but will be filled by `Move` objects later in your code.
      - Note: Do NOT make an empty list a default value of a parameter. Just create it in your constructor like this: `self.list_of_moves = []`. Making an empty list a default parameter causes all created objects to reference the same empty list.
- Methods:
  - `__init__`
    - The constructor / initializer!
  - `get_info`
    - returns a string with the name, elemental_type and hit_points
  - `heal`
    - adds 15 hit points to `hit_points` and prints out a message with the new number of hit_points.
  - ***NEW*** `display_choices`
    - displays a number next to each move that the Pokémon has. Should also display `“H: Heal 15 hit points”` after the moves. It prints the message directly.
  - ***NEW***  `attack`
    - Besides self, includes parameters:
      - `move_index`
        - an integer representing an index location to use with `list_of_moves` to select a `Move` to attack with.
      - `opposing_pokemon`
        - a `Pokemon` object that will receive the damage from the attack.
    - Will calculate how much damage an attack should do based off of the `Move`’s `generate_attack_value` method, with potential multipliers based on the `elemental_type` of the move, the `elemental_type` of the opposing Pokémon, and a small chance to get a critical hit. Prints out the move that was used, whether or not a type advantage was present, whether or not a critical hit occurred, and how many points of damage occurred. Does not return anything.

## Custom Functions Required:
- `pokemon_battle`
  - Purpose:
    - Starts the battle between your chosen `Pokemon` and an opponent `Pokemon`. Continues until one `Pokemon`’s hit_points reaches 0. Details are described in the logical flow section.
  - Parameters:
    - `your_pokemon`
    - `opponent_pokemon`
      - The two parameters will hold `Pokemon` objects. The object you want to control should be passed first.
  - Return values:
    - None


## Logical Flow:

The project is split up into 4 parts, with part 4 being the longest (so plan accordingly). The instructions will tell you what the code should accomplish but won’t always tell you how to do it. There almost always multiple ways to accomplish each of the requirements. All that matters is you fulfill the listed requirements.

To not overcomplicate the project, you do not need to handle any errors (meaning you can assume the user will always input valid options). However, one design principle you *must* follow is that none of your functions (which includes methods) can reference global variables (which are variables made outside the function). Functions should only reference parameters passed in as arguments (which for methods, includes variables you access through self) or any variables that you make inside the function.


### Part 1: Creating Move objects
---

See the instructions in your previous assignment for details on creating the `Move` class and all the `Move` objects. The exact code for the `Move` class can be copied over, as well as the exact code for creating the 9 Move objects below. All the move objects should be stored in a list.

| Move Name      | Elemental Type | Low Attack Points | High Attack Points |
|----------------|----------------|-------------------|--------------------|
| Tackle         | Normal         | 5                 | 20                 |
| Quick Attack   | Normal         | 6                 | 25                 |
| Slash          | Normal         | 10                | 30                 |
| Flamethrower   | Fire           | 5                 | 30                 |
| Ember          | Fire           | 10                | 20                 |
| Water Gun      | Water          | 5                 | 15                 |
| Hydro Pump     | Water          | 20                | 25                 |
| Vine Whip      | Grass          | 10                | 25                 |
| Solar Beam     | Grass          | 18                | 27                 |

The only thing you will do differently is print out a message that says:
- `These are the moves the pokemon will randomly select from: `

followed by the `get_info` method returned string for all the `Move` objects, as shown below:
```
These are the moves the pokemon will randomly select from:
        Tackle (Type: Normal): 5 to 20 Attack Points
        Slash (Type: Normal): 10 to 30 Attack Points
        Quick Attack (Type: Normal): 6 to 25 Attack Points
        Flamethrower (Type: Fire): 5 to 30 Attack Points
        Ember (Type: Fire): 10 to 25 Attack Points
        Water Gun (Type: Water): 5 to 15 Attack Points
        Hydro Pump (Type: Water): 20 to 25 Attack Points
        Vine Whip (Type: Grass): 10 to 25 Attack Points
        Solar Beam (Type: Grass): 18 to 27 Attack Points
```
 
### Part 2: Creating Pokémon objects and assigning moves
---

See the instructions in your previous assignment for details on creating the `Pokemon` class and all the `Pokemon` objects. You can copy over your code for making the Pokémon class and creating the 3 Pokémon objects, and adding those 3 objects to a list.

| Name        | Elemental Type | Hit Points |
|-------------|----------------|------------|
| Bulbasaur   | Grass          | 60         |
| Charmander  | Fire           | 55         |
| Squirtle    | Water          | 65         |

You will, however, need to make the following changes to the `Pokemon` class:
- In the constructor, `__init__`, add a new instance variable called `list_of_moves` and make it equal to an empty list, like `self.list_of_moves = []`
- Add methods called `display_choices` and `attack`.
  - I recommend not making these methods just yet. The instructions will give more details on them in Part 4.

Now that the `Pokemon` objects will have a `list_of_moves` instance variable, you need to add 2 `Move` objects to each `Pokemon` object’s `list_of_moves`. To clarify, you are NOT just adding the names of the moves to the list, but the entire `Move` objects.

However, this process must follow certain requirements:
- Only add 2 `Move` objects to each `Pokemon`’s `list_of_moves`
- The `Move` objects added to `list_of_moves` should be randomly chosen each time the program is run.
- BUT a move can only be added to a `Pokemon`’s list if either:
  - The `elemental_type` of the `Move` matches the `elemental_type` of the `Pokemon`
  - Or, the `elemental_type` of the `Move` is “Normal”
    - For example, Bulbasaur can get only Grass type moves, or Normal type moves, but not Water or Fire moves.
- A move can never be assigned twice. 
  - e.g. two `Pokemon` can’t both have the `Move` “Slash”, or a single `Pokemon` can’t have two copies of the `Move` “Quick Attack”, etc.

You should print out the `Moves` that are assigned to each `Pokemon` as shown below (though it should differ each time you run your code):

 ```
 Bulbasaur was assigned:
        Vine Whip
        Tackle
Charmander was assigned:
        Ember
        Flamethrower
Squirtle was assigned:
        Water Gun
        Hydro Pump
```

### Part 3: Choosing your Pokémon and the Opponent’s Pokémon
---

Now, your program should print out a number alongside all the available `Pokemon` for the user to choose the `Pokemon` they want to battle with, followed by another display of the `Pokemon` that are left to choose for your opponent. The user should enter a number to choose their `Pokemon` and their opponent. Keep track of which `Pokemon` is the user’s chosen pick, and which is the opponent for Part 4.
- Optional Hint: You may find the `enumerate()` function useful here. <a href="https://chat.openai.com/share/eebd99ee-45af-430c-8ad9-89a4cc0b8b8a"> Click here for an example. </a> But like always, there are many ways to code something so use what makes sense to you.

Here's an example of me choosing Charmander for my `Pokemon` and Bulbasaur as the opponent `Pokemon`:

```
Available Pokemon:
1: Bulbasaur - Type: Grass - Hit Points: 60
2: Charmander - Type: Fire - Hit Points: 55
3: Squirtle - Type: Water - Hit Points: 65
Choose the # of your pokemon: 2

You chose Charmander as your pokemon

1: Bulbasaur - Type: Grass - Hit Points: 60
2: Squirtle - Type: Water - Hit Points: 65
Choose the # of the opponent pokemon: 1

You chose Bulbasaur as the opponent.
```


### Part 4: Battle!
---
Now for the fun (and perhaps frustrating) part!. This section should make a call to a function (not part of any class) called `pokemon_battle` that has two parameters: `your_pokemon` and `opponent_pokemon`, each representing the `Pokemon` objects selected in Part 3.

You may find watching the video posted at the top of this file helpful (the one with the professor running through the finished code) as it shows what it looks like when all the functions/methods are interacting. When `pokemon_battle` is called, it should do the following:

Print out a brief message of `BATTLE START!`, that the `<opponent pokemon name> wants to fight!` and `Go! <your pokemon name>`, like below:

- ```
  BATTLE START!
  Bulbasaur wants to fight!
  Go! Charmander!
  ```

Then, your program should continually go through the following cycle until either your `Pokemon` or the opponent `Pokemon` get to 0 (or below) hit points:
1. Display the result of `get_info` for the opponent `Pokemon` and your `Pokemon`, like below:
    - ```
      Opponent: Bulbasaur - Type: Grass - Hit Points: 60
      You: Charmander - Type: Fire - Hit Points: 55
      ```

2. Your Pokémon should run a method called `display_choices`
    - `display_choices` should print out `Your options:` and then print line for each move in the `Pokemon`’s `list_of_moves`, as well as one extra line for Healing. Each line should have a number, and then display the result of the `Move`’s `get_info` method. The heal line should display `H: Heal 15 hit points`. Nothing needs to be returned, it should print all lines inside the method.
    - For example, if a Pokémon with Ember and Flamethrower stored in `list_of_moves` calls `display_choices`, it would look like this:
      - ```
        Your options:
        1: Ember (Type: Fire): 10 to 25 Attack Points
        2: Flamethrower (Type: Fire): 5 to 30 Attack Points
        H: Heal 15 hit points
        ```

3. Then you should ask for an input with the text:
    - `Choose an option: `
    - Reminder: for this assignment you are NOT required to account for improper inputs. You can assume correct inputs will be given.
4. If the user inputs `H`, then run the `heal` method (you should already have this written from the previous assignment).
5. Otherwise, if the user inputs `1` or `2`, your Pokémon should run the `attack` method:
    - attack should take 3 parameters (`self`, `move_index`, `opposing_pokemon`). `move_index` is just an integer that represents which move was chosen. So if the user entered `1`, that means they want to use the first attack in the Pokémon’s `list_of_moves`, `2` means the second, etc. You should use the `move_index` to get access to the `Move` object. `opposing_pokemon` will be the opposing `Pokemon` object. 
    - The purpose of the `attack` method is to follow an algorithm for what the total attack value will be (or in other words, how many points to take away from the opposing `Pokemon`’s `hit_points` variable)
    - To calculate the attack value (the number to subtract from the opposing `Pokémon`’s hit_points) do the following:
      - Run the `generate_attack_value` method on the `Move` that was selected to generate an integer between the `low_attack_points` and the `high_attack_points`. You should have already created this in the last assignment.
      - Multiply the generated attack value by 2 if there is an elemental type advantage, or by 0.5 if there is a type disadvantage. Don’t multiply the attack value if the Move’s elemental type is “Normal” (or just multiply it by 1). See the below table for a list of attack value multipliers based on the elemental types. 
      - <table border="1" style="text-align: center; ">
          <tr>
              <th>Attack elemental type</th>
              <th>Opposing Pokémon elemental type</th>
              <th>Attack value multiplier</th>
              <th>Advantage message</th>
          </tr>
          <tr>
              <td>Grass</td>
              <td>Fire</td>
              <td>0.5</td>
              <td>“It’s not very effective…”</td>
          </tr>
          <tr>
              <td>Grass</td>
              <td>Water</td>
              <td>2.0</td>
              <td>“It’s super effective!”</td>
          </tr>
          <tr>
              <td>Fire</td>
              <td>Water</td>
              <td>0.5</td>
              <td>“It’s not very effective…”</td>
          </tr>
          <tr>
              <td>Fire</td>
              <td>Grass</td>
              <td>2.0</td>
              <td>“It’s super effective!”</td>
          </tr>
          <tr>
              <td>Water</td>
              <td>Grass</td>
              <td>0.5</td>
              <td>“It’s not very effective…”</td>
          </tr>
          <tr>
              <td>Water</td>
              <td>Fire</td>
              <td>2.0</td>
              <td>“It’s super effective!”</td>
          </tr>
          <tr>
              <td>Normal</td>
              <td>Anything</td>
              <td>None</td>
              <td>None</td>
          </tr>
      </table>

    - Additionally, there is a 6% chance of a “critical hit”, which adds an additional 1.5 multiplier, regardless of any type advantage, disadvantage, or neither.
    - Round the final attack value so that it is a whole number.
    - Subtract the final attack value from the opposing `Pokémon`’s `hit_points`.
  - See the below table for an example of how to calculate each situation:
    - | Example Starting value | Type Advantage? | Critical Hit? | Calculation                |
      |------------------------|-----------------|---------------|----------------------------|
      | 20                     | Advantage       | No            | 20 * 2 = 40                |
      | 20                     | Advantage       | Yes           | 20 * 2 * 1.5 = 60          |
      | 20                     | Disadvantage    | No            | 20 * .5 = 10               |
      | 20                     | Disadvantage    | Yes           | 20 * .5 * 1.5 = 15         |
      | 20                     | None            | No            | 20 = 20                    |
      | 20                     | None            | Yes           | 20 * 1.5 = 30              |
  - Additionally, you must print out:
    - the name of the move used
    - the amount of damage taken
    - if relevant:
      - a critical hit message
      - an advantage message (shown 2 tables above).
  - The order to print these messages is shown in this table:
    - | Order | Message                                                       | Print?                                        |
      |-------|---------------------------------------------------------------|-----------------------------------------------|
      | 1     | `<attacking pokemon name> used <move name>!`                            | Always                                        |
      | 2     | `Critical hit!`                                                | Only if 6% chance critical hit occurs         |
      | 3     | Advantage message (`It’s super effective!` or `It’s not very effective…`) | Only if type advantage or disadvantage occurs |
      | 4     | `<damaged pokemon name> took <attack value> points of damage!` | Always                                        |

6. Now, back in the `pokemon_battle` function, after the `attack` method is run, call the `input()` function with this prompt: `Press enter to proceed...` This doesn’t do anything other than pause the program until the user presses enter in the terminal. This just makes it easier to read what happened (and sort of mimics pressing a button to continue like in the original Pokémon games).
7. Now, it is the opposing `Pokemon` object’s turn to choose a `Move`. Randomly select to either call `attack` with one of their 2 `Moves`, or call `heal` (e.g. there should be an equal chance for any of those 3 options to occur). Just remember that if attack is called, the your_pokemon object needs to be passed into attack instead of the opposing_pokemon (since you are reversing roles of who is attacking).
8. Once the opposing `Pokemon` has attacked, make sure there is another `input` with `Press enter to proceed...` to give a pause before the whole thing starts over again. 
9. Now you should start from step 1 again (displaying `get_info` from both `Pokemon`) until one of the `Pokemon`’s `hit_points` reaches 0.
    - When one of the Pokémon’s hit_points reaches 0, you’ll display text saying which Pokémon was defeated, and which won, like below: 
    - ```
      Bulbasaur has been defeated.
      Charmander has won!
      ```

## Optional Fun
If you want to add some extra fun to your project for absolutely no extra points:
- add `import optional_fun` into your `p1_pokemon_battle.py` file
- call `optional_fun.battle_music()` at the start of the `pokemon_battle` function
- call `optional_fun.attack_sfx()` at the start of the `attack` function
- call `optional_fun.heal_sfx()` at the start of the `heal` function
- call `optional_fun.victory_music()` at the end of the `pokemon_battle` function after the message about who won and who lost. You might need to call it twice depending on how you wrote your code.

## Grading Rubric:
See Rubric.md. Remember to right click and select "Open Preview" to view the file in a nice format. The TAs will update this file with your grade when they are done grading your submission.


## Example Output:
You can watch the video at the top of the file for an example of running the code. Because a lot of the code logic is randomly determined, each run will look different. Below is an example that contains a critical hit, as well as type advantages and disadvantages:

```
These are the moves the pokemon will randomly select from:
        Tackle (Type: Normal): 5 to 20 Attack Points
        Slash (Type: Normal): 10 to 30 Attack Points
        Quick Attack (Type: Normal): 6 to 25 Attack Points
        Flamethrower (Type: Fire): 5 to 30 Attack Points
        Ember (Type: Fire): 10 to 25 Attack Points
        Water Gun (Type: Water): 5 to 15 Attack Points
        Hydro Pump (Type: Water): 20 to 25 Attack Points
        Vine Whip (Type: Grass): 10 to 25 Attack Points
        Solar Beam (Type: Grass): 18 to 27 Attack Points

Bulbasaur was assigned:
        Quick Attack
        Vine Whip
Charmander was assigned:
        Slash
        Ember
Squirtle was assigned:
        Water Gun
        Hydro Pump

Available Pokemon:
1: Bulbasaur - Type: Grass - Hit Points: 60
2: Charmander - Type: Fire - Hit Points: 55
3: Squirtle - Type: Water - Hit Points: 65
Choose the # of your pokemon: 2

You chose Charmander as your pokemon

1: Bulbasaur - Type: Grass - Hit Points: 60
2: Squirtle - Type: Water - Hit Points: 65
Choose the # of the opponent pokemon: 1

You chose Bulbasaur as the opponent.

BATTLE START!
Bulbasaur wants to fight!
Go! Charmander!

Opponent: Bulbasaur - Type: Grass - Hit Points: 60
You: Charmander - Type: Fire - Hit Points: 55

Your options:
1: Slash (Type: Normal): 10 to 30 Attack Points
2: Ember (Type: Fire): 10 to 25 Attack Points
H: Heal 15 hit points
Choose an option: 2

Charmander used Ember!
It's super effective!
Bulbasaur took 42 points of damage!

Press enter to proceed...

Bulbasaur has been healed to 33 hit points.

Press enter to proceed...

Opponent: Bulbasaur - Type: Grass - Hit Points: 33
You: Charmander - Type: Fire - Hit Points: 55

Your options:
1: Slash (Type: Normal): 10 to 30 Attack Points
2: Ember (Type: Fire): 10 to 25 Attack Points
H: Heal 15 hit points
Choose an option: H

Charmander has been healed to 70 hit points.

Press enter to proceed...

Bulbasaur used Quick Attack!
Charmander took 19 points of damage!

Press enter to proceed...

Opponent: Bulbasaur - Type: Grass - Hit Points: 33
You: Charmander - Type: Fire - Hit Points: 51

Your options:
1: Slash (Type: Normal): 10 to 30 Attack Points
2: Ember (Type: Fire): 10 to 25 Attack Points
H: Heal 15 hit points
Choose an option: 1

Charmander used Slash!
Critical hit!
Bulbasaur took 22 points of damage!

Press enter to proceed...

Bulbasaur used Vine Whip!
It's not very effective...
Charmander took 8 points of damage!

Press enter to proceed...

Opponent: Bulbasaur - Type: Grass - Hit Points: 11
You: Charmander - Type: Fire - Hit Points: 43

Your options:
1: Slash (Type: Normal): 10 to 30 Attack Points
2: Ember (Type: Fire): 10 to 25 Attack Points
H: Heal 15 hit points
Choose an option: 2

Charmander used Ember!
It's super effective!
Bulbasaur took 46 points of damage!

Press enter to proceed...

Bulbasaur has been defeated.
Charmander has won!
```







