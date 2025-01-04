output "database_password" {
  value = random_password.budget_database.result
  sensitive = true
}