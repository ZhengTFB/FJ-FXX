import time

#分割字符串
def fenge(fenge_word):
  fenge_word_n=len(fenge_word)-1
  fenge_list1=[]
  while fenge_word_n>=0:
    ff=fenge_word[fenge_word_n]
    fenge_list1.append(ff)
    fenge_word_n=fenge_word_n-1
  fenge_list1.reverse()
  return fenge_list1

#缓慢打印
def yanshi(sentence_yanshi,time_sentence_yanshi):
  n=len(sentence_yanshi)
  sentence_yanshi=fenge(sentence_yanshi)
  for i in sentence_yanshi:
    print(i,end='')
    time.sleep(time_sentence_yanshi)
  print()
