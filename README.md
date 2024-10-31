# QuizMe-CLI
Project Overview:
The QuizMe project is a Command Line Interface (CLI) application that provides an interactive quiz experience using an adaptive review system. Designed to help users reinforce their knowledge effectively, QuizMe adapts question order based on user performance, employing a hybrid Leitner system to focus on challenging topics and aid retention.

Objectives:
The objective of QuizMe is to develop a Python CLI application that:

1.Loads quiz questions from a JSON file.
2.Initiates quiz sessions with structured question prompts.
3.Processes user responses and delivers feedback.
4.Adjusts question difficulty and timing based on the user’s prior performance.
5.Adaptive Review System (ARS) Library
6.Central to the project is the Adaptive Review System (ARS) library, which supports the adaptive learning model. ARS organizes questions into a spaced repetition 
  system with five levels (boxes):

Box 0: For missed questions, reviewed after 60 seconds.

Box 1: For new, unasked questions.

Box 2: For questions answered correctly once, reviewed after 180 seconds.

Box 3: For questions answered correctly twice, reviewed after 360 seconds.

Box 4: For well-known questions, reviewed only when other boxes are empty.
