# 🏗️ Project Structure & Naming Rules

## 1. 디렉토리 구조
```text
📦 Root Directory
 ┣ 📂 database/        # 데이터베이스 초기 스키마 및 마이그레이션/SQL 스크립트
 ┣ 📂 config/          # 시스템 환경 설정 및 모델 하이퍼파라미터 관리
 ┣ 📂 docs/            # 프로젝트 기획 문서, 회의록 및 각종 산출물 보관
 ┣ 📂 mlflow/          # 모델 실험 결과, 파라미터 기록 및 아티팩트 관리 (Experiment Tracking)
 ┣ 📂 notebooks/       # EDA 및 실험용 코드 (개인 영문명 폴더 생성 후 작업 필수!)
 ┣ 📂 pipeline/        # 데이터 전처리, 모델 학습 및 추론을 위한 핵심 ML 파이프라인 로직
 ┣ 📂 streamlit/       # Streamlit 기반 UI/UX 서비스 레이어
 ┣ 📜 .gitignore       # Git 추적 제외 파일 설정
 ┣ 📜 LICENSE          # 프로젝트 라이선스 명시
 ┣ 📜 README.md         # 프로젝트 메인 설명서
 ┗ 📜 docker-compose.yml # 멀티 컨테이너 서비스(App, DB, MLflow 등) 오케스트레이션 설정