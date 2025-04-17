# Web Services and Applications


This repository contains coursework for the semester three module, _Web Services and Applications_, part of the [Higher Diploma in Science in Computing in Data Analytics](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics) at [Atlantic Technological University](https://www.atu.ie/).

## Repository Structure


```WSAA-coursework/
├── assignments/       # WSAA Coursework assignments that accompany the weekly lectures
├── labs/              # WSAA Labs and extra work
├──.gitignore          # .gitignore file for this repository.
└── README.md          # Main repository overview (this file).
```

## assignments

Assignments make up 40% of the overall module grade. 

In addition to the 3 assignments listed below, two MCQ's were also part of the assessment. 

This directory contains the following assignments:

1. __assignment2-carddraw.ipynb__

    Using the [Deck of Cards API](https://deckofcardsapi.com/) write a Python program that shuffles a deck, draws five cards and prints the value and suit of each card.

    For extra marks, congratulate the user if the user draws a pair, triple or a straight. 

2. __assignment03-cso.py__

    Write a program that retrieves the dataset for the "Exchequer Account (Historical Series)" from [CSO.ie](data.cso.ie), and store it in a file named "cso.json".
    
    To locate the dataset: 

        Economy → Finance → Financial Indicators → Exchequer Account (Historical Series).

    [Link to cso.json](data\cso.json)

3. __assignment04-github.py__

    This script reads a file from a GitHub repository and replaces all instances of "Andrew" with my name, "Irene". The updated file is committed and pushed back to the repository.

    This is the [repository, wsaa-assignment4](https://github.com/IreneKilgannon/wsaa-assignment4) and [text.txt](https://github.com/IreneKilgannon/wsaa-assignment4/blob/main/text.txt) file used for this assignment.

    This assignment involves the creation and use of fine grain access tokens in GitHub. The access token is saved to a private file, config.py and imported into assignment04-github.py.

## Prerequisites

To run the files on your local system, the following must be downloaded and installed.

1. Download and install Anaconda. Anaconda is a Python distribution and comes with pre-installed packages. 

Please note that when installing Anaconda, it is important to check the two boxes for:
* Add Anaconda3 to my PATH environment variable.
* Register Anaconda3 as my default.

![Anaconda](https://github.com/IreneKilgannon/pands-project/blob/main/images/Anaconda.png)

2. Download and install [Visual Studio Code](https://code.visualstudio.com/).

3. Download and install [git](https://git-scm.com/downloads).

4. Install [Cmder](https://cmder.app/).

## Usage

Enter ``git clone https://github.com/IreneKilgannon/WSAA-coursework.git`` in Cmder or the terminal of Visual Studio Code to clone the repository.

## Get Help

Contact me at g00220627@atu.ie or alternatively [submit an issue](https://github.com/IreneKilgannon/wsaa/issues).