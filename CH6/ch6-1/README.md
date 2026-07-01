# 실습과제 1
### 예제에서 보듯이 반복문을 이용한 화소처리와 opencv함수를 이용한 처리의 연산시간의 차이가 크게 나는 이유를 설명하라.
Python에서 반복문을 이용한 화소 처리는 모든 화소를 Python 인터프리터가 하나씩 실행하므로 반복 실행에 따른 비용이 크게 발생한다. 반면 OpenCV 함수는 내부적으로 C/C++로 구현되어 있어 화소 처리를 컴파일된 코드에서 수행하므로 Python 반복문보다 훨씬 빠르게 실행된다. 따라서 동일한 화소 처리라도 OpenCV 함수를 사용할 경우 연산 시간이 크게 단축된다.

# 실습과제 2
<img width="514" height="478" alt="image" src="https://github.com/user-attachments/assets/d0b96581-01f0-49d0-be96-7cca07e6e2ea" />

# 실습과제 3
<img width="987" height="795" alt="image" src="https://github.com/user-attachments/assets/8fb62ca6-1e65-42ed-8fb3-3d8475daa5f7" />

# 실습과제 4
<img width="757" height="772" alt="image" src="https://github.com/user-attachments/assets/0bfd7235-2da4-4f4f-a81f-9b34da6516e2" />
