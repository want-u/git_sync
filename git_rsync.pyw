# -*- coding: utf-8 -*-
# @Author  : LuoXian
# @Date    : 2021/1/28 22:45
# Software : PyCharm
# version： Python 3.8
# @File    : git_rsync.py
import os
import sys
import base64
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

# *必填* 同步目录
dir_path = r'D:\MyNoteBook'

# 托盘图标
icon_path = os.path.join(dir_path, 'github.png')
if not os.path.exists(icon_path):
    with open(icon_path, 'wb') as f:
        data = b'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'
        f.write(base64.b64decode(data))

# 创建字典
item = {}
new_item = {}


# 获取文件修改时间
def get_mtimes():
    # 遍历目录
    dst_files = os.walk(dir_path)
    for i in dst_files:
        # 排除.git目录
        except_dir = '.git'
        if except_dir not in i[0].split('\\'):
            for each_file in i[2]:
                full_name = f'{i[0]}/{each_file}'
                # 获取文件的修改时间
                yield full_name, os.stat(full_name).st_mtime


# 初始化数据
def init_item():
    for each_file, each_mtime in get_mtimes():
        item[each_file] = each_mtime
    # git同步所需文件：bat和vbs
    bat_file = os.path.join(dir_path, 'git_push.bat')
    with open(bat_file, 'w', encoding='utf-8') as f:
        data = f'{dir_path[:2]}\ncd {dir_path}\ngit add -A && git commit -m "commit" && git pull origin master && git push origin master'
        f.write(data)
    vbs_file = os.path.join(dir_path, 'git_push.vbs')
    with open(vbs_file, 'w', encoding='utf-8') as f:
        data = f'Set Ws = CreateObject("Wscript.Shell")\nWs.Run("{bat_file}"),0'
        f.write(data)


# 检查字典是否更新
def check_file():
    global item
    for each_file, each_mtime in get_mtimes():
        new_item[each_file] = each_mtime

    if item != new_item:
        item = new_item.copy()
        # git同步
        os.popen(f'{os.path.join(dir_path, "git_push.vbs")}')
        tp.showMessage('Git同步程序', '文件已同步', icon=0)
        return 1
    else:
        return 0


if __name__ == '__main__':
    # pyqt窗口必须在QApplication方法中使用
    app = QApplication(sys.argv)
    # 关闭所有窗口,也不关闭应用程序
    QApplication.setQuitOnLastWindowClosed(False)

    # 添加托盘
    tp = QSystemTrayIcon()
    tp.setIcon(QIcon(icon_path))


    # 设置系统托盘图标的菜单: a1 和 a2
    # a1：打开对话框动作菜单
    def a1_fun():
        update = check_file()
        if not update:
            tp.showMessage('Git同步程序', '手动更新完成，当前无需更新', icon=0)


    a1 = QAction('&手动更新', triggered=a1_fun)


    # a2：关于动作菜单
    def a2_fun():
        tp.showMessage('Git同步程序', 'want-u制作的python小程序', icon=0)


    a2 = QAction('&关于作者', triggered=a2_fun)  # 直接退出可以用qApp.quit

    # a3： 退出菜单
    a3 = QAction('&退出托盘', triggered=qApp.quit)  # 直接退出可以用qApp.quit

    # 添加到托盘菜单
    tpMenu = QMenu()
    tpMenu.addAction(a1)
    tpMenu.addAction(a2)
    tpMenu.addAction(a3)
    tp.setContextMenu(tpMenu)

    # 不调用show不会显示系统托盘
    tp.show()

    # 运行数据函数
    init_item()

    # 信息提示
    # 参数1：标题
    # 参数2：内容
    # 参数3：图标（0没有图标 1信息图标 2警告图标 3错误图标），0还是有一个小图标
    tp.showMessage('Git同步程序', '文件数据已更新！', icon=0)

    # 每10s检测一次文件
    timer = QTimer()  # 初始化一个定时器
    timer.timeout.connect(check_file)  # 计时结束调用operate()方法
    timer.start(10000)  # 设置计时间隔并启动

    sys.exit(app.exec_())