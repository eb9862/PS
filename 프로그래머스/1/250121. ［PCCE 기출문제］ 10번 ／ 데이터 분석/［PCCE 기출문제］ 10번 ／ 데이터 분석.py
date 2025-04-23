def find_index(ext: str) -> int:
    info_list = [ "code", "date", "maximum", "remain" ]
    l = len(info_list)
    for i in range(l):
        if info_list[i] == ext:
            return i
    return -1    

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    extract_index = find_index(ext)
    for d in data:
        if d[extract_index] < val_ext:
            answer.append(d)
    
    sort_index = find_index(sort_by)
    answer.sort(key=lambda x: x[sort_index])
    
    return answer