class ConditionEvaluator:
    """Evaluates conditions in a controlled manner."""

    @staticmethod
    def evaluate_condition(condition: str, value: str) -> bool:
        """Evalúa manualmente las condiciones simples."""
        if "==" in condition:
            left, right = condition.split("==")
            print(f'Condición {type(right)} ==  Valor {value}')
            return value == right.strip().strip('"').strip("'")
        else:
            raise ValueError(f"Condición no soportada: {condition}")