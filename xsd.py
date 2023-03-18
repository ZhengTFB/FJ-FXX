def fenge(fenge_word):#分割字符串
  fenge_word_n=len(fenge_word)-1
  fenge_list1=[]
  while fenge_word_n>=0:
    ff=fenge_word[fenge_word_n]
    fenge_list1.append(ff)
    fenge_word_n=fenge_word_n-1
  fenge_list1.reverse()
  return fenge_list1

def vague(vague_fst_word,vague_sec_word):  #比较相似度
  vague_fst_word=fenge(vague_fst_word)
  vague_sec_word=str(vague_sec_word)
  vague_sec_word=fenge(vague_sec_word)
  #print(vague_sec_word,vague_fst_word)
  vague_return=0
  if len(vague_sec_word) >= len(vague_fst_word):  
    for vague_tt in vague_sec_word:
      for vague_rt in vague_fst_word:
        if vague_tt==vague_rt:
          vague_return=vague_return+1/(len(vague_sec_word)*len(vague_fst_word))
          #print(vague_return)
  if len(vague_sec_word) < len(vague_fst_word):
    for vague_tt in vague_fst_word:
      for vague_rt in vague_sec_word:
        if vague_tt==vague_rt:
          vague_return=vague_return+1/(len(vague_sec_word)*len(vague_fst_word))
  return vague_return
