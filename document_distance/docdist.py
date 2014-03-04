#!/usr/bin/python
import math, string

### implement the following three functions ###

def get_counts(sorted_data):
  # Problem 1-7 Part (a)
  # wordCt = []
  # start = 0
  # endInd = len(sorted_data)-1
  # word = sorted_data[start]
  # counter = 0
  # while start < len(sorted_data):
  #   word = sorted_data[start]
  #   wordStopInd = findEndInd(sorted_data,word,(start,endInd))
  #   currWdCt = wordStopInd - start +1
  #   wordCt.append((word,currWdCt))
  #   start = wordStopInd +1
    
  #   counter += currWdCt

  # return wordCt
  # wordCt = []
  # currct = 0
  # currWd = sorted_data[0]
  # for data in range(len(sorted_data)):
  #   datawd = sorted_data[data]
  #   if ( datawd is not currWd) and data == (len(sorted_data)-1):
  #     wordCt.append((datawd,1))
  #   elif data == (len(sorted_data)-1):
  #     wordCt.append((datawd,currct+1))
  #   elif (datawd == currWd):
  #     currct += 1
    wordCt = []
    currct = 0
    currWd = sorted_data[0]

    for data in sorted_data:
        if currWd == data:
          currct += 1
        else:
            wordCt.append((currWd,currct))
            currct = 1
            currWd = data
    else:
        wordCt.append((currWd,currct))

    return wordCt
    # OHHH MY GOD THIS PROBLEM WHYYYYYYYYYYYY IT SHOULD BE SO EASY GOSH DARNIT HUFFFFFFF
    # if sorted_data[data] == currWd:
    #   currct = currct+1
    # elif data == len(sorted_data)-1:
    #   wordCt.append((sorted_data[-1],1))
    # else:
    #   wordCt.append((currWd,currct))
    #   currct = 0
    #   currWd = sorted_data[data]


# def findEndInd(sortArr,word,currange):
#   mid = (currange[0] + currange[1])//2
#   if currange[0] == currange[1]:
#     return mid
#   if sortArr[mid-1] == word and sortArr[mid] is not word:
#     return mid-1
#   elif sortArr[mid]==word and sortArr[mid+1]is not word:
#     return mid
#   elif sortArr[mid] ==word:
#     return findEndInd(sortArr,word,[mid,currange[1]+1])
#   elif sortArr[mid] is not word:
#     return findEndInd(sortArr,word,[currange[0],mid+1])
#   else:
#     return -1

def get_inner_product(counts1, counts2):

  innerProd = 0
  # wordArr = [x[0] for x in longer]
  # for ind in range(len(shorter)):
  #   curr = shorter[ind][0]
  #   if curr in wordArr:
  #       innerProd += shorter[ind][1] * longer[findWordInd(wordArr,curr)][1]
  # return innerProd
  oneInd = 0
  twoInd = 0
  while oneInd <= (len(counts1) -1) and twoInd <= (len(counts2)-1):
    if counts1[oneInd][0] == counts2[twoInd][0]:
      innerProd += counts1[oneInd][1] *counts2[twoInd][1]
      oneInd +=1
      twoInd +=1
    elif counts1[oneInd][0] > counts2[twoInd][0]:
      twoInd += 1
    else: 
      oneInd += 1
  
  return innerProd





def get_pairs(words):
  pairList = []
  for i in range(len(words)-1):
    pairList.append((words[i],words[i+1]))

  return pairList

### do no modify the following coding ###

translation_table =\
  string.maketrans(string.punctuation + string.uppercase,
                   " " * len(string.punctuation) + string.lowercase)

def main(path1, path2, use_pairs):
  theta = docdist(path1, path2, use_pairs)
  print "Angle between document vectors is %.3f radians.\n" % theta

def docdist(path1, path2, use_pairs):
  sorted_data1 = get_sorted_data(path1, use_pairs)
  sorted_data2 = get_sorted_data(path2, use_pairs)
  counts1 = get_counts(sorted_data1)
  counts2 = get_counts(sorted_data2)
  inner_product = get_inner_product(counts1, counts2)
  norm1 = get_inner_product(counts1, counts1)
  norm2 = get_inner_product(counts2, counts2)
  numerator = inner_product
  denominator = math.sqrt(norm1 * norm2)
  return math.acos(numerator / denominator)

def get_sorted_data(path, use_pairs):
  text = open(path).read()
  normalized_text = text.translate(translation_table)
  words = normalized_text.split()
  sorted_data = sorted(get_pairs(words) if use_pairs else words)
  return sorted_data

if __name__ == '__main__':
  import argparse, cProfile
  parser = argparse.ArgumentParser()
  parser.add_argument("--pairs", help="use pairs instead of words",
                      action="store_true")
  parser.add_argument("file1")
  parser.add_argument("file2")
  args = parser.parse_args()
  use_pairs = args.pairs
  cProfile.run("main(args.file1, args.file2, args.pairs)")
