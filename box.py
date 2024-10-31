from ars.qtype.question import Question
from typing import List,Optional
from datetime import datetime, timedelta
class Box:
    """Module for the Box class in the Adaptive Review System."""
    def __init__(self, name: str, priority_interval: timedelta):
        #Implement constructor here
        self._name = name
        self._questions = []
        self._priority_interval = priority_interval

    @property
    def name(self):
        """Returns the name of the box."""
        return self._name
    
    @property
    def priority_interval(self):
        """Returns the priority interval of the box."""
        return self._priority_interval
    
    def add_question(self, question):
        """Add a question to the box.

        Args:
            question (Question): The question to be added.
        """
        if question not in self._questions:
            self._questions.append(question)

    def remove_question(self, question: Question)->None:
        """Remove a question from the box.

        Args:
            question (Question): The question to be removed.
        """
        if question in self._questions:
            self._questions.remove(question)

    def get_next_priority_question(self)->Optional[Question]:
        """Return the next priority question if available.

        Returns:
            Optional[Question]: The next priority question or None if no priority question is available.
        """
        sorted_questions = sorted(self._questions, key = lambda q : q.last_asked)
        now = datetime.now()
        for q in sorted_questions:
            if  (now - q.last_asked) >= self._priority_interval:
                return q
            
        return None

    def __len__(self):
        """Return the number of questions in the box."""
        return len(self._questions)
    
    def __str__(self):
        """Return a string representation of the Box object."""
        return f"Box(name='{self._name}', questions_count={len(self._questions)})"
    
    

    
