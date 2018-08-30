# Swiss Draw

This is a repository with programs to run Ultimate Frisbee tournaments with Swiss Draw. The program uses linear algebra to approximate team strength based on all the played games so far. This program will be used in <b>Slovenian High School League - ŠUL</b>. A similar system is used on tournaments such as Windmill Windup and G-Spot.

## How it works

Swiss draw is a tournament system that ranks teams or competitors based on their performance in all their games. Each team is given a score (i.e. *strength*) based on the difference in goals scored. After each round of Swiss draw, teams with similar strength are matched up in the next round. This non-eliminating competition style aims to give teams as many close matches as possible while not matching the same two teams twice.

Ideally for match *i*, the strengths of two competing teams, say team *j* and team *k*, would be equal to the number of goals each team scored. Since the number of games can vastly exceed the number of variables (number of teams), estimations have some error ***e***. We can express this in the following equation, where ***s*** are team strengths are ***g*** are the goals scores.

<p align="center">
  <img src="https://imgur.com/r4Ge9e1.png"><!--(g_{j}-g_{k}) = (s_{j}-s_{k}) + e_{i}-->
</p>

We can then generalize this into matrix form:

<p align="center">
  <img src="https://imgur.com/sBpS4rC.png"><!--d = As + \varepsilon -->
</p>

where ***d*** is the vector of the difference in goals scored in each match, ***s*** is the vector containing the variables (teams's strengths), ***e*** is the error vector and ***A*** is the incidence matrix of the matchups, where each row represents one match and the value in column ***j*** is **1** and in column ***k*** is **-1**, all other are **0**.

Our aim is to select the values ***s*** so that the error will be the smallest. We use [!ordinary least squares using projection]{https://en.wikipedia.org/wiki/Ordinary_least_squares#Projection} to find it. The goal is therefore to:

<p align="center">
  <img src="https://imgur.com/iGg50r2.png"><!--min \left \|d -As  \right \|^{2}-->
</p>

## Instructions

You need to have pandas package installed to read from Excel files. Use this command: python3 -m pip install --upgrade pandas
You need to have xlrd package installed to read from Excel files. Use this command: python3 -m pip install --upgrade xlrd

More instructions coming soon ...
