import pandas as pd


class QualityAgent:

    def validate(self, dataframe: pd.DataFrame):

        report = {
            "null_counts": dataframe.isnull().sum().to_dict(),
            "duplicate_rows": dataframe.duplicated().sum(),
            "row_count": len(dataframe)
        }

        return report