from config import CONFIG
from src.orchestrators.MainOrchestrator import MainOrchestrator

if __name__ == '__main__':
    orchestrator = MainOrchestrator(CONFIG)
    orchestrator.run()
