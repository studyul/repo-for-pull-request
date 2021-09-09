def check_count(st,x):
    if st.count(x)>1:
        return False
    else:
        return True

# def first_non_repeating_letter(string):
#     if string=='':
#         return ''
#     mylist=list(string)
#     mylist = [elem for elem in mylist if (elem.isalpha() and mylist.count(elem.lower())+mylist.count(elem.upper())<2 or elem.isalpha()==False and mylist.count(elem)==1)]
#     print(mylist)
#     if mylist==[]:
#         return ''
#     return mylist[0]

# someones solution
# def first_non_repeating_letter(string):
#     for x in string:
#         if string.lower().count(x.lower()) == 1:
#             return x
#     return ''
#     #your code here

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""

# print(first_non_repeating_letter('should handle simple tests'))
# print(first_non_repeating_letter('stress'))
# print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter('sTreSS'))
# print(first_non_repeating_letter('stress'))
# print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('hello world, eh?'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))
# print('dsf, dsfds ,,dsf'.count(','))

