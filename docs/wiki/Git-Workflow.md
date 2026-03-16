# 🌿 Git & GitHub 협업 룰

본 프로젝트는 **Organization Repo를 Fork하여 Personal Repo에서 개발 후 PR을 보내는 방식**으로 진행합니다.

## 1. Branch Strategy (브랜치 전략)
* **Organization Repo (공용)**
  * `main` : 배포 가능 상태 (Protected)
  * `develop` : 통합 개발 브랜치 (**PR 타깃 브랜치**)
* **Personal Fork Repo (개인)**
  * `main` : 기능 통합 브랜치 (**PR 출발 브랜치**)
  * `feature/*` : 기능 개발 (예: `feature/customer-clustering`)
  * `fix/*` : 버그 수정 (예: `fix/prediction-error`)

---

## 2. 🔄 Development Workflow (개발 순서)
작업은 반드시 아래 순서를 지켜서 진행합니다.

**① 작업 시작 전 (최신화)**
```bash
git checkout main
git fetch upstream
git merge upstream/develop
git push origin main