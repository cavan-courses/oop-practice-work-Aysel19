### Tasks
1. (Easy difficulty) Refactor code in `a.py`
  Get rid of repeated code by exporting repeated logic in functions.
2. (Medium difficulty) Implement logic for battles with multiple enemies.
3. (Hard difficulty) Make game. See **Game task** section.
4. Model (using classes and functions) problem in **Modeling task** section.

# Game task
(What will be in game?)

*It is a console application*
*GUI will be your terminal screen*

##### Main screen
In main screen user sees following options:
```
1. Start game (goes to game screen)
2. Load last saved game (loads last saved stats)
3. Save stats (saves current score)
4. Show stats (shows current stats)
3. Quit (quit games without saving)
```

##### Game screen
In game screen a list of enemies to fight appears, for example:
```
1. Frank (weak enemy)
2. Tom (big fat cat)
3. Akva (strong fighting dog)
```
Then user selects enemy he wants to fight and goes to *fight screen*.

Additional task: Make logic for selecting multiple enemies and implement logic of fight in *fight screen*.

##### Fight screen
Fight screen is already implemented, just improve it to suit your game needs.

Additional task: Add power-ups logic (+health, +attack or for example *enemy skips his move*... and so on...)
Additional task 2: Add something more interesting if you can :).

After fight screen player's score increases by amount of enemies defeated (minimum 1) and user is returned back to *main screen*.


# Modeling task

Model school.

(What exactly?)
I won't say, but for example

```python
class Teacher:
    # ... ... ...
    # ... ... ...

class Principle(Teacher): # Direktor
    # ... ... ...
    # ... ... ...

class School:
    def __init__(self, principle, teachers):
        self.principle = principle
        self.teachers = list(teachers)
        # ... ...

    # ... ... ...
    # ... ... ...


# and so on
```


# Good luck!
We will look for solution of this task next Saturday :)
