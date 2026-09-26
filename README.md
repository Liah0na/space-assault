# Overview

Space Assault is a 2D arcade-style space shooter where the player controls a spaceship and must destroy an enemy formation before the enemies reach the player's zone.

The player can move horizontally using the `A` and `D` keys or the left and right arrow keys. The player can shoot by pressing the `SPACE` key. Destroying enemies increases the score, while enemy projectiles can reduce the player's lives.

The enemy formation moves horizontally across the screen and moves downward when it reaches the edge. In addition to the regular formation movement, individual enemies can leave the formation and attack the player. During an attack, an enemy moves diagonally, changes direction when it reaches the edge of the screen, and eventually returns to the current formation position.

The player starts with three lives. After receiving damage, the player becomes temporarily invulnerable and visually blinks. The game ends when the player loses all lives, when the enemy formation reaches the player's zone, or when all enemies have been destroyed.

The purpose of developing this software is to improve my skills as a software engineer by practicing Python programming, object-oriented programming, game loops, collision detection, event handling, state management, debugging, and code organization. I also wanted to gain practical experience developing an interactive application from an initial simple mechanic and gradually improving it through testing and refactoring.

[YouTube demonstration Space Assault](https://youtu.be/xdUzJs7DUKQ)

# Development Environment

The project was developed using the following tools and technologies:

- **Operating System:** Ubuntu 26.04.1 LTS
- **Programming Language:** Python 3.13.15
- **Game Library:** Pygame 2.6.1
- **Graphics/Audio:** Pygame
- **Code Editor:** Visual Studio Code
- **Version Control:** Git
- **Repository:** GitHub
- **Python Environment:** pyenv and Python virtual environment (`.venv`)

The project uses Python and Pygame to create the game window, process keyboard input, manage the game loop, draw game objects, detect collisions, and play sound effects.

The code is organized into separate modules according to their responsibilities:

- `main.py` - Controls the main game loop and coordinates the game.
- `settings.py` - Contains game configuration and constants.
- `player.py` - Manages the player, movement, lives, damage, and invulnerability.
- `bullet.py` - Provides the reusable bullet behavior for player and enemy projectiles.
- `enemy.py` - Manages individual enemies, the enemy formation, enemy movement, attacks, and enemy projectiles.

This structure allows the project to remain simple while keeping different responsibilities separated and easier to maintain.

# Useful Websites

The following websites were useful during the development of Space Assault:

* [Pygame Documentation](https://www.pygame.org/docs/)
* [Pygame Tutorials](https://www.pygame.org/wiki/tutorials)
* [Python Documentation](https://docs.python.org/3/)
* [Python Tutorial](https://docs.python.org/3/tutorial/)

# Future Work

There are several improvements that could be added to Space Assault in the future:

* Add multiple enemy attack patterns to make enemy behavior less predictable.
* Add multiple waves of enemies with increasing difficulty.
* Add different enemy types with different movement and attack behaviors.
* Improve the visual design by replacing the simple rectangles with spaceship and enemy sprites.
* Add additional sound effects for shooting, explosions, player damage, victory, and Game Over.
* Add background music and volume controls.
* Add visual effects such as explosions, particles, and screen effects.
* Add a restart option after the player wins or loses.
* Add a high-score system.
* Improve the user interface with a start screen and game instructions.