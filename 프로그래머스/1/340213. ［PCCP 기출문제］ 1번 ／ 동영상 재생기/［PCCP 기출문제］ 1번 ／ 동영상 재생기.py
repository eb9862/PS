def is_out_of_video_start(current_pos) -> bool:
    
    if current_pos[0] < 0:
        return True
    return False

def is_out_of_video_end(current_pos, video_len) -> bool:

    end_m = int(video_len.split(":")[0])
    end_s = int(video_len.split(":")[1])
    
    if current_pos[0] == end_m:
        return current_pos[1] > end_s
    elif current_pos[0] > end_m:
        return True
    return False

def is_op_range(current_pos, op_start, op_end) -> bool:
    
    current_m = current_pos[0]
    start_m = int(op_start.split(':')[0])
    end_m = int(op_end.split(':')[0])
    
    if current_m in range(start_m, end_m + 1):
        current_s = current_pos[1]
        start_s = int(op_start.split(':')[1])
        end_s = int(op_end.split(':')[1])
        
        if start_m == end_m:
            return start_s <= current_s and current_s <= end_s
        
        if current_m == start_m:
            return start_s <= current_s
        elif current_m == end_m:
            return current_s <= end_s
        else:
            return True
    return False

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    current_pos = [0, 0]
    
    current_pos[0] = int(pos.split(':')[0])
    current_pos[1] = int(pos.split(':')[1])
    
    if is_op_range(current_pos, op_start, op_end):
        current_pos[0] = int(op_end.split(':')[0])
        current_pos[1] = int(op_end.split(':')[1])
    
    for cmd in commands:
        if cmd == "prev":
            current_pos[1] -= 10
            if current_pos[1] < 0:
                current_pos[0] -= 1
                current_pos[1] += 60
        else:
            current_pos[1] += 10
            if current_pos[1] >= 60:
                current_pos[0] += 1
                current_pos[1] -= 60

        if is_out_of_video_start(current_pos):
            current_pos = [0, 0]

        if is_out_of_video_end(current_pos, video_len):
            end_m = int(video_len.split(":")[0])
            end_s = int(video_len.split(":")[1])
            current_pos = [end_m, end_s]

        if is_op_range(current_pos, op_start, op_end):
            current_pos[0] = int(op_end.split(':')[0])
            current_pos[1] = int(op_end.split(':')[1])

    
    if current_pos[0] < 10:
        answer += "0"
    answer += str(current_pos[0])
    answer += ":"
    if current_pos[1] < 10:
        answer += "0"
    answer += str(current_pos[1])
    
    return answer