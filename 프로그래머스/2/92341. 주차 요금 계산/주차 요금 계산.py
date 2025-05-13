from collections import defaultdict

def calculate_minute(time_in: str, time_out: str) -> int:
    result = 0
    out_h = int(time_out.split(':')[0])
    in_h = int(time_in.split(':')[0])
    result += (out_h - in_h) * 60
    
    out_m = int(time_out.split(':')[1])
    in_m = int(time_in.split(':')[1])
    result += out_m - in_m
    return result

def solution(fees, records):
    answer = []
    io_times = dict()
    parking_times = defaultdict(int)
    
    for record in records:
        time_num_io = record.split()
        car_num = time_num_io[1]

        if time_num_io[2] == "IN":
            io_times[car_num] = (time_num_io[0], -1)
        else:
            parking_times[car_num] += calculate_minute(io_times[car_num][0], time_num_io[0])
            del io_times[car_num]
    
    for car_num in io_times.keys():
        parking_times[car_num] += calculate_minute(io_times[car_num][0], "23:59")
    
    car_nums = list(parking_times.keys())
    car_nums.sort()
    for car_num in car_nums:
        cost = 0
        t = parking_times[car_num]
        if t <= fees[0]:
            answer.append(fees[1])
            continue
        t -= fees[0]
        cost += fees[1]
        cost += (t // fees[2]) * fees[3]
        if t % fees[2] != 0:
            cost += fees[3]
        answer.append(cost)
    
    return answer