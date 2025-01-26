import yaml

from src.utils.ConditionEvaluator import ConditionEvaluator


class QuestionFlowManager:
    """Manages the flow of questions based on conditions."""

    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.flow_config = yaml.safe_load(file)

    def get_next_questions(self, current_question_key, answer):
        """Returns the list of questions a saltar si una condición se cumple."""
        current_flow = self.flow_config['question_flow'].get(current_question_key)

        if current_flow:
            for condition in current_flow.get('conditions', []):
                print(f'Condición a evaluar: {condition}')

                if ConditionEvaluator.evaluate_condition(condition['condition'], answer[0].lower()):
                    print(f'Condición {condition["condition"]} evaluada como verdadera con respuesta {answer[0]}')
                    return condition['skip_questions']
                else:
                        print(f'Condición {condition["condition"]} evaluada como falsa. No se saltan preguntas.')
        return None


