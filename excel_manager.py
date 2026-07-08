from excel_reader import ExcelReader


class ExcelManager:

    def __init__(self):
        self.reader = ExcelReader()
        self.df = self.reader.get_all_data()

    def get_by_uid(self, uid):
        return self.reader.get_by_uid(uid)

    def search_anything(self, text):
        return self.reader.search(text)

    def get_projects(self):
        return self.df["Project Name"].unique().tolist()

    def get_employees(self):
        return self.df["Assigned to"].unique().tolist()

    def get_completed_tasks(self):
        return self.df[self.df["Progress"].astype(float) >= 1.0]

    def get_pending_tasks(self):
        return self.df[self.df["Progress"].astype(float) < 1.0]

    def get_statistics(self):

        total_tasks = len(self.df)

        completed = len(
    self.df[self.df["Progress"].astype(float) >= 1.0]
)

        pending = total_tasks - completed

        return {
            "total_tasks": total_tasks,
            "completed": completed,
            "pending": pending,
        }