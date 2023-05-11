import os

#0: staged 1: modified 2: untracked
def git_status():
    i = 0
    result = os.popen('git status').read()

    result_lst = []
    result_dict = {'0': [], '1':[], '2':[]}
    sentence = ""

    for word in result:
        if word == '\n':
            result_lst.append(sentence)
            sentence = ""
            continue
        if word == '\t':
            continue
        sentence += word

    if "On branch" in result_lst[i]:
        i += 2
    
    if "No commits yet" in result_lst[i]:
        i += 2

    if "Changes to be committed:" in result_lst:
        i += 2
        while True:
            if result_lst[i] == '':
                i += 1
                break
            word_lst = result_lst[i].split(' ')
            result_dict['0'].append(word_lst[4]) 
            i += 1
        
    if "Changes not staged for commit:" in result_lst:
        i += 3
        while True:
            if result_lst[i] == '':
                i += 1
                break
            word_lst = result_lst[i].split(' ')
            result_dict['1'].append(word_lst[3])
            i += 1
    
    if "Untracked files:" in result_lst:
        i += 2
        while True:
            if result_lst[i] == '':
                break
            result_dict['2'].append(result_lst[i])
            i += 1
    return result_dict


