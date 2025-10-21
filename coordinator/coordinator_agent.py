from agents.frontend_agent import FrontendAgent
from agents.backend_agent import BackendAgent

class CoordinatorAgent:
    def __init__(self):
        self.frontend = FrontendAgent()
        self.backend = BackendAgent()

    def process_brief(self, brief: str):
        brief_lower = brief.lower()
        results = []

        # Check for UI or frontend clues
        if any(word in brief_lower for word in ["ui", "interface", "frontend"]):
            results.append(self.frontend.create_ui(brief))

        # Check for API or backend clues
        if any(word in brief_lower for word in ["api", "database", "backend"]):
            results.append(self.backend.create_api(brief))

        # If nothing matched, run both by default
        if not results:
            results.append(self.frontend.create_ui(brief))
            results.append(self.backend.create_api(brief))

        return " | ".join(results)
