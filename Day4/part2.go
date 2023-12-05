package main

import (
	"fmt"
	"log"
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
	additional_card := make(map[int]int)

	for i := 0; i < len(text); i++ {
		line := text[i]
		game := strings.Split(line, ":")
		game = strings.Split(game[1], "|")

		winning_numbers := strings.Fields(game[0])
		bingo_numbers := strings.Fields(game[1])
		total_wins := 0

		// Calculate winning numbers
		for i := 0; i < len(bingo_numbers); i++ {
			if bingo_numbers[i] != "" {
				// fmt.Println(bingo_numbers[i])
				for j := 0; j < len(winning_numbers); j++ {
					if bingo_numbers[i] == winning_numbers[j] {
						total_wins++
						// fmt.Println("Won one additional card")
						// fmt.Println("Winning number: ", bingo_numbers[i])

					}
				}
			}
		}
		tmp_array := make(map[int]int)
		total_cards := 0
		// Decrement each card
		for k, v := range additional_card {
			total_cards += v
			if k > 1 {
				tmp_array[k-1] = v
			}
		}
		additional_card = tmp_array
		additional_card[total_wins] += total_cards + 1
		delete(additional_card, 0)
		total += total_cards + 1

		// fmt.Println(additional_card)
	}
	fmt.Println(total)
}
