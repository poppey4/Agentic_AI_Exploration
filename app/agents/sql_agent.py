class SQLAgent:

    def generate_sql(self, question):

        prompt = f'''
        Convert the following business question into SQL.

        Question:
        {question}
        '''

        return prompt