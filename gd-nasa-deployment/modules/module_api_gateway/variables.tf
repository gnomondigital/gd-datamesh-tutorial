#-------------------------------------------------------------------------------
# REGION
#-------------------------------------------------------------------------------

variable "region" {
  description = "name of specific region to deploy services into, e.g. eu-west1"
  default     = "europe-west1"
}

variable "project_id" {
  description = "name of GCP project to deploy services into"
  type        = string
  default     = "gd-gcp-datamesh-qa"
}

variable "api_prefix" {
  description = "api prefix"
  type        = string
  default     = "api"
}

variable "api_spec_path" {
  description = "Path to the OpenAPI spec yaml file"
  type        = string
}

variable "cloudrun_url" {
  description = "Cloud Run URL"
  type        = string
}

variable "spec_names" {
  description = "specs file name"
  type        = list(string)
  default     = ["api.yaml"]
}

variable "api_gateway_sa" {
  description = "Service account name for api gateway"
  type        = string
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
