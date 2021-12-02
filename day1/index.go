package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main(){
	file, err := os.Open("./input.txt")

	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	inputLst := make([]int, 0)
    
    for scanner.Scan() {
		i, err := strconv.Atoi( scanner.Text())
		if err != nil {
			// handle error
			fmt.Println(err)
			os.Exit(2)
		}
		inputLst = append(inputLst, i)
    }
	result_lst := make([]int, 0)
	for i := 0; i < len(inputLst) - 2; i++ {
		result_lst = append(result_lst, inputLst[i] + inputLst[i+1] + inputLst[i+2])
	}
	count := 0

	for i := 1; i < len(result_lst); i++ {
		if result_lst[i] > result_lst[i-1] {
			count += 1
		}
	}

	fmt.Println(count)

	




}