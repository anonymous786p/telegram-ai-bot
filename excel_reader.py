import pandas as pd
from config import EXCEL_FILE


class ExcelReader:

    def __init__(self):

        # Read Excel without assuming the header row
        raw_df = pd.read_excel(EXCEL_FILE, header=None)

        header_row = None

        # Find the row containing "UID"
        for i, row in raw_df.iterrows():
            values = row.astype(str).tolist()

            if "UID" in values:
                header_row = i
                break

        if header_row is None:
            raise Exception("Could not find header row containing 'UID'.")

        # Read again using the correct header
        self.df = pd.read_excel(EXCEL_FILE, header=header_row)

        self.df = self.df.fillna("")
        self.df = self.df.astype(str)

        print(f"✅ Loaded {len(self.df)} rows.")
        print(f"✅ Columns: {list(self.df.columns)}")

    def get_all_data(self):
        return self.df

    def search(self, keyword):

        keyword = keyword.lower()

        result = self.df[
            self.df.apply(
                lambda row: row.astype(str)
                .str.lower()
                .str.contains(keyword)
                .any(),
                axis=1,
            )
        ]

        return result

    def get_by_uid(self, uid):

        uid = uid.strip().lower()

        result = self.df[
            self.df["UID"].str.lower() == uid
        ]

        return result

    def smart_search(self, question):

        question = question.lower()

        words = question.split()

        result = self.df

        for word in words:

            temp = result[
                result.apply(
                    lambda row: row.astype(str)
                    .str.lower()
                    .str.contains(word)
                    .any(),
                    axis=1,
                )
            ]

            if len(temp) > 0:
                result = temp

        return result