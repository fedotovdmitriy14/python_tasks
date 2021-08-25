def ParseTime(time):
  am_or_pm = time[-2:]
  hours, minutes = map(int, time[:-2].split(':'))
  if am_or_pm == 'pm':
    result_time = hours * 60 + minutes + 12 * 60
  else:
    result_time = hours * 60 + minutes 
  return result_time



def TimeDifference(strArr):
  strArr = [ParseTime(i) for i in strArr]
  strArr.sort(reverse=True)
#   return strArr
  return min([strArr[i]-strArr[i+1] for i in range(len(strArr)-1)])
  
  # code goes here
  return strArr

print(TimeDifference(["10:00am", "11:45pm", "5:00am", "12:01am"]))
print(TimeDifference(["1:10pm", "4:40am", "5:00pm"]))   #230






def IsPalindrome(strParam):
  return strParam == strParam[::-1]

def PalindromeSwapper(strParam):
  if IsPalindrome(strParam):
    return strParam
  for i in range(len(strParam)-1):
    result = strParam[0:i] + strParam[i+1] + strParam[i] + strParam[i+2:]
    if IsPalindrome(result):
        return result
  return '-1'


    

PalindromeSwapper('kyaak')


def KUniqueCharacters(strParam):
  k = int(strParam[0])
  strParam = strParam[1:]
  result = []
  for i in range(len(strParam)):
    substring = strParam[i]
    unique_char = {strParam[i]}
    counter = i + 1
    while len(unique_char) < k and counter <= len(strParam)-1:
      if strParam[counter] in unique_char:
        substring += strParam[counter]
      else: 
        unique_char.add(strParam[counter])
        substring += strParam[counter]
      counter += 1
    result.append(substring+strParam[counter+1])
  print(result)
  return max(result)

print(KUniqueCharacters("3aabacbebebe"))