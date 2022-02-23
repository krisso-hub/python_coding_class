# Put your code here
content = './texts/example.txt'

fileName = open(content, 'r')
file = fileName.read()
files = file.split()
files.sort()


def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

remove_dup(files)
for f in files:
   print(f)
