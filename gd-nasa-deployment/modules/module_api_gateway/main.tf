#-------------------------------------------------------------------------------
# DEPLOY API GATEWAY
#------------------------------------------------------------------------------
locals {
  api_prefix               = var.api_prefix
  api_gateway_container_id = "${local.api_prefix}-gw-container"
  gateway_id               = "${local.api_prefix}-gw"
  gateway_config           = "${local.api_prefix}-gw-config"
  spec_names               = var.spec_names
  google_service_account   = var.api_gateway_sa
}


resource "google_api_gateway_api" "api_gw" {
  provider     = google-beta
  api_id       = local.api_prefix
  display_name = local.api_prefix
}

resource "google_api_gateway_api_config" "api_cfg" {
  count                = length(local.spec_names)
  provider             = google-beta
  api                  = google_api_gateway_api.api_gw.api_id
  api_config_id_prefix = local.api_prefix
  display_name         = local.gateway_config

  openapi_documents {
    document {
      path = "specs/${local.spec_names[count.index]}"
      contents = base64encode(templatefile("${path.module}/specs/${local.spec_names[count.index]}",
        {
          CLOUD_RUN_URL = var.cloudrun_url
      }))
    }
  }

  gateway_config {
    backend_config {
      google_service_account = local.google_service_account
    }
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "google_api_gateway_gateway" "gw" {
  provider = google-beta
  region   = var.region

  api_config = google_api_gateway_api_config.api_cfg[0].id

  gateway_id   = local.gateway_id
  display_name = local.gateway_id

  depends_on = [google_api_gateway_api_config.api_cfg]
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
