def main():
  print('Dice Calculator')
  die = [1, 2, 3, 4, 5, 6]
  upgrade = 750
  one = 27
  two = 60
  three = 97
  four = 141
  five = 150

  dieSum = sum(die)
  
  print('Rolls for Upgrade: %5.2f' % ((upgrade / (dieSum / 6))))
  print('Rolls for +1: %5.2f' % (upgrade / ((dieSum + 1) / 6)))
  print('Rolls for +2: %5.2f' % (upgrade / ((dieSum + 2) / 6)))
  print('Rolls for +3: %5.2f' % (upgrade / ((dieSum + 3) / 6)))
  print('Rolls for +4: %5.2f' % (upgrade / ((dieSum + 4) / 6)))
  print('Rolls for +5: %5.2f' % (upgrade / ((dieSum + 5) / 6)))

if __name__ == '__main__':
  main()
