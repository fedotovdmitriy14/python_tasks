# import re
#
# def HTMLElements(strParam):
#     result = []
#     while True:
#         match = re.search(r"<.*?>", strParam)
#         if match:
#             match = strParam[match.start():match.end()]
#             print(match)
#             strParam = strParam.replace(match, '')
#         else:
#             break
#
#     return strParam[match.start():match.end()]
#
#
#
#
#
# print(HTMLElements("<div><div><b></b></div></p>"))
# print(HTMLElements("<div>abc</div><p><em><i>test test test</b></em></p>"))


def ParseTime(time):
    am_or_pm = time[-2:]
    hours, minutes = map(int, time[:-2].split(':'))
    # if am_or_pm == 'pm':
    #   result_time = hours * 60 + minutes + 12 * 60
    # else:
    result_time = hours * 60 + minutes
    print(result_time)
    return result_time



def TimeDifference(strArr):
  strArr = [ParseTime(i) for i in strArr]
  strArr.sort(reverse=True)
  return min([strArr[i]-strArr[i+1] for i in range(len(strArr)-1)])

# keep this function call here
print(TimeDifference(["1:10pm", "4:40am", "5:00pm"]))
print(TimeDifference(["10:00am", "11:45pm", "5:00am", "12:01am"]))