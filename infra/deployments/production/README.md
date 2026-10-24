# Production 部署狀態

未實作，也沒有對應公開腳本。

在 owner 核准 account、region、profile、role、資源、部署產物、驗證及回復方式前，不新增可執行部署流程。核准後使用單一用途且無參數的明確入口，設定讀取固定位置，先驗證身份與目標，再執行部署。

Terraform plan 與 apply 如有需求，使用分開入口。不得因執行 validation 而修改遠端資源。
