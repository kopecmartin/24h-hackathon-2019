# 24h-hackathon-2019


## About
This project was implemented during 24h hackathon competition in Brno organised
by [UnIT](https://unitbrno.cz/) Brno on 12-13.4.2019.

## Task

The task was to create an application for creating advertising videos. The
potential users are large e-shops with a huge amount of pictures of their
products.

Therefore the app should be:
- easy to use
- able to take some users preferences
- easily automatable (because of the huge amount of product pictures)

## Our Goal

We had only 24 hours to implement it, so don't expect anything awesome and
directly ready to use ...

However our goal was to create a CLI application which allows a user to define
a set of pictures, let the user to choose an animation, effect, font of the
captions and the application would take care of the rest.
Thanks to the CLI interface, the application can be called from a different
script so that more videos of any number of product pictures can be created.

We had problems to find any usable library for the animations also called
easing so we had to develop something on our own. We came up with a quite
interesting idea of defining several points on a screen/frame/picture
through a user would like an animation to go through. Then the app interpolates
the given points, creates a function which the user can use for getting a y-axe
point for any given x-axe point - and that's mostly what's needed for creating
an animation.

Some of the videos we created via the app can be seen in the `demovideos`
branch. Not quite amazing, however, if more animations and effects (and also
nicer and more complex ones) were created, the app could be used for creating
promo videos every day/hour of such an e-shop which was described in the task.

## Prerequisites
* Python 3.6 or higher (but it may work even with older versions of Python 3)
* pip3

## Install

1. Install requirements which are listed in the requirements.txt
    ```
    $ ./tools/install_venv.sh
    ```
2. The script creates a .venv where all requirements are installed, source it:
    ```
    $ source .venv/bin/activate
    ```

## Run
```
$ main.py [-h] [-b BACKGROUND] [-a ANIMATION] [-f FONT] [-e EFFECT]
               [-s SPEED] [-m MULTI] [-t TITLE] [-p PRICE] [-r] [-l LINE]
               [-o OUTPUT]
```

## Options

**optional arguments:**

-  -h, --help => show this help message and exit
-  -b BACKGROUND, --background BACKGROUND => specify background video
-  -a ANIMATION, --animation ANIMATION => choose animation
-  -f FONT, --font FONT  Font to use => choose font
-  -e EFFECT, --effect EFFECT => Choose a color effect to be used
-  -s SPEED, --speed SPEED => Speed of the animation (pixels per frame)
-  -t TITLE, --title TITLE => Show the title text.
-  -p PRICE, --price PRICE => Show the price tag.
-  -m, --multi => Multiple product images on the video frame.
-  -r, --render => Show realtime rendering.
-  -l LINE, --line LINE => Chooses a line from the csv file.
-  -o OUTPUT, --output OUTPUT => Output file.

## Authors

[Martin Kopec](https://www.linkedin.com/in/martin-kopec-07b29096/)

[Martin Krajnak](https://www.linkedin.com/in/martin-kraj%C5%88%C3%A1k-148348151/)

[Patrik Segedy](https://www.linkedin.com/in/patrik-segedy-693979148/)

[Tibor Dudlak](https://www.linkedin.com/in/tibor-dudl%C3%A1k-6a8270142/)
