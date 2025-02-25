from collections import deque

def solution(points, routes):
    answer = 0
    
    robot_num = len(routes)
    robots_pos = [ (0, 0) for _ in range(robot_num)]
    robots_dest = [ (0, 0) for _ in range(robot_num)]

    routes_new = [ deque(routes[i]) for i in range(robot_num) ]
    def init_robot():
        for i in range(robot_num):
            
            start = routes_new[i].popleft() - 1
            robots_pos[i] = tuple(points[start])
            
            dest = routes_new[i].popleft() - 1
            robots_dest[i] = tuple(points[dest])
    
    init_robot()
    
    # check collision
    sets = set(robots_pos)
    for point in sets:
        if robots_pos.count(point) != 1:
            answer += 1
    
    while robot_num:
        
        # move
        for i in range(robot_num):
            r = robots_pos[i][0]
            c = robots_pos[i][1]
            dest_r = robots_dest[i][0]
            dest_c = robots_dest[i][1]
            
            if r != dest_r:
                if r < dest_r:
                    robots_pos[i] = (r + 1, c)
                else:
                    robots_pos[i] = (r - 1, c)
            else:
                if c < dest_c:
                    robots_pos[i] = (r, c + 1)
                else:
                    robots_pos[i] = (r, c - 1)
        
        # check collision
        pos_count = {}
        for pos in robots_pos:
            pos_count[pos] = pos_count.get(pos, 0) + 1
        
        for cnt in pos_count.values():
            if cnt != 1:
                answer += 1
        
        # check end
        end = []
        for i in range(robot_num):
            if robots_pos[i] == robots_dest[i]:
                if routes_new[i]:
                    # update dest
                    dest = routes_new[i].popleft() - 1
                    robots_dest[i] = tuple(points[dest])
                else:
                    end.append(i)

        for idx in sorted(end, reverse=True):
            robots_pos.pop(idx)
            robots_dest.pop(idx)
            routes_new.pop(idx)
        robot_num = len(robots_pos)
    
    return answer