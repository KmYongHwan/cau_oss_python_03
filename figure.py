"""
그림과 관련된 함수 및 클래스를 제공하는 모듈입니다.
line class를 통해 선의 길이를 설정 및 참조를 수행하며
외부에서 접근 불가능한 __width와 __height가 있으면,
변수를 수정하고 접근하기 위해
set_length와, get_length 메소드를 제공합니다.
"""

import math

class line:
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """초기 width와 height 값을 입력합니다."""
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
            """선의 길이를 수정합니다."""
            self.__width = width
            self.__height = height

    def get_length(self):
        """저장된 선의 길이를 반환합니다."""
        return self.__width, self.__height

def area_rectangle(width, height):
    """길이를 입력받아 직사각형의 넓이를 구하는 함수입니다."""
    if width <= 0 or height <= 0: raise ValueError
    return width * height

def area_ellipse(width, height):
    """길이를 입력받아 타원의 넓이를 구하는 함수입니다."""
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi

def area_right_triangle(width, height):
    """길이를 입력받아 직삼각형의 넓이를 구하는 함수입니다."""
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2