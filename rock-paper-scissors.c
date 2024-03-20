#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_NAME_LENGTH 50
#define MAX_GESTURE_LENGTH 20
#define MAX_FILENAME_LENGTH 100

char* options[MAX_GESTURE_LENGTH];
int options_count = 0;
int defaultGame = 0;
char name[MAX_NAME_LENGTH];
int score = 0;
int newUser = 1;
char newRating[1000][MAX_NAME_LENGTH + 20];
int newRating_count = 0;

void playGame();

void newUserToFile();

void updateUserToFile();

void helpOption();

int main() {
    printf("Enter your name: ");
    fgets(name, MAX_NAME_LENGTH, stdin);
    name[strcspn(name, "\n")] = '\0'; // Remove trailing newline

    printf("Hello, %s\n", name);

    FILE *file = fopen("rating.txt", "r");
    if (file == NULL) {
        printf("File not found.\n");
    } else {
        char line[100];
        while (fgets(line, sizeof(line), file)) {
            char user[MAX_NAME_LENGTH];
            int user_score;
            sscanf(line, "%s %d", user, &user_score);
            if (strcmp(name, user) == 0) {
                newUser = 0;
                score = user_score;
                break;
            }
        }
        fclose(file);
    }

    char gestures[MAX_GESTURE_LENGTH * 20];
    printf("Enter your gesture options (separated by commas) or leave blank for default (rock,scissors,paper): ");
    fgets(gestures, sizeof(gestures), stdin);
    gestures[strcspn(gestures, "\n")] = '\0'; // Remove trailing newline

    if (gestures[0] == '\0') {
        options[0] = "rock";
        options[1] = "scissors";
        options[2] = "paper";
        options_count = 3;
        defaultGame = 1;
    } else {
        char* token = strtok(gestures, ",");
        while (token != NULL) {
            options[options_count] = token;
            options_count++;
            token = strtok(NULL, ",");
        }
    }

    printf("Okay, let's start\n");

    playGame();

    return 0;
}

void playGame() {
    srand(time(NULL));
    while (1) {
        printf("Enter your action: ");
        char action[MAX_GESTURE_LENGTH];
        fgets(action, sizeof(action), stdin);
        action[strcspn(action, "\n")] = '\0'; // Remove trailing newline

        char* cAction = options[rand() % options_count];

        if (strcmp(action, "!exit") == 0) {
            printf("Bye!\n");
            if (newUser) {
                newUserToFile();
            } else {
                updateUserToFile();
            }
            break;
        }

        if (strcmp(action, "!rating") == 0) {
            printf("Your rating: %d\n", score);
            continue;
        }

        if (strcmp(action, "!help") == 0) {
            helpOption();
            continue;
        }

        int halfList = (options_count - 1) / 2;
        int actionId = -1;
        int cActionId = -1;
        for (int i = 0; i < options_count; i++) {
            if (strcmp(options[i], action) == 0) {
                actionId = i;
            }
            if (strcmp(options[i], cAction) == 0) {
                cActionId = i;
            }
        }

        if (actionId != -1) {
            if (strcmp(action, cAction) == 0) {
                printf("There is a draw (%s) (+50 points)\n", action);
                score += 50;
            } else if ((actionId + halfList <= options_count) &&
                       (cActionId > actionId && actionId >= cActionId - halfList)) {
                printf("Sorry, but computer chose %s\n", cAction);
            } else if ((actionId + halfList > options_count) &&
                       (cActionId < actionId && actionId <= cActionId + halfList)) {
                printf("Sorry, but computer chose %s\n", cAction);
            } else {
                printf("Well done. Computer chose %s and failed (+100 points)\n", cAction);
                score += 100;
            }
        } else {
            printf("Invalid input. Type \"!help\" for help\n");
        }
    }
}

void newUserToFile() {
    FILE *file = fopen("rating.txt", "a");
    if (file != NULL) {
        fprintf(file, "%s %d\n", name, score);
        fclose(file);
    } else {
        printf("An error occurred.\n");
    }
}

void updateUserToFile() {
    FILE *file = fopen("rating.txt", "r");
    if (file != NULL) {
        char line[100];
        while (fgets(line, sizeof(line), file)) {
            char user[MAX_NAME_LENGTH];
            int user_score;
            sscanf(line, "%s %d", user, &user_score);
            if (strcmp(name, user) == 0) {
                sprintf(newRating[newRating_count], "%s %d\n", name, score);
            } else {
                strcpy(newRating[newRating_count], line);
            }
            newRating_count++;
        }
        fclose(file);

        file = fopen("rating.txt", "w");
        if (file != NULL) {
            for (int i = 0; i < newRating_count; i++) {
                fprintf(file, "%s", newRating[i]);
            }
            fclose(file);
        } else {
            printf("An error occurred.\n");
        }
    } else {
        printf("An error occurred.\n");
    }
}

void helpOption() {
    char gameType[100];
    if (defaultGame) {
        strcpy(gameType, "classic version");
    } else {
        strcpy(gameType, "your optional version");
    }
    printf("Hi, %s. You are playing %s of the game\n", name, gameType);
    printf("Your available options for the game are:\n");
    for (int i = 0; i < options_count; i++) {
        printf("%s\n", options[i]);
    }
    printf("\n");
    printf("To play a game, type one of the options\n");
    printf("The option beats the next half of options, but loses to the previous ones\n");
    printf("If you win, you get +100 points. Draw: +50 points. Lose: +0 points\n");
    printf("\n");
    printf("Type \"!exit\" to exit your game. Your score will be added/updated to \"rating.txt\"\n");
    printf("Type \"!rating\" to get your current score\n");
    printf("Type \"!help\" to get this message one more time\n");
}
