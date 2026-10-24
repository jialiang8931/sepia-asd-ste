# Production 參考說明

這是既有的部署邊界說明，不是部署功能、必備架構或待交付計畫。本 repo 沒有 production 入口，不會因為目錄存在就新增部署流程。

實際專案確有需要且經核准時，才決定 account、region、profile、role、資源、產物、驗證與回復方式。部署入口只做唯一目的，先驗證身份與目標，不以參數切換行為。

基礎設施使用 Terraform，並透過 Docker 執行。Plan 與 apply 分開，驗證不修改遠端資源。本文件不授權部署或 CI/CD。
