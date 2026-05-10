class GovernanceAgent:

    def capture_metadata(self, table_name, columns):

        metadata = {
            "table_name": table_name,
            "columns": columns
        }

        return metadata