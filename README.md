# sepia-asd-ste

Sepia／STE 寫作輔助技能與開發規範參考庫，供個人按需取用，不是主導專案開發的框架。

## 輔助用途

主要內容在 `skills/sepia-ste/`。一般寫作以 Sepia 摘要為主，技術與操作文件按需加入 STE 原則；嚴格 STE 只有明確要求時啟用。摘要不是完整標準或字典，不宣稱完整 ASD-STE100 合規。

FP、imperative shell、目錄、Docker、Terraform、AWS 與 scripts 文件供架構參考。使用寫作技能不代表整套導入；目標專案自己的需求、契約與 AGENTS.md 才是開發依據。本 repo 不自動覆寫它們，也不接管測試、部署或 Git。

## 內容配置

根目錄只有 AGENTS.md、README.md、.gitignore 三個檔案。其餘內容放在資料夾：

```text
AGENTS.md
README.md
.gitignore
contracts/
services/sample/
  core/
  shell/
infra/
  docker/
    Dockerfile
    Dockerfile.dockerignore
  terraform/
    README.md
  deployments/production/
    README.md
scripts/
  validate.sh
  test.sh
tests/
tools/
docs/
skills/sepia-ste/
```

`services/sample/` 是既有 Python 示範，不是應用程式必備骨架。`infra/terraform/` 目前只有存取及執行邊界說明，沒有資源、工具映像或 plan/apply 入口。部署文件不是後續開發計畫。

實際專案的架構配置與 Git 規範參考 `docs/architecture.md`；不為完整性建立空目錄或新增功能。

## 本機驗證

單純閱讀文件或使用寫作技能，不需要執行本 repo 的驗證。維護本 repo 時，可明確執行：

```sh
./scripts/validate.sh
```

既有入口先在 Docker 使用鎖定的 Gitleaks 映像掃描，再檢查本 repo 的結構、腳本與 Python 範例，最後執行測試。它不是其他專案的開發閘門。只執行既有測試：

```sh
./scripts/test.sh
```

兩個入口都不接受參數，第一次執行需要 Docker 映像下載權限。本機允許安裝 Docker、AWS CLI、Git；其他開發工具走容器，不要求主機安裝 Python、Terraform 或 Gitleaks。這兩個入口不需要 AWS 身份，不讀取或掛載 `~/.aws`。

GitHub Actions 維持停用，沒有 workflow。不自動串接驗證、commit、push、tag 或部署，未經明確核准不新增 CI/CD。

## 開發與重用

日常工作從 dev 開符合用途的分支。沒有 dev 時，從 main 建立 dev；遠端已有 dev 時沿用遠端分支。release 只用於核准的正式上線發布，合併 main/master 需要明確允許。

Commit 使用 `<type>(<file>): <中文描述>`，例如 `docs(AGENTS.md): 補充分支與提交規範`。詳見 `AGENTS.md`。

優先取用需要的技能與文件，不必複製整個 repo 或重排既有專案。GitHub 的 Use this template 是可選方式，不代表整套規範自動適用。詳見 `docs/reuse.md`。

`0.0.0`、`latest` 保留歷史版本，仍包含最初的 workflow。此輪架構與定位更新位於 `docs/clarify-auxiliary-structure`，尚未合併 dev、main 或 master；dev 只完成從 main 初始化。標籤不移動、不重建，也不代表部署完成。
