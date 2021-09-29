from ORM.SQLConnector import SQLConnector
from Model.Student import Student


class StudentController:
    def __init__(self):
        super().__init__()
        self.sql_connector = SQLConnector()

    def view(self) -> None:
        result = self.sql_connector.select(table='students')  # результ должен быть списком обьекта студент
        for record in result:
            print(f'id={record.id}; full_name={record.full_name};')
