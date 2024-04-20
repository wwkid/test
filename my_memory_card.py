from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle
from random import randint

class Question():
    def __init__(
self, question, right_answer, 
wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def show_result():
    AnswerGroupBox.show()
    RadioGroupBox.hide()
    button.setText('Следующий вопрос')
    check_answer()

def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    main_win.number_question = randint(0, len(question_list))
    ask(question_list[main_win.number_question%len(question_list)])

def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answer_text.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

def check_answer():
    main_win.count_question += 1
    if answers[0].isChecked():
        resultQuestion.setText('Правильно')
        answer.setText('Вы молодец!')
    else:
        resultQuestion.setText('Неправильно')
        answer.setText('Правильный ответ: ' + answers[0].text()+f"\n Статистика правиельных ответов: {main_win.count_true_question}/{main_win.count_question}")


app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.number_question = 0
main_win.count_question = 0
main_win.count_true_question = 0




question_list = []
q1 = Question('Этот идентификатор, используемый для хранения значений в памяти компьютера?', 'Переменная', 'Класс', 'Функция', "Выражение")
question_list.append(q1)
q2 = Question('Это блок кода, который выполняет определенную операцию?',
'Функция', 'Массив', 'Объект', 'Интерфейс')
question_list.append(q2)
q3 = Question('Это конструкция, которую используют программисты для выполнения разных операций, в зависимости от условий?', 'Условное выражение', 'Рекурсия', 'Индекс', 'Поток')
question_list.append(q3)
q4 = Question('Это конструкция, позволяющая программе выполнять определенный блок кода многократно?', 'Цикл', 'Массив', 'Класс', "Объект")
question_list.append(q4)
q5 = Question('Это структура данных, позволяющая хранить множество элементов одного типа?', 'Масссив', 'Класс', 'Переменная', "Объект")
q6 = Question('Какая функция отвечает за вывод текста?', 'print', 'def', 'input', "turtle")
q7 = Question('Это шаблон или описание для создания объектов. Класс определяет свойства и методы, которые могут быть использованы объектами этого класса?', 'Класс', 'Шаблон', 'Рекурсия', "Аргумент")
q8 = Question('Это экземпляр класса, который имеет свои собственные значения свойств и может вызывать методы, определенные в классе?', 'Объект', 'База данных', 'Поток', "Сортировка")
q9 = Question('Это процесс преобразования сериализованных данных в исходный формат?', 'Десериализация', 'Шаблон проектирования', 'Шаблон', "База данных")
q10 = Question('Это процесс преобразования исходного кода программы в машинный код, который может быть выполнен компьютером?', 'Компиляция', 'Десериализация', 'Криптография', "Эмуляция")
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)



#Форма для вопроса
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

#Создание группы объектов для отображения результата
AnswerGroupBox = QGroupBox("Результат теста:")
resultQuestion = QLabel('Неправильно')
answer = QLabel('Правильный ответ')
answerLayout = QVBoxLayout()
answerLayout.addWidget(resultQuestion)
answerLayout.addWidget(answer, alignment=Qt.AlignCenter)
AnswerGroupBox.setLayout(answerLayout)



#Верхняя надпись. Сам вопрос
answer_text = QLabel('Какой национальности не существует?')
#Кнопка ответить
button = QPushButton('Ответить')
button.clicked.connect(start_test)

#Самый главный лэяут
total_layout = QVBoxLayout()
total_layout.addWidget(answer_text, alignment=Qt.AlignCenter)
total_layout.addWidget(answer_text, alignment=Qt.AlignCenter)
total_layout.addWidget(RadioGroupBox)
total_layout.addWidget(AnswerGroupBox)
total_layout.addWidget(button, alignment=Qt.AlignCenter)

AnswerGroupBox.hide()


main_win.setLayout(total_layout)

main_win.show()
app.exec_()