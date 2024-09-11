""" 크로아티안 알파벳  https://www.acmicpc.net/problem/2941 """
croatian_s = input()
croatian_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian_list:
    croatian_s = croatian_s.replace(i, "1")

print(len(croatian_s))