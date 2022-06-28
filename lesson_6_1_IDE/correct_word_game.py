# def check_word(s, q):
#    Q = list(s.upper())
#    S = list(q.upper())
#    result = []
#    for i in range(len(S)):
#       if S[i] == Q[i]:
#          result.append("correct")
#          Q[i] = None
#       else:
#          flag = True
#          for j in range(len(Q)):
#             if S[i] == Q[j]:
#                result.append("present")
#                Q[j] = None
#                flag = False
#          if flag:
#             result.append("absent")
#    return result
#
# print(check_word("COVER", "CLEAR"))
# print(check_word("ABBA", "AAAA"))