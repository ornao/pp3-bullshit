**Developer: Orna Reynolds**

💻 [Visit live website](https://pp3-bullshit.herokuapp.com/)

## About

This is a command-line version of the bluff card game Bullshit for 3 players. Many versions of this game exist and the classic game is best played in a group of people. 

The classic game generally is played with relatively no rules and players can discard cards to communal pile in any order with any amount of matching cards. My game is played where the user can only discard one card at a time. 

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
    - [Manual Testing](#manual-testing)
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
- Design a game that asks for user input, validates and manipulates it and also providesnfeedback to players while they play

## User Experience

### Target Audience

Those of all ages who enjoy card games and more specifically card bluffing games. 

### User Stories

### Users
1. I want the name of the game clearly displayed and have an idea how to play it from first look.
2. I want to be asked if I want to start the game or read the rules first
3. I want to be able to start the game after I have read the rules of the game
4. I would like the cards in my hand to display as a graphic picture and for them to update when I play a card
5. I want to receive feedback from the game about the my inputs and have the opportunity ti input them again if I am wrong.
6. I want the option to play again once the game is over 
7. If I play the game multiple times, I want how many times I have won to be saved

### Site Owner
8. I want the back of the computer's cards to display as a graphic and for them to update when hand is updated. Seeing the front of the cards would ruin the game for the user because they would know if the computer was lying
9. I want the user to have the option to play the game again without having to exit. This is to enhance user experience.
10. I want the user's name and how many times they have won to be saved to google sheets.
11. I want user inputs to undergo extensive validation so game execution is not affected. 
12. 


[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Flowchart


## Technologies Used

### Languages

- Python

### Frameworks & Tools

- Git was used for version control
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Sheets](https://www.google.co.uk/sheets/about/) were used to store player usernames

### Libraries

#### Python Libraries

- os - used to add a seperate line to terminal underneath text
- random - used to shuffle deck, control computer choices of card selection and calling bullshit
- sys & sleep - used to create a typing effect within the games rules

#### Third Party Libraries

- [colorama](https://pypi.org/project/colorama/) - used this library to add color to the terminal to differenciate players
- gspread - used to add and manipulate data in my Google spreadsheet and to interact with Google APIs

[Back to Table Of Contents](#table-of-contents)

## Features

### Title screen 

- Provides name of game in pleasant graphic
- Gives short description of game to user has idea of what game is about immediately
- User stories covered:
 
<details>
    <summary>Screenshot</summary>

<img src = assets/docs/screenshots/titlescreen.png>
</details>

### Menu
- Gives user option to play the game or read the rules first
- User stories covered: 
  
<details>
    <summary>Screenshot</summary>

  <img src = assets/docs/screenshots/menuselect.png>

</details>

### Game rules
- Displays clear game rules
- Allows user to start game once they are ready
- User stories covered: 
  
<details>
    <summary>Screenshot</summary>

  <img src = assets/docs/screenshots/.png>
</details>

[Back to Table Of Contents](#table-of-contents)

## Validation

## Testing

### Manual Testing

#### Users stories
1. I want the name of the game clearly displayed and have an idea how to play it from first look.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Title screen | Press "Run Programme" | Users are greeted with graphic title and short explanation of game | Works as expected |

<details><summary>Screenshot</summary>
<img src = assets/docs/screenshots/titlescreen.png>
</details>

2. I want to be asked if I want to start the game or read the rules first

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Menu | Select 1 | Game begins | Works as expected |
| Menu | Select 2 | User is presented with rules | Works as expected |

<details><summary>Screenshots</summary>
  <img src = assets/docs/screenshots/menuselect.png>
  <img src = assets/docs/screenshots/option1.png>
  <img src = assets/docs/screenshots/option2.png>
</details>

3. I want to be able to start the game after I have read the rules of the game
4. I would like the cards in my hand to display as a graphic picture and for them to update when I play a card
5. I want to receive feedback from the game about the my inputs and have the opportunity ti input them again if I am wrong.
6. I want the option to play again once the game is over 
7. If I play the game multiple times, I want how many times I have won to be saved

#### Site Owner stories
8. I want the back of the computer's cards to display as a graphic and for them to update when hand is updated. Seeing the front of the cards would ruin the game for the user because they would know if the computer was lying
9. I want the user to have the option to play the game again without having to exit. This is to enhance user experience.
10. I want the user's name and how many times they have won to be saved to google sheets.
11. I want user inputs to undergo extensive validation so game execution is not affected. 
12. 



[Back to Table Of Contents](#table-of-contents)
## Bugs
| **Bug** | **Fix** |
| ------- | ------- |
| 
menu_select() bug: This function was not executing its if or else ==1,2 when incorrect value enter first followed by 1 or 2. | Fixed by setting the start_option_selected variable to input() to get the user's input and using this in loop rather than other value. See [commit ea2de49](https://github.com/ornao/pp3-bullshit/commit/ea2de49f39f90ae87ef3a2644ee9e6bde323bb87) for further details. |

---


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
