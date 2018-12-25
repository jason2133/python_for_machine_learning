from pandas import Series, DataFrame
import pandas as pd
import numpy as np

raw_data = {'first_name' : ['Jason', 'Estel', 'Amy', 'Leopold', 'John'],
            'last_name' : ['Lee', 'Kim', 'Son', 'Sim', 'Jeon'],
            'age' : ['21', '20', '19', '25', '23'],
            'city' : ['Suwon', 'Seoul', 'Incheon', 'New York', 'Gwangjoo']
            }

a = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city']) # columns 기준으로 프린트한다!
print(a)

print(DataFrame(raw_data, columns = ['first_name', 'city']))  # Coulmn 선택

print(DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city', "University"]))

b = DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city', "University"])
print(b.first_name)
print(b["first_name"])
# 위 두 줄은 같은 말이다
# Column 선택 -> Series 추출

print(a)
print(a.loc[0]) # loc - index location : index 이름
print(a["age"].iloc[1:]) # iloc - index position : index 숫자

del b["University"] # Column을 삭제함
print(b)

# DataFrame
c = {'Suwon' : {2017 : 580, 2018 : 690}, 'Seoul' : {2016 : 740, 2017 : 120, 2018 : 240}}
print(DataFrame(c))
# 이렇게 표를 만들어라!






