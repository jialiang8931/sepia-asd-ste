# 架構參考與本 repo 的邊界

sepia-asd-ste 是輔助技能與規範參考庫。下列是已確認的實際專案配置參考，不是寫作技能的安裝要求，也不授權自動改造其他專案。

## 實際專案的配置參考

根目錄只保留 AGENTS.md、README.md、.gitignore。其他設定、依賴及鎖檔放在對應資料夾。目錄只在實際需要時建立：

```text
contracts/                 核准的 API、資料與架構契約
services/<service>/core/   純業務規則、不可變資料
services/<service>/shell/  邊界驗證、IO、外部整合
infra/docker/              容器與工具鏈設定
infra/terraform/           基礎設施宣告與版本鎖定
scripts/                   單一用途、無隱藏參數的入口
tests/                     核心、契約與整合測試
docs/                      需求、架構與操作說明
tools/                     必要時才加入的容器化工具
skills/                    明確選用的輔助技能
```

Terraform 的環境設定、provider 鎖檔及有真實重用需求的 modules 放在 infra/terraform/，不在根目錄建立設定，不為範例建立空環境。Terraform 只在 Docker 執行。

## 程式責任

資料方向是外部輸入、shell 驗證、core 純計算、shell 執行必要 IO，最後輸出。相依方向為 shell -> core。

既有 `services/sample/core/quantities.py` 對不可變 tuple 計算總數。負數是業務錯誤。外殼 `services/sample/shell/main.py` 處理 JSON、型別驗證、stdin、stdout、stderr 及 exit code。

輸入契約在 `contracts/sample-request.schema.json`，外殼的解析另拒絕布林及小數表示。這是示範，不是其他專案必用的業務邏輯。

目前檢查只覆蓋本 repo 的結構、腳本及 Python 範例，不能證明其他專案、其他語言或所有函數純度。是否導入參考架構，由目標專案明確決定。

## Git 方向

日常工作從 dev 開 `<type>/<具體目的>` 分支，完成後須經核准才整合回 dev。沒有 dev 時從 main 建立；遠端已有 dev 時沿用，不另建不同起點。

release 僅處理核准的正式上線發布。只有使用者明確允許，才可合併 main/master。提交或推送授權不等於合併或發布授權。

Commit 格式為 `<type>(<file>): <中文描述>`，依實際行為使用 feat、fix、docs、refactor、test、chore 等前綴。本輪更新只推送初始化的 dev 與用途分支，不合併、不移動版本標籤。
