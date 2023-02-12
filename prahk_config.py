import os
import PySimpleGUI as sg

line = "——————————————————————————————————————————————————"


def print_line(word):
    print("————————————%s————————————" % (word))


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file = BASE_DIR + '\\config.txt'
print(file)
with open(file, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()
data = []
for line in lines:
    line = line.replace('\n', '')
    data.append(line)

print_line(data)
debug_status = "1" == data[2]
print(debug_status)

if __name__ == '__main__':
    sg.theme("LightGray1")
    colText = [[sg.Text('Esc')],
               [sg.Text('F2')],
               [sg.Text('F3')],
               [sg.Text('F4')],
               [sg.Text('~')],
               [sg.Text('1')],
               [sg.Text('2')],
               [sg.Text('3')],
               [sg.Text('4')],
               [sg.Text('5')],
               ]
    keyName = ["esc", "f2", "f3", "f4", "~", "1", "2", "3", "4", "5"]
    inputData = [data[3:12]]
    colInput = []
    dataNum = 3
    for i in keyName:
        print(i)
        print(data[dataNum])
        colInput.append(
            [sg.InputText(data[dataNum], key=i, s=(25, 3), tooltip="Premiere中对应效果预设的名字")])
        dataNum += 1

    frame = sg.Frame("", element_justification="center", layout=[
        [sg.Text('鼠标偏移 X'), sg.InputText(data[0], s=(4, 3), key="x", tooltip="X轴的偏移量，通常保持默认"),
         sg.Text('Y'), sg.InputText(
            data[1], key="y", s=(
                4, 3), tooltip="Y轴的偏移量"),
            sg.Checkbox("调试", default=debug_status, key="debug")],
        [sg.Column(colText, element_justification="center"), sg.Column(colInput, element_justification="center")],
    ])

    layout = [
        [frame],
        [sg.Button('教程', expand_x=True), sg.Button('保存', tooltip="保存配置文件", expand_x=True), sg.Button(
            '退出', expand_x=True)]
    ]

    window = sg.Window('配置修改', layout, font=('黑体', 15))
    while True:
        event, values = window.read()
        if event in (None, '退出'):
            break
        #if event in ("测试"):
            #print(colInput)
        if event in ("教程"):

        if event in ("保存"):
            if values["debug"]:
                debug = 1
            else:
                debug = 0
            data = [
                values["x"],
                values["y"],
                str(debug),
                values["esc"],
                values["f2"],
                values["f3"],
                values["f4"],
                values["~"],
                values["1"],
                values["2"],
                values["3"],
                values["4"],
                values["5"],
                ]
            x = 0
            for value in data:
                value = str(value) + "\n"
                data[x] = value
                x = x + 1
            print(data)
            with open(file, 'w', encoding='utf-8-sig') as f:
                f.writelines(data)
            sg.popup("配置文件已保存")
        print('你按下了按钮：', event)
    window.close()
