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

## 시스템 요구사항

- 운영체제: Linux (Ubuntu 18.04 LTS 이상 권장)
- Python 3.6 이상
- DJI Tello 드론
- 웹캠 (드론 카메라 대신 사용 가능)

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

<br/>
<br/>

# Drone Face Recognition and License Plate OCR Project

This project uses a DJI Tello drone to recognize specific individuals' faces and read vehicle license plates using OCR.

## Key Features
1. Face Recognition: Uses a model trained with Teachable Machine to recognize specific faces and mark them with bounding boxes.
2. Drone Control: Allows drone control through keyboard inputs.
3. License Plate OCR: Recognizes vehicle license plates in captured images and extracts the text.
4. Image Saving: Saves captured images and extracted license plate text.

## Technologies Used
- Python
- OpenCV
- Keras
- DJITelloPy
- PyTesseract
- NumPy

## System Requirements
- Operating System: Linux (Ubuntu 18.04 LTS or higher recommended)
- Python 3.6 or higher
- DJI Tello drone
- Webcam (can be used instead of drone camera)

## Installation
1. Install required libraries:
   ```
   pip install djitellopy opencv-python keras numpy pytesseract
   ```
2. Place the model file (`keras_model.h5`) and label file (`labels.txt`) trained in Teachable Machine in the project directory.
3. Download the Haar Cascade file (`haarcascade_frontalface_default.xml`) for face recognition and place it in the project directory.

## Usage
1. Turn on the DJI Tello drone and connect via Wi-Fi.
2. Run the program with the following command:
   ```
   python run.py
   ```
3. Keyboard controls:
   - W/S/A/D: Forward/Backward/Left/Right
   - I/K/J/L: Up/Down/Rotate Left/Rotate Right
   - UP: Takeoff
   - DOWN: Land
   - C: Take photo
   - ESC: Exit program
4. Captured images and OCR results are saved in the `LP_OCR` folder.

## Project Structure
- `run.py`: Main execution file
- `Drone.py`: Drone control and face recognition logic
- `OCR.py`: License plate OCR processing
- `KBcon.py`: Keyboard input handling
- `face.py`: Face recognition test file

## Precautions
- This project should be used for educational and research purposes only.
- Comply with relevant regulations when using drones.
- Use with caution regarding personal privacy protection.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).



## 라이선스

이 프로젝트는 [MIT 라이선스](https://opensource.org/licenses/MIT)에 따라 라이선스가 부여됩니다.
