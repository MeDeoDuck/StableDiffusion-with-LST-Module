# StableDiffusion-with-LST-Module
Text2Image 모델의 학습 효율성 증대를 위해 LDM에 LST모듈 추가
논문 작성을 위해 연구 진행

# Introduction
생성형 모델이 대용량 데이터를 학습 시 시간 및 메모리 비용이 급증하게 된다.
이를 해결하기 위해, PETL방법 중 하나인 Ladder Side Tuning을 활용해 학습 효율성을 증대시킨다

# 논문 작성 가능 조건
LoRA보다 성능 좋아야됨

# 결과
기존 모델 대비 메모리 효율이 28.6% 향상하였고, 학습 시간도 1000 에포크 기준 절반 아래 감소
하지만, LoRA보다 성능 향상률 적음
