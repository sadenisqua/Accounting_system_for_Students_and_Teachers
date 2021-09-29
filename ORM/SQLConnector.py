import sqlalchemy


class SQLConnector:
    def __init__(self):
        connection_str = 'postgresql+psycopg2://postgres:7910dk123@localhost:5432/accounting_system'
        engine = sqlalchemy.create_engine(connection_str)
        self.connection = engine.connect()

    def insert(self, table, values, columns):
        pass

    def select(self, table, columns='*', conditions=None):
        query = 'SELECT ' + columns + 'FROM ' + table
        if conditions is not None:
            query += 'WHERE ' + conditions

        query += ';'

        return self.connection.execute(query)

    def update(self, table, columns, values, conditions=None):
        pass

    def delete(self, table, conditions):
        pass
