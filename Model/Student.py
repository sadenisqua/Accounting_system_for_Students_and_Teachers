from ORM.SQLConnector import SQLConnector


class Student:
    def __init__(self):
        self._record_id = None
        self._name = None
        self._group_id = None
        self._sql_connector = SQLConnector().select(table='student')

    def get_record_id(self):
        return self._record_id

    def set_record_id(self, record_id):
        self._record_id = record_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_group_id(self):
        return self._group_id

    def set_group_id(self, group_id):
        self._group_id = group_id
