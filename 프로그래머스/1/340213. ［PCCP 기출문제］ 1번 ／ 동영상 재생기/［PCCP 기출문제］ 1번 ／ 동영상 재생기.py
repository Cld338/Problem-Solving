def get_sec(m):
    ls = m.split(":")
    return int(ls[0])*60+int(ls[1])

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len_sec = get_sec(video_len)
    pos_sec = get_sec(pos)
    op_start_sec = get_sec(op_start)
    op_end_sec = get_sec(op_end)
    for cmd in commands:
        if op_start_sec <= pos_sec < op_end_sec:
            pos_sec = op_end_sec
        if cmd=="next":
            pos_sec += 10
        elif cmd=="prev":
            pos_sec -= 10
        if pos_sec < 0:
            pos_sec = 0
        if op_start_sec <= pos_sec < op_end_sec:
            pos_sec = op_end_sec
        if pos_sec > video_len_sec:
            pos_sec = video_len_sec
    answer = str(pos_sec//60).zfill(2)+":"+str(pos_sec%60).zfill(2)
    return answer