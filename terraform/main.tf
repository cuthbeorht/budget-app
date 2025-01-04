resource "azurerm_resource_group" "budget" {
  name = var.resource_group_name
  location = var.dev_location
}

resource "azurerm_postgresql_server" "budget" {
  name = "budget-1"
  location = "canadaeast"
  resource_group_name = azurerm_resource_group.budget.name

  sku_name = var.postrgres_sku_name

  storage_mb = 5120
  backup_retention_days = 7
  geo_redundant_backup_enabled = false
  auto_grow_enabled = false

  administrator_login = "pgadmin"
  administrator_login_password = random_password.budget_database.result
  version = var.postgres_version
  ssl_enforcement_enabled = true
}

resource "azurerm_postgresql_database" "budget" {
  name                = "budgetdb"
  resource_group_name = azurerm_resource_group.budget.name
  server_name         = azurerm_postgresql_server.budget.name
  charset             = "UTF8"
  collation           = "English_United States.1252"

  # prevent the possibility of accidental data loss
  lifecycle {
    prevent_destroy = false
  }
}

resource "azurerm_postgresql_firewall_rule" "budget" {
  name = "home_dev_access"
  resource_group_name = azurerm_resource_group.budget.name
  server_name = azurerm_postgresql_server.budget.name
  start_ip_address = data.http.my_ip.response_body
  end_ip_address = data.http.my_ip.response_body
}