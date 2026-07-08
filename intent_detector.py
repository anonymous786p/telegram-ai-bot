import re


class IntentDetector:

    def __init__(self, manager):

        self.manager = manager

    def detect(self, question):

        q = question.strip().lower()

        # UID
        if re.match(r"uid-\d+", q):
            return {
                "intent": "uid",
                "value": question.strip()
            }

        # completed
        if "completed" in q:
            return {
                "intent": "completed"
            }

        # pending
        if "pending" in q:
            return {
                "intent": "pending"
            }

        # statistics
        if "statistics" in q or "stats" in q:
            return {
                "intent": "statistics"
            }

        # employee names
        for employee in self.manager.get_employees():

            if employee.lower() in q:

                return {
                    "intent": "employee",
                    "value": employee
                }

        # project names
        for project in self.manager.get_projects():

            if project.lower() in q:

                return {
                    "intent": "project",
                    "value": project
                }

        return {
            "intent": "ai",
            "value": question
        }