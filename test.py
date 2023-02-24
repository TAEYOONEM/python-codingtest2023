# # terms = ["A 6", "B 12", "C 3"]
# # privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# # def solution(today, terms, privacies):
# #     answer = []
# #     terms_dic = {}
# #     pri_dic = {}
    
# #     for i in range(len(terms)) :
# #         terms_dic[terms[i][0]] = int(terms[i][2:])
# #     for i in range(len(privacies)) :
# #         pri_dic[privacies[i][11]] = []
# #         pri_dic[privacies[i][11]].append(int(privacies[i][:4]))
# #         pri_dic[privacies[i][11]].append(int(privacies[i][5:7]))
# #         pri_dic[privacies[i][11]].append(int(privacies[i][8:10]))


# #     return answer

# def dayCal(arr,t) :
#     result = arr
#     if result[1] + t <= 12 :
#         result[1] += t
#         result[2] -= 1
#         return result
#     else : 
#         result[0] += 1
#         result[1] = result[1] + t - 12  
#         result[2] -= 1
#         return result

# arr=[2021,5,2]
# t = 6
# print(dayCal(arr,t))

def solution2(n, lost, reserve):
    answer = 0
    student = [1] * n
    

    for i in lost :
        student[i-1] = 0
    for i in reserve :
        student[i-1] += 1
    
    for i in lost :
        if student[i-2] == 2 if i-2 in range(n) else student[i] == 2 if i in range(n) else None :
            student[i-1] += 1
            student[i] -= 1

    for i in range(n) :
        if student[i] <= 1:
            answer += 1


    return answer

n = 5
lost = [2, 4]
reserve = [1,3,5]

print(solution2(n, lost, reserve)) # return 5