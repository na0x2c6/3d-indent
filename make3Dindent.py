#!/usr/bin/env python3
import sys
import os

start = '{' # ネストの起点
end = '}' # ネストの終点
width = 20 # 改行幅

def make3Dindent(stream, reverse=False):
  depth = 0
  charcount = 0
  left = ''
  right = ' ' * depth # いまの浮かび具合（右側のテキストに適用）
  charcount = 0
  for line in stream: 
    for c in line:
      charcount += 1
      if(c == start):
        # 浮かび具合を上げる
        depth += 1
        left += c
        right += ' ' + c
      elif(c == end):
        # 浮かび具合を下げる
        depth -= 1
        left += c + ' '
        right += c
      else:
        left += c
        right += c

      if charcount >= width or c == "\n": # 改行処理
        left += "\n"
        right += "\n" + (' ' * depth)
        charcount = 0

  if charcount > 0:
    left += "\n"
    right += "\n"

  # 焦点補助のドット
  dot = ' ' * int(width / 2) + '●'
  left += dot
  right += dot

  if reverse:
    # 沈む
    return (right, left)
  else:
    # 浮かぶ
    return (left, right)

# 出力用
def printLeftRight(left, right):
  for (l, r) in zip(left.split("\n"), right.split("\n")):
    print (l + ((width - len(l)) * ' ') + '    ' + r)


if __name__ == '__main__':
  if len(sys.argv) == 1:
    (left, right) = make3Dindent(sys.stdin)
    printLeftRight(left, right)
  else:
    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
      print(input_file + ': not found')
      sys.exit(1)

    f = open(input_file)
    (left, right) = make3Dindent(f)
    f.close()
    printLeftRight(left, right)
