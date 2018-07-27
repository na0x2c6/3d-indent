#!/usr/bin/env python3
import sys
import os

start = '{' # ネストの起点
end = '}' # ネストの終点
width = 20 # 改行幅

def make3Dindent(stream, reverse=False):
  depth = 0 # いまの浮かび具合（右側のテキストに適用）
  depthList = [] # 行ごとの浮かび具合の管理
  leftLines = []
  rightLines = []
  for line in stream: 
    charcount = 0
    left = ''
    right = ''
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
      elif charcount >= width or c == "\n": # 改行処理
        pad = (width - charcount) * ' '
        leftLines.append(left + pad)
        rightLines.append(right + pad)
        depthList.append(depth)
        left = ''
        right = ''
        charcount = 0
        continue
      else:
        left += c
        right += c

  if charcount > 0:
    leftLines.append(left)
    rightLines.append(right)
    depthList.append(depth)

  maxDepth = max(depthList)

  retRight = []
  retLeft = []

  for (l, r, d) in zip(leftLines, rightLines, depthList):
    retLeft.append((' ' * (maxDepth - d)) + l)
    retRight.append((' ' * d) + r)

  # 焦点補助のドット
  pad = ' ' * int(width / 2)
  dotLine = pad + '●' + pad
  retLeft.append(dotLine)
  retRight.append(dotLine)

  if reverse:
    # 沈む
    return (retRight, retLeft)
  else:
    # 浮かぶ
    return (retLeft, retRight)

# 出力用
def printLeftRight(left, right):
  for (l, r) in zip(left, right):
    print (l + '    ' + r)


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
