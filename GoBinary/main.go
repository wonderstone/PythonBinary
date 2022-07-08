package main

import (
	"C"
	"fmt"
	"log"
	"time"
)

//export helloWorld
func helloWorld() {
	log.Println("Hello World")
	// iter for 10 seconds
	for i := 0; i < 10; i++ {
		// convert int to string
		fmt.Println(i)

		// sleep for 1 second
		time.Sleep(time.Second)
	}
	fmt.Println("Hello, World!")
}

func main() {

}
