from datetime import timedelta
from typing import Optional
from .box import Box 
import logging
from .qtype.question import Question

class BoxManager:
    """Manages multiple boxes in the Adaptive Review System."""
    def __init__(self):
        """Initialize a new BoxManager instance.

        Creates predefined boxes with specific priority intervals:
        - "Missed Questions": 60 seconds
        - "Unasked Questions": 0 seconds (no delay)
        - "Correctly Answered Once": 180 seconds
        - "Correctly Answered Twice": 360 seconds
        - "Known Questions": timedelta.max
        """
        self._boxes = [Box(name = "Missed Questions", priority_interval= timedelta(seconds=60)),Box(name = "Unasked Questions", priority_interval= timedelta(seconds=0)),Box(name = "Correctly Answered Once",priority_interval= timedelta(seconds=180)),Box(name = "Correctly Answered Twice", priority_interval= timedelta(seconds=360)),Box(name = "Known Questions", priority_interval= timedelta.max)]
        self._question_location = {}

    
    def add_new_question(self, question):
        """Add a new question to the Unasked Questions box.

        Args:
            question (Question): The question to add.

        The question's ID is stored as a string key in the `_question_location` dictionary.
        """
        self._boxes[1].add_question(question)
        self._question_location[str(question.id)] = 1

    def move_question(self, question, answered_correctly):
        """Move a question based on whether it was answered correctly.

        Args:
            question (Question): The question to move.
            answered_correctly (bool): True if the question was answered correctly, False otherwise.

        Moves the question to a new box based on the current box and the correctness of the answer.
        Updates `_question_location` with the new index and logs the box counts.
        """
        i = self._question_location[str(question.id)]

        if answered_correctly:
            if i == 0:
                j = 2
            else:
                j = min(i + 1, len(self._boxes) - 1)
        else:
            j = 0

        self._boxes[i].remove_question(question)
        self._boxes[j].add_question(question)

        self._question_location[str(question.id)] = j

        self._log_box_counts()
    
    def get_next_question(self) -> Optional[Question]:
        """Determine and return the next question to present.

        Returns:
            Optional[Question]: The next question to present, or None if no question is available.

        Iterates through all boxes except the "Known Questions" box to find the next priority question.
        """
        for b in self._boxes[:-1]:
            q = b.get_next_priority_question()
            if q:
                return q
            
        return None

    def _log_box_counts(self):
        """Log the number of questions in each box by name and count.

        Useful for tracking the distribution of questions across the system.
        """
        for b in self._boxes:
            print(f"{b.name}: {len(b)} questions")