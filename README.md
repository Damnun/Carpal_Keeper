# 손목 터널 증후군 개선 보호대 - 카파키퍼 (Carpal Keeper)
아두이노와 파이썬을 이용한 손목 터널 증후군 개선 보호대입니다.
It is a wrist protector that helps improve Carpal Tunnel Syndrome symptoms using Arduino and Python.



# 손목 터널 증후군이란? (What is carpal tunnel syndrome?)
![image](https://user-images.githubusercontent.com/72370701/159734842-32304d24-5549-442d-af3f-5a6c6f45e621.png

손목 정중 신경(Median Nerve Compression)의 지속적인 압박으로 인해 손목 관절에서 정중 신경 포착(Median Nerve entrapment)이 발생하여 여러 증상을 동반한다.

![image](https://user-images.githubusercontent.com/72370701/159735130-748cf609-db86-44bb-b69f-5e4266feeb5c.png)



# 아이디어 구상 배경 (background of idea planning)

![image](https://user-images.githubusercontent.com/72370701/159734272-2e416d38-dc03-4b34-b12c-cb800c1bf9b5.png)

![image](https://user-images.githubusercontent.com/72370701/159734283-348160ed-f9bc-4876-8ab4-aeabf3781ead.png)

최근 스마트폰, 컴퓨터 등의 사용량 급증으로 손목 터널 증후군, 거북목 증후군, 안구 건조증 등을 겪는 인구가 많아지고 있다. 그 피해와 발생률은 IT업계 종사자들에게는 더욱 치명적이다.
이에, 질병에 힘들어 하는 사람들을 도울 방법을 생각하다 손목 터널 증후군의 증상을 개선할 수 있는 보호대를 생각하게 되었다.



# 보호대로 손목 터널 증후군을 개선할 수 있는가? (Can wrist protector improve wrist tunnel syndrome?)

안동과학대학과 김천대학에서 발간한 "수근관 증후군 환자의 테이핑, 초음파, AMCT 치료가 통증과 악력에 미치는 효과, 2008"을 찾아보면 테이핑, 초음파, AMCT 치료군 모두 치료 전에 비해 유의하게 통증이 감소하였다는 연구 결과가 있다.


# 보호대 모델 디자인 (wrist protector model design)
위 연구 결과에 맞게 테이핑 방식을 사용한 보호대를 제작하고, 보호대 내부에는 압력 감지 센서 (Force Sensing Registor)를, 외부에는 탈부착 가능한 전원 모듈을 추가하였다.

![카파키퍼 모듈 디자인](https://user-images.githubusercontent.com/72370701/159736972-e842abda-ed24-4c60-b55f-ebf4f4b25aa0.png)

![카파키퍼 착용시](https://user-images.githubusercontent.com/72370701/159736988-29b254a5-904c-48e9-a4d9-55025ea4f877.png)

![카피키퍼 밴드 내외부](https://user-images.githubusercontent.com/72370701/159737000-438a0415-301c-45db-8918-2ad741fe98f1.png)


# 카파 키퍼에 사용된 주요 기능 / 기술
- 시제품 제작에 있어 개발의 편의성과 호환을 위해 아두이노 우도 보드를 사용하였음.
- 버저와 LED, 압력감지센서(FSR) 등을 부착하였음.
- 아두이노 보드에서 보호대에서 전해지는 압력 센서를 데이터화 한 뒤, 파이썬 Mathplotlib 라이브러리   를 이용해 그래프로 표현한다.
- 실제 제품에는 블루투스나 와이파이를 이용한 무선 통신, 충전형 이온 전지, 원격 작동과 데이터 관리   가 가능한 플랫폼이나 어플리케이션, DB가 필요함


![image](https://user-images.githubusercontent.com/72370701/159737754-920b8523-8c25-4199-9fc6-2fceddcbf9b1.png)


# 카파 키퍼 작동 순서
![image](https://user-images.githubusercontent.com/72370701/159737842-c51e7259-6205-4644-89c4-f51602840cba.png)


# 카파 키퍼 실행 화면
![image](https://user-images.githubusercontent.com/72370701/159737885-75332d82-3cac-4a9a-ba9a-314a79cdd5e9.png)


# 제작 과정 실험 사진
![실험사진](https://user-images.githubusercontent.com/72370701/159738709-83b5dd88-60e2-4567-a83f-970c26d0318c.jpg)


# 시연 영상
https://youtu.be/YaL7QLNlIGQ
Carpal Keeper 시연 영상
실험자에게 게임을 플레이 시킨 후, 플레이 하는 동안 손목에 주어지는 압력값을 그래프로 나타내고 있음.
