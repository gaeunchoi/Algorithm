times = 0
for _ in range(5):
    intime, outtime = map(str, input().split())

    intime_h, intime_m = intime.split(":")
    outtime_h, outtime_m = outtime.split(":")

    h = int(outtime_h) - int(intime_h)
    m = int(outtime_m) - int(intime_m)

    if m < 0:
        h -= 1
        m = 60 + m

    times += 60*h + m

print(times)