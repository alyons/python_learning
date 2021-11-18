def main():
  report = []
  with open('day1.txt') as f:
    for line in f:
      report.append(int(line))

  for item in report:
    other = 2020 - item
    if (other in report):
      print(item * other)

def secondary():
  report = []
  with open('day1.txt') as f:
    for line in f:
      report.append(int(line))

  for item in report:
    secondSum = 2020 - item
    for item2 in report:
      other = secondSum - item2
      if (other in report):
        print(item * item2 * other)

if __name__ == '__main__':
  secondary()