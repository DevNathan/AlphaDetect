# AlphaDetect

문자 분포(Alphabet Frequency) 데이터를 기반으로 텍스트의 언어 DNA를 추출하고 판별하는 경량화된 머신러닝 분류기입니다.

🔗 **Live Demo:** [AlphaDetect Web App](https://alphadetect-kc2vqc6tt2uwmcbcbem5qp.streamlit.app/)
📓 **Model Training (Colab):** [Jupyter Notebook](https://colab.research.google.com/drive/1s8i1kVEdblKCSZdQHqyZifrLWTrrJmtd#scrollTo=nmXT3jjHuFTH)

---

## 📌 Project Overview
AlphaDetect는 텍스트 내 26개 영문 알파벳의 출현 빈도를 계산하고 정규화하여, 해당 텍스트가 어떤 언어로 작성되었는지 판별하는 머신러닝 시스템입니다. 인간의 눈에는 보이지 않는 각 언어 고유의 알파벳 분포 패턴(Language DNA)을 Support Vector Machine (SVM)을 통해 시각화하고 분류합니다.

### 지원하는 언어 (Supported Languages)
* 영어 (English - en)
* 프랑스어 (French - fr)
* 인도네시아어 (Indonesian - id)
* 타갈로그어 (Tagalog - tl)

---

## 🛠️ Tech Stack
* **Language:** Python 3
* **Machine Learning:** Scikit-learn (SVM)
* **Data Processing:** Pandas, Collections
* **Web Framework:** Streamlit
* **Model Serialization:** Joblib

---

## 🚀 Features
1. **Real-time Language Detection:** 텍스트 입력 시 즉각적인 언어 판별.
2. **Language DNA Visualization:** 예측의 근거가 되는 알파벳 빈도수 데이터를 막대그래프로 시각화하여 제공.
3. **Statistical Defense Logic:** 통계적 유의성을 확보하기 위해 영문 알파벳 100자 미만의 데이터는 판별을 보류하여 시스템의 신뢰성 보장.

---

## ⚠️ Known Limitations & Future Works
본 프로젝트는 알파벳 개별의 빈도수(1-gram)를 독립 변수로 사용하는 통계적 모델의 특성과 한계를 가지고 있으며, 이를 개선하기 위한 향후 계획은 다음과 같습니다.
- 현 모델의 구조적 한계 (Limitations): 알파벳의 단순 출현 비율만을 계산하므로, 인도네시아어(id)와 타갈로그어(tl) 같이 동일한 어족(Austronesian)에 속하여 모음 'a' 등의 출현율이 유사한 언어의 경우, 짧은 문장에서 오분류가 발생할 수 있습니다. 이를 어느정도 방지하기 위해, 
- 향후 개선 방향 (Future Works): 언어 분류 엔진의 정밀도를 고도화하기 위해, 단일 알파벳이 아닌 문자의 연속성(Sequence)을 파악하는 Character N-gram 방식, 혹은 특정 희귀 패턴에 가중치를 부여하는 TF-IDF 파이프라인을 결합한 모델로 아키텍처를 업그레이드할 예정입니다.
