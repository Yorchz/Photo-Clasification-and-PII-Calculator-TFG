from src.config.config import CONFIG
from src.orchestrators.MainOrchestrator import MainOrchestrator

if __name__ == '__main__':
    orchestrator = MainOrchestrator(CONFIG, "blip_vqa", "vqav2")
    orchestrator.run()


