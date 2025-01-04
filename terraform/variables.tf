variable "subscription_id" {
  type = string
  description = "The tenant the resources will be created in"
}

variable "resource_group_name" {
  type = string
  description = "Identifier given to the resource group"
}

variable "dev_location" {
  type = string
  description = "Name of the geographic location of the dev environment in Azure"
}

# Postgres Server variables

variable "postrgres_sku_name" {
  type = string
  description = "Identifier to the type of VM's assigned to the database"
}

variable "postgres_version" {
  type = string
  description = "Iteration of the Postgresql server"

  validation {
    condition = contains(["10"], var.postgres_version)
    error_message = "Version not in allowed list"
  }
}
