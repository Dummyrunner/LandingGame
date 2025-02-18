# Concept Plan
Orientation https://pet.triquence.org/A02_air_track_framework.pdf

# Needed Components (Classes)
* GameWindow
  * Attributes
    * Dimensions of screen
    * Display surface object
  * Methods
    * Init
    * Set Caption (opt)
    * Erase Screen
  
* LinearKinematics
  * Attributes (SI units by default)
    * position (p)
    * velocity (v)
    * acceleration (a)
    * mass
    * Max./Min. boundaries for phyisical attributes
  * Methods
    * step
    * saturate according to min max boundaries

* Rocket(Pygame Sprite, LinearKinematics)
  * Attributes
    * Visualization: Sprite
    * Rect: aligned to sprite
  * Methods

* Platform
  * Attributes
    * Position
    * Dimensions
    * Max./Min. boundaries for phyisical attributes
  * Methods

* GeneralPhysics
  * Attributes
    * Gravitation
    * Objects affected by Physics []
  * Methods
    * Handle Physics
      * ...
    * Collision Detection

* Environment
    * Attributes
      * Ratios: pixel2meter, meter2pixel
      * Timestep size (?)
    * Methods
      * Conversions: pixel2meter, meter2pixel

* CommonConstants dataclass struct
  * gravitational acc.
  * ...


## Game Procedure 
### Main Game Loop:
* Erase surface
* establish time step
* check for user input
* Update physics
* Draw objects on new positions
  * Convert meter to pixels
  * draw
* update total time from starting
* Make update visible

## Infrastructure
### DevOps tools
* Formatter: Black, default settings
* unit test library: pytest
### Repo Structure
* `LandingGame`
  * `test/`
  * `landing_game/`


