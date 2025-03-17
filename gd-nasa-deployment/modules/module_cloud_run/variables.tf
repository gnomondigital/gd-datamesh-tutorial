#-------------------------------------------------------------------------------
# VARIBALES
#-------------------------------------------------------------------------------
variable "region" {
  description = "Name of specific region to deploy services into, e.g. eu-west1"
  type        = string
  default     = "europe-west1"
}

variable "api_name" {
  description = "API name"
  type        = string
  default     = "api"
}

variable "image_name" {
  description = "Docker image name"
  type        = string
}

variable "image_args" {
  description = "Docker image runtime args"
  type        = list(string)
  default     = []
}

variable "memory_limit" {
  description = "Cloud RUN runtime memery limit"
  type        = string
  default     = "512Mi"
}

variable "cpu_limit" {
  description = "Cloud RUN runtime memery limit"
  type        = string
  default     = "1"
}

variable "api_run_sa" {
  description = "Service account name for cloud run"
  type        = string
}
variable "project_id" {
  description = "Name of GCP project to deploy services into"
  type        = string
  default     = "gnomondigital-ai-platform-dev"

}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
