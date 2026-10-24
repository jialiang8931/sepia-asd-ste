# Terraform 參考邊界

此資料夾目前只有文件，不包含資源、provider 設定、工具映像或 plan/apply 入口，也不是待實作的部署計畫。

實際專案確有基礎設施需求且經核准時，將 Terraform 宣告、環境設定與 provider 鎖檔放在 infra/terraform/。有真實重用需求才建立 modules，不預建空環境。

Terraform 一律透過 Docker 執行，不在本機安裝。Docker 工具設定放在 infra/docker/。本機允許 Docker、AWS CLI、Git，不擴及其他開發工具。

Plan 與 apply 使用各自用途明確的入口，不靠參數切換。執行 plan 不取得 apply 授權；資源異動前核對身份、環境、目標與變更範圍。

AWS 身份使用 `~/.aws`，容器只在必要操作中唯讀掛載。State、plan 與機敏產物不提交 Git，依核准方式保存或清理。本 repo 不因加入此說明就執行 Terraform、存取 AWS 或新增部署流程。
