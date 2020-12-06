first_moment_hh = int(input())
first_moment_mm = int(input())
first_moment_ss = int(input())

second_moment_hh = int(input())
second_moment_mm = int(input())
second_moment_ss = int(input())

secs_first_moment = first_moment_hh * 3600 + first_moment_mm * 60 + first_moment_ss
secs_second_moment = second_moment_hh * 3600 + second_moment_mm * 60 + second_moment_ss

print(secs_second_moment - secs_first_moment)