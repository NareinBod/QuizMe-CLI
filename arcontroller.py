from typing import Any, Dict, List
from .boxmanager import BoxManager
from .qtype.shortanswer import ShortAnswer
from .qtype.truefalse import TrueFalse

class ARController:
    """Main controller for running an adaptive review session."""
    def __init__(self, question_data):
        """Initialize the Adaptive Review Controller.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        self._box_manager = BoxManager()
        self._initialize_questions(question_data)

    def _initialize_questions(self, question_data):
        """Initialize questions and place them in the Unasked Questions box.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        for q in question_data:
            q_type = q.get("type")
            try:
                if q_type == "shortanswer":
                    question = ShortAnswer(
                        question=q["question"], 
                        answer = q["correct_answer"], 
                        case_sensitive = q.get("case_sensitive", False))
                elif q_type == "truefalse":
                    question = TrueFalse(
                        question=q["question"], 
                        answer = q["correct_answer"], 
                        explanation = q.get("explanation", ""))
                else:
                    print(f"Unsupported question type: {q_type}. Skipping this question.")
                    continue
            
                self._box_manager.add_new_question(question)
        
            except KeyError as k:
                print(f"Missing required field for question: {k}. Skipping this question.")



    def start(self)->None:
        """Run the interactive adaptive review session."""
        print("Type 'q' at any time to quit the session.")

        while True:
            question = self._box_manager.get_next_question()
            if not question:
                print("All questions have been reviewed. Session complete!")
                break

            print(f"\n{question.ask()}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == "q":
                break
            
            try:

                if question.check_answer(user_answer):
                    print("Correct!")
                else:
                    print(question.incorrect_feedback())

                self._box_manager.move_question(question, question.check_answer(user_answer))
            except ValueError as e:
                print(f"Invalid input: {e}")

        print("Thank you, goodbye!")