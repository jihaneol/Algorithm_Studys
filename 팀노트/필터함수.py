users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
{'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
 {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},  
 {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
  {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]
def is_man(user):
    return user["sex"] == "M"

for man in filter(is_man, users):
    pass

{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'}
{'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'}
# 결과값

for woman in filter(lambda u: u["sex"] != "M", users):
   pass
{'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'}
{'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'}
{'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}
#결과값

def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
#응용 필터, 람다, 맵
a=input()    
print(solution(a))