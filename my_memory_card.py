#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QMessageBox,QGroupBox,QButtonGroup
app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Memory Card')
lb_question=QLabel('Какой национальности не существует?')
btn=QPushButton('Ответить')
RadioGroupBox=QGroupBox('Варианты ответов')
ans_1=QRadioButton('Энцы')
ans_2=QRadioButton('Смурфы')
ans_3=QRadioButton('Чулымцы')
ans_4=QRadioButton('Алеуты')
layout_rbtn1=QHBoxLayout()
layout_rbtn2=QVBoxLayout()
layout_rbtn3=QVBoxLayout()
layout_rbtn2.addWidget(ans_1)
layout_rbtn2.addWidget(ans_2)
layout_rbtn3.addWidget(ans_3)
layout_rbtn3.addWidget(ans_4)
layout_rbtn1.addLayout(layout_rbtn2)
layout_rbtn1.addLayout(layout_rbtn3)
RadioGroupBox.setLayout(layout_rbtn1)
RadioGroup=QButtonGroup()
RadioGroup.addButton(ans_1)
RadioGroup.addButton(ans_2)
RadioGroup.addButton(ans_3)
RadioGroup.addButton(ans_4)
AnsGroupBox=QGroupBox('Результат теста')
a1=QLabel('Правильно/Неправильно')
a2=QLabel('Правильный ответ')
layout_res=QVBoxLayout()
layout_res.addWidget(a1, alignment=Qt.AlignLeft)
layout_res.addWidget(a2, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.show()
layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_line1.addWidget(lb_question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
layout_line2.addWidget(AnsGroupBox, alignment=Qt.AlignCenter)
AnsGroupBox.hide()
layout_line3.addWidget(btn,stretch=2)
layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
main_win.setLayout(layout_card)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    ans_1.setChecked(False)
    ans_2.setChecked(False)
    ans_3.setChecked(False)
    ans_4.setChecked(False)
    RadioGroup.setExclusive(True)
answer=[ans_1,ans_2,ans_3,ans_4]
def ask(question, right_answer, wrong1, wrong2,wrong3):
    shuffle(answer)
    answer[0].setText(right_answer)
    answer[1].setText(wrong1)
    answer[2].setText(wrong2)
    answer[3].setText(wrong3)
    lb_question.setText(question)
    a2.setText(right_answer)
    show_question()
def show_correct(res):
    a1.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')
ask('Государственный язык Бразилии:', 'Португальский', 'Английский', 'Испанский', 'Фрунцузский')
btn.clicked.connect(check_answer)
main_win.show()
app.exec()