import base64

def transform(file, name):
    data = open(file, 'rb')
    content = '{} = {}\n'.format(name, base64.b64encode(data.read()))
    data.close()

    with open('pic.py', 'a') as f:
        f.write(content)

if __name__ == '__main__':
    while True :
        print("路徑|名稱(英文開頭)")
        Path_Name = input().split('|')
        if len(Path_Name) == 1:
            path = Path_Name[0]
            if path == 'exit':
                break
        else:
            path = Path_Name[0]
            name = Path_Name[1]
            transform(path, name)