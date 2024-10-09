class ConditionEvaluator:
    """Evaluates conditions in a controlled manner."""

    @staticmethod
    def evaluate_condition(condition: str, value: str) -> bool:
        """Evalúa manualmente las condiciones simples."""
        # Dividimos la condición por operadores que conocemos
        if "==" in condition:
            left, right = condition.split("==")
            print(f'Condición {type(right)} ==  Valor {value}')
            a = right.strip().strip('"').strip("'")
            print(f'Esta es la condicion con la q se compara {a}, y este su tipo {type(a)}')
            print(f'Este es el valor con el q se compara {value}, y este su tipo {type(value)}')
            # Comparamos si ambos lados son iguales
            return value == right.strip().strip('"').strip("'")
        else:
            raise ValueError(f"Condición no soportada: {condition}")