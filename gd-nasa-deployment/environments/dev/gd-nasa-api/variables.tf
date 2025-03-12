#-------------------------------------------------------------------------------
# VARIBALES
#-------------------------------------------------------------------------------
variable "project_id" {
  type        = string
  description = "GCP project name"
  default     = "gd-gcp-datamesh-qa"
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west1"
}

variable "image_name" {
  type        = string
  description = "Docker image to be deployed on cloud run"
}

variable "image_tag" {
  type        = string
  description = "Docker image tag to be deployed on cloud run"
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
