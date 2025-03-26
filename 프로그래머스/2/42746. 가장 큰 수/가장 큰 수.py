from functools import cmp_to_key

def solution(numbers):
    str_numbers = list(map(str, numbers))

    def compare(a, b):
        if a + b > b + a:
            return -1  # a가 b보다 앞에 있어야 함
        elif a + b < b + a:
            return 1   # b가 a보다 앞에 있어야 함
        else:
            return 0   # 두 경우가 같으면 순서 상관 없음
    
    str_numbers.sort(key=cmp_to_key(compare))
    
    result = ''.join(str_numbers)
    
    # 모든 숫자가 0인 경우 "0" 반환
    if result[0] == "0":
        return "0"
    return result



# def solution(numbers):
#     # 맨 앞자리가 높은 숫자 먼저 사용
#     # 맨 앞자리가 같으면, 그 다음 숫자가 있는경우와 없는 경우가 있으면, 그다음숫자가 앞에 숫자보다 작으면 있는거 먼저, 그 다음 숫자가 맨 앞자리보다 큰게 첫번째, 그다음은 그다음숫자가 없는게 두번째, 맨앞자리보다작은거 먼저 사용
#     # =>3이면 33으로 두고 3,30,34 => 33,30,34로 비교하면 됨, 1000이하니까 3번 곱하고 문자열 비교 (문자열은 33>300)
#     numbers = [str(num) for num in numbers]
#     answer = ''.join(sorted(numbers, key=lambda x: x*3, reverse=True))
#     return '0' if answer[0]=='0' else answer