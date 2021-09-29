import os

from Controller.StudentController import StudentController


class InteractiveConsoleView:
    def __init__(self):
        self.student_controller = StudentController()

    @staticmethod
    def cls() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def execute(self) -> None:
        while True:
            print('Список доступных команд:\n1. Просмотреть записи\n2. Удалить записи\n3. Добавить записи\n4. Обновить '
                  'записи\n5. Выход')
            crud_choice = input()
            if crud_choice == '1':
                print('Список доступных команд:\n1. Студенты\n2. Группы\n3. Преподователи\n4. Предметы\n5. Назад\n6. '
                      'Выход')
                model_choice = input()
                print('Укажите тип выборки:\n1. Все записи\n2. Поиск по полю')
                select_type_choice = input()
                if model_choice == '1':
                    self.student_controller.view()
                if model_choice == '5':
                    InteractiveConsoleView()
                if model_choice == '6':
                    break
            if crud_choice == '5':
                break
        self.cls()
