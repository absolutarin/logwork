package main

import (
	"fmt"
	"log"
	"os/exec"
)

func main() {
	command := exec.Command("exec", "pwd")
	out, err := command.CombinedOutput()
	if err != nil {
		log.Printf("command.Run() failed with error: %s", err)
	}
	fmt.Println("output: ", string(out))
}
