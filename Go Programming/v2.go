package main

import "fmt"

// Define a structure to represent the finite state machine
type FSM struct {
  currentState int
}

// Function to update the state of the finite state machine
func (fsm *FSM) updateState(input1, input2 int) {
  // Convert the inputs to a 2-bit integer
  input := input1<<1 | input2

  // Set the next state based on the current state and the inputs
  switch fsm.currentState {
  case 0:
    switch input {
    case 0:
      fsm.currentState = 0
    case 1:
      fsm.currentState = 1
    case 2:
      fsm.currentState = 2
    case 3:
      fsm.currentState = 3
    }
  case 1:
    switch input {
    case 0:
      fsm.currentState = 0
    case 1:
      fsm.currentState = 1
    case 2:
      fsm.currentState = 2
    case 3:
      fsm.currentState = 3
    }
  case 2:
    switch input {
    case 0:
      fsm.currentState = 0
    case 1:
      fsm.currentState = 1
    case 2:
      fsm.currentState = 2
    case 3:
      fsm.currentState = 3
    }
  case 3:
    switch input {
    case 0:
      fsm.currentState = 0
    case 1:
      fsm.currentState = 1
    case 2:
      fsm.currentState = 2
    case 3:
      fsm.currentState = 3
    }
  }
}

func main() {
  // Create a new finite state machine with initial state 0
  fsm := FSM{0}

  // Update the state of the finite state machine with input (1, 0)
  fsm.updateState(1, 0)

  // Print the current state of the finite state machine
  fmt.Println("Current state:", fsm.currentState)
}
