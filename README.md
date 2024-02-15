# Rock-Paper-Scissors
This is my first project with creating and reading an external file for data. Enter your name, get your score from rating.txt (ex. Roman 100), or start with 0 with a new name. Then choose how to play. Classic game - press Enter. Unusual game - enter elements clockwise, where element loses to the next element (win is counterclockwise). Use pictures as a reference.

# rules

Enter your name and elements for a game. If you don't play classic game, the written element loses to the next half of the elements, but wins against the previous half (clockwise, ignoring where's the end of the 'elements' list). If there are even number of elements, you get draw for playing against the opposite side of the element.

  - You get 100 points for a win;
  - You get 50 points for a draw;
  - You get 0 points for a lose;
  - Type `!rating` to get your current score;
  - Type `!exit` to end the current game series;
  - Type `!help` to get all commands you can type.

| Elements count | What should you type |
| ------ | ------ |
| 4 | rock,lizard,scissors,paper |
| 9 | rock,gun,water,air,paper,sponge,human,scissors,fire |
| 15 | rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire |

# warning

I updated the rating system. Now it automatically adds and updates the rating for new and old players. You need to have a 'rating.txt' file in the directory with at least one score (ex. 'Roman 100') and a new line! It reads the file to check if your name is in the rating. You can download this file here as an example.
