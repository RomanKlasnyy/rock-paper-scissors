package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

var (
	options     []string
	defaultGame bool
	name        string
	score       int
	newRating   []string
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Enter your name: ")
	if scanner.Scan() {
		name = scanner.Text()
		fmt.Printf("Hello, %s\n", name)
	}

	file, err := os.Open("rating.txt")
	if err != nil {
		fmt.Println("File not found.")
	}
	defer file.Close()

	fileScanner := bufio.NewScanner(file)
	for fileScanner.Scan() {
		line := fileScanner.Text()
		lineList := strings.Split(line, " ")
		if name == lineList[0] {
			score, _ = strconv.Atoi(lineList[1])
		}
	}

	fmt.Println("Enter gestures (comma-separated, leave empty for default - rock,scissors,paper): ")
	if scanner.Scan() {
		gestures := scanner.Text()
		if gestures == "" {
			options = []string{"rock", "scissors", "paper"}
			defaultGame = true
		} else {
			options = strings.Split(gestures, ",")
		}
	}

	fmt.Println("Okay, let's start")

	if defaultGame || len(options)%2 != 0 {
		playGame(scanner)
	} else {
		playGame(scanner)
	}
}

func playGame(scanner *bufio.Scanner) {
	random := rand.New(rand.NewSource(time.Now().UnixNano()))

	for {
		fmt.Print("Enter your move: ")
		scanner.Scan()
		action := scanner.Text()
		cAction := options[random.Intn(len(options))]

		switch action {
		case "!exit":
			fmt.Println("Bye!")
			updateUser()
			return
		case "!rating":
			fmt.Println("Your rating: ", score)
			continue
		case "!help":
			helpOption()
			continue
		default:
			if contains(options, action) {
				halfList := (len(options) - 1) / 2
				actionId := index(options, action)
				cActionId := index(options, cAction)

				if action == cAction {
					fmt.Printf("There is a draw (%s) (+50 points)\n", action)
					score += 50
				} else if actionId+halfList <= len(options) {
					if cActionId > actionId && actionId >= cActionId-halfList {
						fmt.Printf("Sorry, but computer chose %s\n", cAction)
					} else {
						fmt.Printf("Well done. Computer chose %s and failed (+100 points)\n", cAction)
						score += 100
					}
				} else {
					if cActionId < actionId && actionId <= cActionId+halfList {
						fmt.Printf("Well done. Computer chose %s and failed (+100 points)\n", cAction)
						score += 100
					} else {
						fmt.Printf("Sorry, but computer chose %s\n", cAction)
					}
				}
			} else {
				fmt.Println("Invalid input. Type \"!help\" for help")
			}
		}
	}
}

func newUser() {
	file, err := os.OpenFile("rating.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		fmt.Println("An error occurred.")
	}
	defer file.Close()

	_, err = file.WriteString(name + " " + strconv.Itoa(score) + "\n")
	if err != nil {
		fmt.Println("An error occurred.")
	}
}

func updateUser() {
	file, err := os.Open("rating.txt")
	if err != nil {
		fmt.Println("An error occurred.")
	}
	defer file.Close()

	fileScanner := bufio.NewScanner(file)
	for fileScanner.Scan() {
		data := fileScanner.Text()
		dataList := strings.Split(data, " ")
		if name == dataList[0] {
			newRating = append(newRating, name+" "+strconv.Itoa(score))
		} else {
			newRating = append(newRating, data)
		}
	}

	writer, err := os.Create("rating.txt")
	if err != nil {
		fmt.Println("An error occurred.")
	}
	defer writer.Close()

	for _, s := range newRating {
		writer.WriteString(s + "\n")
	}
}

func helpOption() {
	gameType := "your optional version"
	if defaultGame {
		gameType = "classic version"
	}

	fmt.Printf("Hi, %s. You are playing %s of the game\n", name, gameType)
	fmt.Println("Your available options for the game are:")
	fmt.Println(options)
	fmt.Println()
	fmt.Println("To play a game, type one of the options")
	fmt.Println("The option beats the next half of options, but loses to the previous ones")
	fmt.Println("If you win, you get +100 points. Draw: +50 points. Lose: +0 points")
	fmt.Println()
	fmt.Println("Type \"!exit\" to exit your game. Your score will be added/updated to \"rating.txt\"")
	fmt.Println("Type \"!rating\" to get your current score")
	fmt.Println("Type \"!help\" to get this message one more time")
}

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func index(s []string, e string) int {
	for i, a := range s {
		if a == e {
			return i
		}
	}
	return -1
}
