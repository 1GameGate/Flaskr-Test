Memos = [[]]
def save(name, content, tag, date):
    if name == '':
        return False
    else:
        global count
        Memos.append([name,content,slice(tag), date, count])
        count += 1
        print(Memos)
    
def load(name):
    num = findIDbyName(name)
    if num == False:
        return False
    global count
    for i in range(1,count):
        if Memos[i][4] == int(num):
            return i
    return False
        
def slice(text):
    slicedText = text.split()
    return slicedText

def delete(name):
    num = findIDbyName(name)
    if num == False:
        return False
    for i in range(4):
        Memos[num][i] = ''
    
def findIDbyName(name):
    for i in range(1,len(Memos)):
        if Memos[i][0] == name:
            return Memos[i][4]
    return False

def detectOverlap(name):
    for i in range(1,len(Memos)):
        if Memos[i][0] == name:
            return False
    return True

def Modify(name,fixname,content,tag,date):
    for i in range(1,len(Memos)):
        if Memos[i][0] == name:
            if fixname != '':
                Memos[i][0] = fixname
            if content != '':
                Memos[i][1] = content
            if tag != '':
                Memos[i][2] = slice(tag)
            Memos[i][3] = date
            return True
    return False