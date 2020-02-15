# FlapPy Bird (A python version of Flappy Bird Game)

The main purpose of this project is to demonstrate that you can build nice games on Python using PyGame. 

Initially, my idea was to use AI to play this game but later on I decided that this will make a project too complicated so I decided to keep things simple

As for me, the main idea around all this pet project was to get to know the concepts and techniques of Software Engineering.

[//]:#
![video](https://media3.giphy.com/media/euuaA2cwLEUuI/giphy.gif?cid=790b76111f0c39a1c15a764ac504e97512b1d16982def664&rid=giphy.gif)

----

**Overview of my badges**

Travis-CI:

[![Travis build status](https://travis-ci.com/yusif-ifraimo/FlapPy_Bird_SWT.svg?branch=master)](https://travis-ci.com/yusif-ifraimo)

CodeCov:

[![codecov](https://codecov.io/gh/yusif-ifraimo/FlapPy_Bird_SWT/branch/master/graph/badge.svg)](https://codecov.io/gh/yusif-ifraimo/FlapPy_Bird_SWT)

AppVeyor:

[![Build status](https://ci.appveyor.com/api/projects/status/k9km8fyluwwbox57?svg=true)](https://ci.appveyor.com/project/yusif-ifraimov/flappy-bird-swt)

CodeClimate:

[![Test Coverage](https://api.codeclimate.com/v1/badges/983281f5f5ee15bfe5cc/test_coverage)](https://codeclimate.com/github/yusif-ifraimo/FlapPy_Bird_SWT/test_coverage)
<a href="https://codeclimate.com/github/yusif-ifraimo/FlapPy_Bird_SWT/maintainability"><img src="https://api.codeclimate.com/v1/badges/983281f5f5ee15bfe5cc/maintainability" /></a>

Sonarcloud:

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=yusif-ifraimo_FlapPy_Bird_SWT)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=yusif-ifraimo_FlapPy_Bird_SWT&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=yusif-ifraimo_FlapPy_Bird_SWT&metric=security_rating)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=yusif-ifraimo_FlapPy_Bird_SWT&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=yusif-ifraimo_FlapPy_Bird_SWT&metric=code_smells)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT) 

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=yusif-ifraimo_FlapPy_Bird_SWT&metric=bugs)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=yusif-ifraimo_FlapPy_Bird_SWT&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=yusif-ifraimo_FlapPy_Bird_SWT&metric=sqale_index)](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)

## 1. UML
To create UML diagrams I used a PlantUML plugin in PyCharm.
### 1.1. Use Case Diagram
<p align="center">
  <img src="https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/docs/UML/Use_Case_Diagram.png">
</p>

### 1.2. Class Diagram
<p align="center">
  <img src="https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/docs/UML/flappy_bird-Class_Diagram.png">
</p>

### 1.3. Activity diagram
<p align="center">
  <img src="https://github.com/yusif-ifraimov/Data-Science-M.Sc/blob/master/Advanced%20Software%20Techniques/FlapPy_Birds/docs/UML/flappy_bird-Activity_Diagram.png">
</p>

## 2. Metrics

By clicking on the bages above you should be
redorected to an appropriate page. Nevertheless, here
are all the metrics that I used towards my pet project:
* [codeclimate](https://codeclimate.com/github/yusif-ifraimo/FlapPy_Bird_SWT)
* [sonarcloud.io](https://sonarcloud.io/dashboard?id=yusif-ifraimo_FlapPy_Bird_SWT)  
* [codecov.io](https://codecov.io/gh/yusif-ifraimo/FlapPy_Bird_SWT) 


## 3. Clean Code Development
I used the principles from **Clean Code by Robert Martin** book and <a href = https://www.python.org/dev/peps/pep-0008/>**PEP Conventions** </a>.

1. [Maximum Line Length](https://pep8.org/#maximum-line-length):
    Limit all lines to a maximum of 79 characters.
    ```python
    def getHitmask(image):
    #returns a hitmask using an image's alpha.
    mask = []
    for x in xrange(image.get_width()):
        mask.append([])
        for y in xrange(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask
    ```
   Why I like PyCharm is that it is really easy to monitor the number of characters in your code.

2. [Method Names and Instance Variables](https://pep8.org/#method-names-and-instance-variables):
    Use the function naming rules: lowercase with words separated by underscores is necessary to improve readability.
    ```python
    def __get_Random_Pipe():
        # returns a randomly generated pipe
        # y of gap between upper and lower pipe
        gapY = random.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
        gapY += int(BASEY * 0.2)
        pipeHeight = IMAGES['pipe'][0].get_height()
        pipeX = SCREENWIDTH + 10

        return [
            {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
            {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
        ]
    ```

3. [Intendation](https://www.python.org/dev/peps/pep-0008/#indentation)
    Use 4 spaces per indentation level.
    ```python
    def pixelCollision(rect1, rect2, hitmask1, hitmask2):
        #Checks if two objects collide and not just their rects
        rect = rect1.clip(rect2)

        if rect.width == 0 or rect.height == 0:
            return False

        x1, y1 = rect.x - rect1.x, rect.y - rect1.y
        x2, y2 = rect.x - rect2.x, rect.y - rect2.y

        for x in xrange(rect.width):
            for y in xrange(rect.height):
                if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                  return True
        return False
    ```
4. [Class Names](https://pep8.org/#class-names):
    Class names should normally use the CapWords convention.
    ```python
    class User(object):
        ...
    class Bird:
        ...
    class ShowWelcomeAnimation:
        ...
    ```
5. Function rules: Small, Do one thing, Use descriptive names:
    ```python
    def getBackgroundID(self):
        """
        Returns the id's of the background images
        """
        return [self.__background_default, *self.__background]
   
    def stop(self):
        """
        Function to stop background animation
        """
        return self.__stop = True
    
    def birdIsAlive(self):
        """
        Checks if the bird is alive
        """
        return self.__isAlive

    def getTag(self):
        """
        Returns the bird tag
        """
        return self.__tag

    def kill(self):
        return self.__isAlive = False    
        
    def get_pos(self):
        return self.__get_pos()
    ```

     
       
   
[10 points CCD Cheatsheet](https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/docs/10%20point%20cheat%20sheet.pdf)

## 4. Build Management (with PyGradle and Gradle)
It took me a lot of time in order to find out how to do a proper Build Managment in Python. 
Eventually I found that the most convenient way is [PyGradle](https://github.com/innobead/pygradle).

Here what it does:
* it launches tests
* installs environment, dependencies etc.
* builds python <a href="https://pythonwheels.com/"> wheel </a>
* generates docs (both html and xml) 

There was a tricky part - Gradle does not work with PyCharm 
(there will be a pop up saying you need IntelliJ Ultimate)
but it works with IntelliJ. There is a nice <a href="https://engineering.linkedin.com/blog/2016/08/introducing--py-gradle--an-open-source-python-plugin-for-gradle"> article </a> explaining how
gradle works.

You will find two files in my repository:
* [gradle_report.txt](https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/gradle_report.txt) an output example of the report from my computer.
* [build.gradle](https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/build.gradle) file with instruction for build.

After running build.gradle file it creates its own setup.py file. 


## 5. Unit-Tests
There is a GUI in my project but I thought that it would be unreasonable to test it. I just tested all the modules in my code responsible for sound production and especially bird movement, score counting etc. 

Here are the tests: [unit_test.py](https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/unit_test.py) links to - 
[test_this_nasty_bird.py](https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/test/test_this_nasty_bird.py)

## 6. Continuous Integration
Basically, there are standard delivery parts like [PyPI](https://pypi.org/) or usually Python-based website (e.g built on [Django](https://www.djangoproject.com/)). 
Unfortunately, my project has not neither of above mentioned delivery parts for understandable reasons. Thats why let's suppose that I  deliver my project just on github 
with all green/yellow 
values of the badges. So that all of them were green or at 
least yellow for such badges as test coverage.

My Pipeline: 
![pipeline](docs/pics/pipeline.png)

As you can see from this scheme [Travis-CI](https://travis-ci.com/yusif-ifraimo/FlapPy_Bird_SWT) is responsible for delivery on Linux and Appveyor for delivery on Windows

Travis-CI service sends reports after the unit tests 
to codecov.io and CodeClimate.com.
You can file details in **travis.yml** file
and in **appveyor.yml**, **tox.ini** file for Travis and AppVeyor respectively.

You can find Graddle report in **gradle_report.txt** file.

## 7. IDE 

I have used PyCharm as my IDE.

I used such plugins as:
* Ace Jump - to boost my productivity while writing, running and debugging code.
* IdeaVim - also to make development process a bit faster
* PlantUML - to draw UML diagrams
* Sonar Lint - to help me polish my code a little bit :)

Here are my most favorite shortcuts in PyCharm IDE:
* Search everywhere (**Double ⇧**) 
* Run Anything (**Double Ctrl**) 
* Commit and Push (**Ctrl+Alt+K**)
* Suggestions... (**Ctrl+⇧ Shift+A**)
* SmartType Code Completion (**Ctrl+⇧ Shift+Space**)

## 8. DSL
This part was quite tricky. Basically because of the PyGame. So the main problem with the PyGame is that it operates with seperate GUI. As in our case a small rectangular window. Basically, it is nearly [impossible](https://stackoverflow.com/questions/6044316/how-can-i-insert-a-console-in-to-a-pygame-window) to implement console within the GUI in order to type in our DSL commands. Especially, with such dynamic game as Flappy Bird where you must use PyGame's pygame.event.get() feature (and type in very fast). All this because ["Pygame is designed for making (graphical) games, so it only captures key presses when there is a window displayed."](https://stackoverflow.com/questions/9815995/read-console-input-using-pygame) <br>

**However**, there is one wonderfull thing. All games have a DSL in them since in order to 'speak' with the game you use specific key inputs and combinations. As in our case: (**q**), (**space**),(**space**+**1**), (**⇧**),(**esc**) etc. So that is a DSL Snippet!

But I thought that it would still be nice to include some sort of console DSL, so the user can put in commands there. As I said it is impossible to control the gamplay from the console, **but** it is possible to use Domain Specific Language for some of our game's settings! 

So I built a small DSL Snippet which allow user to set the mode of the game and then start to play the game. 

Below you will find demos.

**Running Game in Furry Off Mode trough DSL**
<p align="center">
  <img src="https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/docs/gifs/Python_DSL_Example_Furry_Mode_Off.gif">
</p>

The quality is bad so there is a
Full version of this gif in FULL HD format is available [here](https://youtu.be/S-9TUfrJY98) 

**Running Game in Furry On Mode trough DSL**
<p align="center">
  <img src="https://github.com/yusif-ifraimov/FlapPy_Bird_SWT/blob/master/docs/gifs/Python_DSL_Example_Furry_Mode_On.gif">
</p>

The quality is bad so there is a
Full version of this gif in FULL HD format is available [here](https://youtu.be/f7Xiq03kDbU) as well.


## 9. Functional Programming

* Final data structures

   A nice example of this would be tuples inside my  **Load Game**  class. 
   However, they can be ordinal variables as well if we would want to allow the user manipulate game's settings </br> (trough DSL for example).
    ```python
    class Load_Game:
          FPS = (31)
          SCREEN_SIZE = SCREENWIDTH, SCREENHEIGHT = (288, 512)
          PIPEGAPSIZE = (100) # gap between upper and lower part of pipe
          BASEY = (SCREENHEIGHT * 0.79)
    ```
* Side effect free functions

    An goood example:
    ```python
    def get_input(input):
        if input in moves():
            dir = moves()[input]
            bird.move(dir)
        elif input == 'q':
            return False
    return True
    ```

 * The use of higher order functions

    I have made a few examples below. 
     ```python
    def number(the_number, arg):
        return arg[0](the_number, arg[1]) if arg else the_number

    def zero (arg = None): return number(0, arg)
    def one  (arg = None): return number(1, arg)
    def two  (arg = None): return number(2, arg)
    def three(arg = None): return number(3, arg)
    def four (arg = None): return number(4, arg)
    def five (arg = None): return number(5, arg)
    def six  (arg = None): return number(6, arg)
    def seven(arg = None): return number(7, arg)
    def eight(arg = None): return number(8, arg)
    def nine (arg = None): return number(9, arg)


    def plus      (value): return int.__add__, value
    def minus     (value): return int.__sub__, value
    def times     (value): return int.__mul__, value
    def divided_by(value): return int.__floordiv__, value

    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3
     ```

* Functions as parameters and return values/anonymous functions

    When I was at school I often had to solve equastions like this:
    $ (a_1*x^2 + a_2^x + a_3) * x^2 + (a_4*x + a_5) * x + a_6 $
    ```python
    def quad(a, b, c):
        return lambda x: (a(x) if callable(a) else a)*(x ** 2) + \
                         (b(x) if callable(b) else b) * x + \
                         (a(x) if callable(c) else c)

    assert quad(0, 0, 3)(0) == 3
    assert quad(quad(1, 0, 0), quad(0, 2, 0), 3)(0) == 3
    ```

* Use Closures / Anonymous functions
    
    ```python
    def inputs():
        INPUTS = {'w': "up", 's': "down", 'x': "quit", 'p': "pause"}

        def function_inside():
            return INPUTS

        return function_inside()
   
   inputs()

    ```





