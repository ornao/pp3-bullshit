**Developer: Orna Reynolds**

💻 [Visit live website](https://pp3-bullshit.herokuapp.com/)

## About

This is a command-line version of the bluff card game Bullshit for 3 players. Many versions of this game exist and the classic game is best player in a group of people. 

The classic game generally have no rules and players can discard cards to communal pile in any order with any amount of matching cards. To add order to game, I added a question to get rid of certain card number each turn. 

The objective of the game is to be the first one to get rid of all your cards. 

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
      - [Users](#users)
      - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Enjoy a fun and straightforward card game 
- Have the option to view over the rules of the game or play game straightaway. 
- Possiblility log into an existing account that keeps track of results.

### Site Owner Goals

- Build a game that is simple and straightforward to use.
- Make sure players understand the goal of the game and how to achieve that 
- Design a game that provides user input and feedback to players while they play

## User Experience

### Target Audience

Those of all ages who enjoy card games and more specifically card bluffing games. 

### User Stories

### Users
1. I want the name of the game clearly displayed and have an idea how to play it from first look.
2. I want to quickly learn how to play the game before it starts.
2. I want to be able to read the rules of the game in depth also if I need more explanation

### Site Owner

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Flowchart


## Technologies Used

### Languages


### Frameworks & Tools


### Libraries

#### Python Libraries


#### Third Party Libraries


[Back to Table Of Contents](#table-of-contents)

## Features

[Back to Table Of Contents](#table-of-contents)

## Validation


## Testing


[Back to Table Of Contents](#table-of-contents)
## Bugs


## Deployment
1. Update requirements.txt file by using this command in the terminal Pip3 freeze > requirements.txt. This populates this file with necessary dependencies.
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment1.png">
</details>

2. Login to heroku and navigate to dashboard where have option to creat a new app
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment2.png">
</details>

3. Choose a unique name and select Europe as destination 
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment3.png">
</details>

4. Once app is created navigate to settings and press button “reveal config vars”
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment4.png">
<img src="assets/docs/screenshots/deployment5.png">
</details>

5. Add creds key and content from creds file as value
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment6.png">
</details>

6. Add port key and 800 value to to config var also
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment7.png">
</details>

7. Scroll down and add python build pack and save changes
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment8.png">
</details>

8. Add node.js build pack also. It is important to make sure python buildpack is added first and hence ontop of node.js buildpack. 
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment9.png">
</details>

9. Scroll back to top of page and click deploy tab
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deployment10.png">
</details>

10. From the deploy methods displayed select GitHub
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deploymen11.png">
</details>

11. Search for repo name and click connect to link the two up
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deploymen12.png">
</details>

12. Deploy from branch and follow link to deployed site after it loads
<details><summary>Screenshot</summary>
<img src="assets/docs/screenshots/deploymen13.png">
</details>

[Back to Table Of Contents](#table-of-contents)

## Credits

### Images


### Code


## Acknowledgements
