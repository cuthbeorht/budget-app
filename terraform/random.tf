resource "random_password" "budget_database" {
  length = 25
  special = true
  override_special = "!@#$%*-_"
}