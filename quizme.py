import json
from pathlib import Path
from typing import List, Dict, Any
from ars.arcontroller import ARController
import argparse

"""
QuizMe: An adaptive quiz Command Line Interface (CLI) application.

This script allows users to take an adaptive quiz based on questions loaded from a JSON file.
It uses the Adaptive Review System (ARS) to manage the quiz session.
"""

def load_questions(file_path: Path)-> List[Dict[str,Any]]:
    """
    Load questions from a JSON file.

    Args:
        file_path (Path): Path to the JSON file containing quiz questions.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a quiz question.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as f:
            questions = json.load(f)
            return questions
    except FileNotFoundError:
        print(f"Error: Question file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        print("Error: Invalid JSON in question file invalid.json")
        raise

def run_quiz(name: str, questions: list[dict[str, Any]]):
    """
    Run the adaptive quiz session.

    Args:
        name (str): The name of the quiz taker.
        questions (List[Dict[str, Any]]): A list of dictionaries containing question data.
    """
    print(f"Welcome, {name}! Let's start your adaptive quiz session.")
    c = ARController(questions)
    c.start()

def main()->None:
    """
    Main function to set up and run the QuizMe CLI application.
    """
    p = argparse.ArgumentParser(description="")
    p.add_argument("name",help="Your name")
    p.add_argument("--questions",required=True, help= "path to the question data file.")

    a = p.parse_args()

    try:
        questions = load_questions(Path(a.questions))
        run_quiz(a.name, questions)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Exiting due to error in loading questions.")

if __name__ == "__main__":
    main()
