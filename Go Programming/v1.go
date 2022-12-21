package main

import "fmt"

// Define a structure to represent the finite state machine
type FSM struct {
  currentState int
}

// Function to update the state of the finite state machine
func (fsm *FSM) updateState(input1, input2 int) {
  // Set the next state based on the current state and the inputs
  if fsm.currentState == 0 {
    if input1 == 0 && input2 == 0 {
      fsm.currentState = 0
    } else if input1 == 0 && input2 == 1 {
      fsm.currentState = 1
    } else if input1 == 1 && input2 == 0 {
      fsm.currentState = 2
    } else if input1 == 1 && input2 == 1 {
      fsm.currentState = 3
    }
  } else if fsm.currentState == 1 {
    if input1 == 0 && input2 == 0 {
      fsm.currentState = 0
    } else if input1 == 0 && input2 == 1 {
      fsm.currentState = 1
    } else if input1 == 1 && input2 == 0 {
      fsm.currentState = 2
    } else if input1 == 1 && input2 == 1 {
      fsm.currentState = 3
    }
  } else if fsm.currentState == 2 {
    if input1 == 0 && input2 == 0 {
      fsm.currentState = 0
    } else if input1 == 0 && input2 == 1 {
      fsm.currentState = 1
    } else if input1 == 1 && input2 == 0 {
      fsm.currentState = 2
    } else if input1 == 1 && input2 == 1 {
      fsm.currentState = 3
    }
  } else if fsm.currentState == 3 {
    if input1 == 0 && input2 == 0 {
      fsm.currentState = 0
    } else if input1 == 0 && input2 == 1 {
      fsm.currentState = 1
    } else if input1 == 1 && input2 == 0 {
      fsm.currentState = 2
    } else if input1 == 1 && input2 == 1 {
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
