package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strings"
)

func main() {
	//hellow world
	filepath := "input.txt"

	content, err := os.ReadFile(filepath)
	if err != nil {
		log.Fatal(err)
		return
	}

	text := strings.Split(string(content), "\n")

	total := 0

	for i := 0; i < len(text); i++ {
		line := text[i]
		game := strings.Split(line, ":")
		game = strings.Split(game[1], "|")

		winning_numbers := strings.Fields(game[0])
		bingo_numbers := strings.Fields(game[1])
		total_wins := 0
		fmt.Println(game[1])

		for i := 0; i < len(bingo_numbers); i++ {
			if bingo_numbers[i] != "" {
				// fmt.Println(bingo_numbers[i])
				for j := 0; j < len(winning_numbers); j++ {
					if bingo_numbers[i] == winning_numbers[j] {
						total_wins++
						// fmt.Println("Winning number: ", bingo_numbers[i])

					}
				}
			}
		}
		if total_wins != 0 {
			// fmt.Print("Total wins: ", total_wins, "\n")
			total += int(math.Pow(2, float64(total_wins-1)))
			// fmt.Print("Total wins: ", total, "\n")
		}
	}
	fmt.Println(total)
}
