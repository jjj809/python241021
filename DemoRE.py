# DemoRE.py
#정규표현식 사용

import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "This is apple")
print(result.group())

result = re.search("\d{4}", "올해는 2024년")
print(result.group())

result = re.search("\d{5}", "우리동네는 52300")
print(result.group())



def is_valid_email(email):
    # 이메일 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
    # re.search() 함수를 사용하여 패턴 매칭
    # if re.search(pattern, email):
    #     return True
    # else:
    #     return False

# 테스트할 이메일 주소 샘플
email_samples = [
    "user@example.com",
    "user.name@example.co.kr",
    "user+tag@example.org",
    "user123@sub.example.com",
    "user@example",  # 잘못된 형식
    "user@.com",  # 잘못된 형식
    "user@example.",  # 잘못된 형식
    "user@exam ple.com",  # 잘못된 형식
    "사용자@example.com",  # 한글 사용
    "user@example.com."  # 마지막에 점
]

# 각 샘플에 대해 유효성 검사 실행
for email in email_samples:
    if is_valid_email(email):
        print(f"{email} : 유효한 이메일 주소입니다.")
    else:
        print(f"{email} : 유효하지 않은 이메일 주소입니다.")