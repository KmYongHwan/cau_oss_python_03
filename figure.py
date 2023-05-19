"""
그림과 관련된 함수 및 클래스를 제공하는 모듈입니다.
line class를 통해 선의 길이를 설정 및 참조를 수행하며
area_square, area_circle, area_regular_triangle 함수로
각각 정사각형, 원, 정삼각형의 넓이를 반환합니다.
"""

import math

class line:
    """선의 길이에 대해 저장하고 있는 클래스입니다."""
    __length = 0

    def __init__(self, length):
        """선의 길이를 받습니다.(length)"""
        self.__length = length

    def set_length(self,length):
            """선의 길이를 수정합니다."""
            self.__length = length

    def get_length(self):
        """저장된 선의 길이를 반환합니다."""
        return self.__length

def area_square(length):
    """길이를 입력받아 정사각형의 넓이를 구하는 함수입니다."""
    return length * length

def area_circle(length):
    """길이를 입력받아 원의 넓이를 구하는 함수입니다."""
    return length * length * math.pi

def area_regular_triangle(length):
    """길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다."""
    return length * length * math.sqrt(3) / 4