#文件处理示例
import os


'''
description: 遍历删除指定文件夹
param {*} root 删除的目录
return {*}
'''
def delDir(path):
    for file in os.listdir(path):
        filename=path+"/"+file
        print("path:",filename)
        print(os.stat(filename))
        # 判断是否为目录
        if os.stat(filename)[0]==16384:
            print("path:",filename)
            delDir(filename)
        else:
            print("file:",filename)
            os.remove(filename)
    os.rmdir(path)
