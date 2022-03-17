# package
# test;
#
# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.io.StringReader;
# import java.util.ArrayList;
# import java.util.Collections;
# import java.util.List;
# import java.util.StringTokenizer;
#
# public
#
a, b = map(int, input().split())

N = int(input())

num_list = []
sb = []
for _ in range(N):
    x, y, z = map(int, input().split())
    num_list.append([x, y, z])

    num_list.sort(key=lambda x:x[0])

    sambun = int(len(num_list) // 3)

    size = sambun + 1

    sumSambun = sambun

    while sumSambun < len(num_list):
        sb.append(num_list.index(sumSambun).append(" "))

        sumSambun += size

    sb.append("\n")

print(sb)