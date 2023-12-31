# Project Structure

## app.py

The starting point of the application.

## View

The View component is responsible for managing all user interface-related tasks and is further subdivided into three parts:

### Window

The Window is the root of the tkinter screen and contains all the major global variables, making it crucial for maintaining the application's state.

### Menu

The Menu section encapsulates all user inputs, such as selections and button clicks.

### Main

The Main section is dedicated to displaying results, including the generation of graphs and outputting the results.

## Controller

The Controller component is designed to house most of the application's logic, effectively separating the user interface from the underlying business logic. It also handles the output of results to the console.

## Output

The Output folder stores screenshots and images generated by the application for reference and documentation purposes.
