# 按需重用輔助內容

優先取用 `skills/sepia-ste/` 或需要的參考文件，不必複製整個 repo、重排專案或安裝驗證工具。目標專案自己的需求、契約與 AGENTS.md 才是開發依據。

FP、目錄、Docker、Terraform、AWS 及 scripts 規範供明確採用時參考。使用寫作技能不自動啟用整套架構或開發流程。GitHub 的 Use this template 只是取得完整內容的可選方式，不是預設步驟。

本 repo 的驗證只檢查自身結構與既有 Python 示範，不是所有專案的開發閘門，也不證明其他語言符合架構。不要為使用輔助工具而新增測試階段或部署流程。

本機允許安裝 Docker、AWS CLI、Git。其他開發工具與 Terraform 透過容器執行。全域技能安裝或 AGENTS 修改是另一項明確操作，不自動覆寫已安裝內容或 `~/.codex/AGENTS.md`。

GitHub Actions 維持停用，不提供 CI/CD。由此建立的新 repo 不保證繼承 GitHub 設定；不得因複製文件就假設 Actions 已停用，也不擅自新增自動化。

維護本 repo 時從 dev 開用途分支，沒有 dev 時從 main 建立。Commit 使用 `<type>(<file>): <中文描述>`。合併 main/master、上線 release 與移動標籤都須各自取得授權。

`0.0.0`、`latest` 保留初始 commit，仍含歷史 workflow。本輪定位與結構更新位於 `docs/clarify-auxiliary-structure`，尚未合併 dev、main 或 master；dev 只是從 main 初始化。不移動或重建標籤，也不把標籤當作部署成功。

ASD-STE100 完整標準及字典未包含或重新授權。Sepia 摘要來源及版本記錄於技能來源檔。技能摘要只在明確要求更新時刷新，不在一般使用時自動抓取來源。
