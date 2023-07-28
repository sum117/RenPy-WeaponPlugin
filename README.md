# RenPy Weapon Plugin

The Weapon Plugin is an extension designed for the Ren'Py visual novel game engine. It enables developers to add an interactive weapon feature, including actions like shooting and reloading, to their games.

![Example](example.gif)

## Features

* Weapon state control (shooting, reloading)
* Customizable sound effects for shooting and reloading actions
* Easily integrable with other game systems

## Usage

To use this plugin, you need to create an instance of the `Weapon` class and add it to your screen:

```python
screen gun_screen:
    add Weapon(
        static_displayable="shotgun.png", 
        shooting_displayables=["shotgun_shooting.png"], 
        reloading_displayables=["shotgun_reloading1.png","shotgun_reloading2.png", "shotgun_reloading3.png", "shotgun_reloading4.png"], 
        shooting_sfx="<from 3.7 to 5.3>sfx_shotgun.opus", 
        reloading_sfx="<from 1.7 to 2.6>sfx_shotgun.opus"
    )
```

The parameters for the `Weapon` class are:

* `static_displayable`: The default image of the weapon
* `shooting_displayables`: A list of images displayed when the weapon is shooting
* `reloading_displayables`: A list of images displayed when the weapon is reloading
* `shooting_state`: Initial shooting state (optional)
* `reloading_state`: Initial reloading state (optional)
* `shooting_sfx`: The sound effect for shooting (optional)
* `reloading_sfx`: The sound effect for reloading (optional)

## Contribution

Contributions are welcomed! If you find a bug or have a feature suggestion, please open an issue to discuss.

## License

This project is under the [MIT](LICENSE) license.
