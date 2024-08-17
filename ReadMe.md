# 드론 얼굴 인식 및 번호판 OCR 프로젝트

이 프로젝트는 DJI Tello 드론을 사용하여 특정 인물의 얼굴을 인식하고, 차량 번호판을 OCR로 읽어 저장하는 시스템입니다.

## 주요 기능

1. 얼굴 인식: Teachable Machine으로 학습된 모델을 사용하여 특정 인물의 얼굴을 인식하고 바운딩 박스로 표시합니다.
2. 드론 제어: 키보드 입력을 통해 드론을 조종할 수 있습니다.
3. 번호판 OCR: 촬영된 이미지에서 차량 번호판을 인식하고 텍스트로 추출합니다.
4. 이미지 저장: 촬영된 이미지와 추출된 번호판 텍스트를 저장합니다.

## 사용된 기술

- Python
- OpenCV
- Keras
- DJITelloPy
- PyTesseract
- NumPy

## 설치 방법

1. 필요한 라이브러리 설치:
   ```
   pip install djitellopy opencv-python keras numpy pytesseract
   ```

2. Teachable Machine에서 학습한 모델 파일(`keras_model.h5`)과 라벨 파일(`labels.txt`)을 프로젝트 디렉토리에 위치시킵니다.

3. 얼굴 인식을 위한 Haar Cascade 파일(`haarcascade_frontalface_default.xml`)을 다운로드하여 프로젝트 디렉토리에 위치시킵니다.

## 사용 방법

1. DJI Tello 드론의 전원을 켜고 Wi-Fi로 연결합니다.

2. 다음 명령어로 프로그램을 실행합니다:
   ```
   python run.py
   ```

3. 키보드 컨트롤:
   - W/S/A/D: 전진/후진/좌/우
   - I/K/J/L: 상승/하강/좌회전/우회전
   - UP: 이륙
   - DOWN: 착륙
   - C: 사진 촬영
   - ESC: 프로그램 종료

4. 촬영된 이미지와 OCR 결과는 `LP_OCR` 폴더에 저장됩니다.

## 프로젝트 구조

- `run.py`: 메인 실행 파일
- `Drone.py`: 드론 제어 및 얼굴 인식 로직
- `OCR.py`: 번호판 OCR 처리
- `KBcon.py`: 키보드 입력 처리
- `face.py`: 얼굴 인식 테스트용 파일

## 주의사항

- 이 프로젝트는 교육 및 연구 목적으로만 사용해야 합니다.
- 드론 사용 시 관련 법규를 준수해야 합니다.
- 개인정보 보호에 유의하여 사용해야 합니다.

## 라이선스

이 프로젝트는 [MIT 라이선스](https://opensource.org/licenses/MIT)에 따라 라이선스가 부여됩니다.
