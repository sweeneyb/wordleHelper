package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func isLenFive(line string) bool {
	return len(line) == 5
}

func filter(scanner *bufio.Scanner, fn func(line string) bool) {
	for scanner.Scan() {
		line := strings.ToLower(scanner.Text())
		if fn(line) {
			fmt.Println(scanner.Text())
		}
	}
}

func sizeFive(line string) bool {
	return len(line) == 5
}

func contains(char rune) func(line string) bool {
	return func(line string) bool {
		return strings.ContainsRune(line, char)
	}
}

func containsAll(chars []rune) func(line string) bool {
	return func(line string) bool {
		for _, r := range chars {
			if !strings.ContainsRune(line, r) {
				return false
			}
		}
		return true
	}
}

func containsNoneOf(chars []rune) func(line string) bool {
	return func(line string) bool {
		for _, r := range chars {
			if strings.ContainsRune(line, r) {
				return false
			}
		}
		return true
	}
}

func and2(left func(string) bool, right func(string) bool) func(line string) bool {
	return func(line string) bool {
		return left(line) && right(line)
	}
}

func and(funcs ...func(string) bool) func(line string) bool {
	return func(line string) bool {
		for _, fn := range funcs {
			if !fn(line) {
				return false
			}
		}
		return true
	}
}

func notAt(char byte, location int) func(line string) bool {
	return func(line string) bool {
		return !(line[location] == char)
	}
}

func isAt(char byte, location int) func(line string) bool {
	return func(line string) bool {
		return (line[location] == char)
	}
}

func main() {
	file, err := os.Open("../words/words.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	// filter(scanner, sizeFive)
	// filter(scanner, and(sizeFive, contains('a')))
	// filter(scanner, and2(and2(sizeFive, containsNoneOf([]rune{'e', 's', 'h', 'p'})),
	// 	containsAll([]rune{'o', 'a'})))
	filter(scanner, and(sizeFive,
		containsNoneOf([]rune{'f', 'a', 'c', 'y'}),
		containsAll([]rune{'n'}),
		notAt('n', 2),
	))

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
