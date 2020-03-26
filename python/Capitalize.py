import string
def c(s):
  if len(s) == 0:
    return ""
  return s[0].upper() + s[1:]

def solve(s):
    return " ".join(map(c, s.split(" ")))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()