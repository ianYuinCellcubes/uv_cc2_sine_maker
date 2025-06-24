# This Project is ...

This project is a SW for outputting and controlling sine Gray Pattern.
The SW structure follows MVC and you can install and run it using UV.

## About UV

`uv`는 Python 생태계를 위한 **초고속 패키지 설치 + 가상환경 관리 + Python 버전 관리** 도구입니다.
Rust로 작성되어 있어 **pip + venv보다 수십 배 빠르고 편리**합니다.

### How to install UV

**윈도우 (PowerShell)**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux (bash)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치 확인:
```bash
uv --version
```

**공식 설치 문서**: [https://docs.astral.sh/uv/getting-started/installation/#standalone-installer](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

---

## Setup Sine Maker

```bash
# 1) 저장소 복제
git clone https://github.com/ianYuinCellcubes/uv_cc2_sine_maker.git

# 2) 프로젝트 폴더로 이동 및 초기화
cd uv_cc2_sine_maker

# 3) 프로젝트 실행
uv run main.py
```

---
