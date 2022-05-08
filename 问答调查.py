#库
import PySimpleGUI as sg
#

#布局
layout=[

    [sg.Text('请输入下列信息…^_^',key='-1-',font=('宋体',20),enable_events=True)],
    [sg.Text('名字：', font=('宋体')), sg.InputText('留鑫雨')],
    [sg.Text('年龄：',font=('宋体')), sg.InputText('12')],
    [sg.Text('性别：',font=('宋体')), sg.InputText('男')],
    [sg.Text('国籍：',font=('宋体')), sg.InputText('中国')],
    [sg.Text('职业：',font=('宋体')), sg.InputText('学生')],
    [sg.Button('确定'), sg.Button('取消')]

        ]

#窗口
sg.theme('LightBlue1')
windows=sg.Window('python GUI',layout)


#循环
while True:
    
    event,value=windows.read()

    if event == None:
        break
    if event == '确定':
        sg.Popup(value)
        print(value)
    if event == '取消':
        sg.Popup('-OK-')
        break
    if event == '-1-':
        sg.Popup('eeeeee')

#关闭
windows.close()