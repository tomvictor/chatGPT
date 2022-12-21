# 2 Bit finite state machine

## v1.go

This program defines a structure called FSM that has a single field: currentState. It also defines a method called updateState that takes two integer inputs and updates the state of the finite state machine based on the current state and the inputs.
In the main function, the program creates a new FSM structure with an initial state of 0, and then calls the updateState method with the inputs (1, 0). It then prints the current state of the finite state machine to the console.

## v2.go

This program uses bit conversion to convert the two inputs to a single 2-bit integer, and then uses a switch statement to update the state of the finite state machine based on the current state and the inputs. The switch statement is nested to allow for different transitions depending on the current state.
In the main function, the program creates a new FSM structure with an initial state of 0, and then calls the updateState method with the inputs (1, 0). It then prints the current state of the finite state machine to the console.

## v3.go

Here is a revised version of the 2-bit finite state machine program that uses functions, compositions, and a struct to improve code quality and reduce the number of lines.

