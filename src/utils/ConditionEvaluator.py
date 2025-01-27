class ConditionEvaluator:

    @staticmethod
    def evaluate_condition(condition: str, value: str) -> bool:
        """Evalúa manualmente las condiciones simples."""
        if "==" in condition:
            left, right = condition.split("==")
            a = right.strip().strip('"').strip("'")
            print(f'Condición {a} ==  Valor {value} \n')
            return value == right.strip().strip('"').strip("'")
        else:
            raise ValueError(f"Condición no soportada: {condition}")