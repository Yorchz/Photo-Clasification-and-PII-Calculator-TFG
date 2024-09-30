class Deserializer:
    """Deserializes data into objects."""

    @staticmethod
    def deserialize(data: dict, cls: type):
        questions_data = data['questions']
        combined_questions = {}

        for q in questions_data:
            combined_questions.update(q)

        return cls(**combined_questions)
