def get_file_path():
    global filepath
    global pagenum
    filepath = input("请输入目录文件地址：")
    pagenum = int(input("请输入页码第一页所在的PDF中的页数："))
    get_mother_path(filepath)
    read_file(filepath, pagenum)


def get_mother_path(path):
    global filename
    filename = path.split('.')[-2]


def read_file(path,num):
    content_last = ''
    with open(path, 'rb') as f:
        content = f.readlines()
        f.close()
    for c in content:
        tag = c.decode('utf8')
        tag_head = tag.split('@')[0:-1]
        tag_sum = int(tag.split('@')[-1]) + num-1  # 获取出结尾的数字,将数字加上页数等于实际的页数
        tag_new = tag_head[0].replace('#', '\t')  # 将#，@替换为制表符
        tag_last = tag_new + '\t' + str(tag_sum)
        content_last = content_last + tag_last + '\n'
    save_file(content_last)


def save_file(content):
    save_path = filename + '_已修改.txt'
    with open(save_path, 'wb') as f:
        f.write(content.encode('utf8'))
        f.close()


if __name__ == '__main__':
    get_file_path()
