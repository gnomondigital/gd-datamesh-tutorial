#-------------------------------------------------------------------------------
# TO DEPLOY ALGO ARIMA ALGO
# - CLOUD RUN
# - API GATEWAY WITH API KEY
# INPUT IS OPENAPI.YAML OF API
#-------------------------------------------------------------------------------
module "cloud_run" {
  source       = "../../../modules/cloud-run"
  region       = var.region
  image_name   = "${var.image_name}:${var.image_tag}"
  api_name     = "gd-nasa-api"
  memory_limit = "4Gi"
  cpu_limit    = "1.0"
  api_run_sa   = data.terraform_remote_state.foundation.outputs.api_run_sa

}

module "api_gateway" {
  source         = "../../../modules/api-gateway"
  region         = var.region
  project_id     = var.project_id
  api_prefix     = "gd-nasa-api"
  spec_names     = ["api_meteo.yaml"]
  api_spec_path  = "./spec_meteo.yaml"
  cloudrun_url   = module.cloud_run.cloudrun_url
  api_gateway_sa = data.terraform_remote_state.foundation.outputs.api_gateway_sa
  depends_on     = [module.cloud_run]
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
