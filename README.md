# Space Assault

## Project Overview

Space Assault is a simple 2D arcade shooter developed as a CSE 310 course project.

The game is inspired by classic arcade games such as Space Invaders, with an additional mechanic where individual enemies can leave the formation, attack the player, and then return to their original formation.

The main goal of the project was to practice Python programming, object-oriented programming, game loops, collision detection, user input, and basic game development using Pygame.

---

## Features

### Player

- Move left and right using the keyboard.
- Supports both `A / D` and the arrow keys.
- Shoot projectiles using the `SPACE` key.
- The player has three lives.
- Temporary invulnerability is activated after taking damage.
- The player visually blinks while invulnerable.

### Enemy Formation

- Multiple enemies are organized into a formation.
- The formation moves horizontally across the screen.
- When the formation reaches an edge, it changes direction and moves downward.
- Enemies can be destroyed by player bullets.

### Individual Enemy Attacks

One of the main features of Space Assault is the individual enemy attack system.

An available enemy can leave the formation and attack the player.

During the attack:

- The enemy moves diagonally.
- The initial horizontal direction is determined by the player's current position.
- The enemy bounces when it reaches the edge of the screen.
- The enemy eventually stops attacking.
- The enemy returns to the current formation position.
- The attacking enemy is displayed with a different color.

### Enemy Projectiles

Enemies can also shoot projectiles toward the player.

If an enemy projectile hits the player:

- The player loses a life.
- Temporary invulnerability is activated.
- The player visually blinks during the invulnerability period.

### Score and Game States

- The player receives points for destroying enemies.
- The game displays the current score.
- The game displays the player's remaining lives.
- The player wins when all enemies are destroyed.
- The game ends if the player loses all lives.
- The game also ends if the enemy formation reaches the player's zone.

### Audio

A simple shooting sound effect is played when the player fires.

---

## Technologies

- Python
- Pygame
- Object-Oriented Programming
- Git / GitHub

---

## Controls

| Key | Action |
|---|---|
| `A` | Move left |
| `D` | Move right |
| `←` | Move left |
| `→` | Move right |
| `SPACE` | Shoot |

---

## Project Structure

```text
SpaceAssault/
├── src/
│   ├── main.py
│   ├── settings.py
│   ├── player.py
│   ├── bullet.py
│   └── enemy.py
│
├── assets/
│   ├── images/
│   └── sounds/
│       └── player_shoot.wav
│
└── README.md