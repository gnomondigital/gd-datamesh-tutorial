#-------------------------------------------------------------------------------
# TO DEPLOY CLOUD RUN
#-------------------------------------------------------------------------------

locals {
  google_service_account = var.api_run_sa
}

resource "google_cloud_run_v2_service" "this" {

  name     = var.api_name
  location = var.region

  template {
    containers {
      image = var.image_name
      args  = var.image_args

      env {
        name  = "DB_NAME"
        value = "xxxx"
      }

      env {
        name  = "DB_PORT"
        value = "5432"
      }

      env {
        name  = "DB_USER"
        value = "xxxx"
      }

      env {
        name  = "DB_TABLE"
        value = "meteo_with_referential"
      }

      env {
        name  = "DB_HOST"
        value = "xxx"
      }
      env {
        name  = "DB_PASS"
        value = "xxxx"
      }
      resources {
        limits = {
          # Memory usage limit (per container)
          memory = var.memory_limit
          # CPI usage limit (per container)
          cpu = var.cpu_limit
        }
      }

      liveness_probe {
        http_get {
          path = "/"
        }
      }
    }
    service_account = local.google_service_account
    vpc_access {
      connector = "projects/${var.project_id}/locations/${var.region}/connectors/my-connector"
      egress    = "PRIVATE_RANGES_ONLY"
    }
  }
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
