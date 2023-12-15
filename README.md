# 🃏 Black Jack Project 🃏
Blackjack is a popular two-player card game that is played with a deck of standard playing cards around the world in casinos. The main criteria for winning this game are chance and strategy. The challenge of this game is to get as close to 21 points as possible without exceeding them. That is why it is also known as Twenty-One.
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#game-rules">Game Rules</a>
    </li>
    <li><a href="#code-explanation">About the code</a>
      <ol>Class Card</ol>
      <ol>Class Deck</ol>
      <ol>Class Hand</ol>
      <ol>Class Player</ol>
      <ol>Class BlackjackGame</ol>
    </li>
    <li><a href="#lets-play">Let's Play!</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## ♣️ About the project ♣️
Blackjack is a popular two-player card game that is played with a deck of standard playing cards around the world in casinos. The main criteria for winning this game are chance and strategy. The challenge of this game is to get as close to 21 points as possible without exceeding them. That is why it is also known as Twenty-One.

<!-- RULES -->
## ♥️ Game Rules ♥️ 
Before conducting the code we need to understand the rules of the game.
<ol>
    <li>
      <p>In blackjack, each player and dealer receives two cards.</p>
    </li>
    <li>
      <p>The player can then choose to “play” (request another card) or “stop” (keep on hold until a new request is made). The goal in this game is to keep the sum of all card points equal to 21 without exceeding it.</p>
    </li>
    <li><p>Face cards (i.e. Jack, Queen, and King) are worth 10 points, and Aces can be worth 11 points. If a player has more than 21 points then the player automatically loses the game.</p></li>
  </ol>

<!-- ABOUT THE CODE -->
## ♠️ Code explanation ♠️
<ol>
  <li>Class Card</li>
  <p>It is used to describe and get information about the card. Here we can find methods like get_numeric_value that return the value of each card and the method get_image that returns the proper photo from the image directory.</p>
  <li>Class Deck</li>
    <p>It is responsible for initializing the deck, including the shuffling and dealing method.</p>
  <li>Class Hand</li>
  <p>Initialize the hand: it should make a space for adding deal cards. The other method calculates the sum of the card's value.</p>
  <li>Class Player</li>
  <p>Initialize the player values - their name and Hand (cards they possess).</p>
  <li>Class BlackjackGame</li>
    <p>This class is the most important one as it uses all the other classes to initialize the game. It starts with initiating the player, the dealer, and the deck. It has a method to start a game giving both players two cards each. What is also needed is to determine important states of the game: player hit, dealer hit and most importantly to determine the winner according to the rules.</p>
</ol>


  <!-- LETS PLAY -->
## ♦️ Let's Play! ♦️
Try your hand against the dealer and enjoy the game - maybe it's your date to became millionaire 💲💲💲 
