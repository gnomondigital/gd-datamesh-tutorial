#-------------------------------------------------------------------------------
# VARIBALES
#-------------------------------------------------------------------------------
variable "project_id" {
  type        = string
  description = "GCP project name"
  default     = "gnomondigital-ai-platform-dev"
}

variable "project_id_bq" {
  type        = string
  description = "GCP project name for big query"
  default     = "gnomondigital-ai-platform-dev"
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west1"
}

#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
