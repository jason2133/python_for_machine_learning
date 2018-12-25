# import os
# for file in os.listdir("C:\\Users\\선호\\Desktop\\naver_data\\naver_python\\naver_python\\codes\\ch_1\\news\\news_data"):
#     if file.endswith(".txt"): #끝이 ".txt"로 끝나는 경우
#         print(file)

# C:\Users\선호\\\Desktop\naver_data\naver_python\naver_python\codes\ch_1\news\news_data
# \\를 이렇게 2개씩 붙이면 된다

# 왜 위에껀 되고 밑에껀 안될까 ㅜ 일단 넘어가보자

import os

def get_file_list(dir_name):
    return os.listdir(dir_name)

print(get_file_list('C:\\Users\\선호\\Desktop\\naver_data\\naver_python\\naver_python\\codes\\ch_1\\news\\news_data'))

if __name__ == "__main__" :
    dir_name = "C:\\Users\\선호\\Desktop\\naver_data\\naver_python\\naver_python\\codes\\ch_1\\news\\news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    print(file_list)
    # 폴더명이랑 파일명을 join 시켜주었다
    # 폴더명이랑 파일명이 붙어서 같이 프린트가 된다.
    print(len(file_list)) #그럼 개수가 나오겠지

# 요기까지가 파일 불러오기

def get_contents(file_list):
    y_class = []
    x_text = []
    class_dict = {1: "0", 2: "0", 3: "0", 4: "0", 5: "1", 6: "1", 7: "1", 8: "1"}

    for file_name in file_list:
        try:
            f = open(file_name, "r", encoding="cp949")
            category = int(file_name.split(os.sep)[1].split("_")[0])
            y_class.append(class_dict[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class

# 파일별로 내용읽기
# X_text는 그 파일에 들어가 있는 말들을 프린트해주고
# y_class는 이게 0이냐 1이냐 프린트해줌. 즉 0은 40개고 1은 40개겠지

def get_cleaned_text(text):
    import re
    text = re.sub('\\+', '', text.lower() )
    return text

print(get_cleaned_text("I'm"))
# 문장부호를 없애주고 소문자로 바꿔주는 역할을 해줌
# 소문자로 바꿔주고 의미없는 것들을 없애줌








