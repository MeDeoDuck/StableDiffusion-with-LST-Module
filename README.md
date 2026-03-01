# StableDiffusion-with-LST-Module
Text2Image 모델의 학습 효율성 증대를 위해 LDM에 LST모듈 추가
Backbone 모델: [‘High-Resolution Image Synthesis with Latent Diffusion Models’](https://github.com/CompVis/latent-diffusion)

## Introduction
생성형 모델이 대용량 데이터를 학습 시 시간 및 메모리 등의 비용 급증

이를 해결하기 위해, PETL방법 중 하나인 Ladder Side Tuning을 활용해 학습 효율성 향상 시도

업로드한 코드들은 백본 모델에 수정한 부분만 업로드

## Features
<img width="625" height="592" alt="image" src="https://github.com/user-attachments/assets/bbb0bfae-768a-4c67-b2ea-262d61ce0a5f" />

백본 모델의 각 블록은 freezing한 후, 사이드 네트워크를 연결해 추가 파라미터만 학습 

자세한 설명은 [블로그](https://blog.naver.com/deoduck92/224200035002) 참고

## Result
<img width="1072" height="164" alt="image" src="https://github.com/user-attachments/assets/2d17fa05-e88c-479b-871e-2f1343fa1241" />

기존 모델 대비 메모리 효율이 28.6% 향상하였고, 학습 시간도 1000 에포크 기준 절반 아래 감소
