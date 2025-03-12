#-------------------------------------------------------------------------------
# OUTPUTS
#-------------------------------------------------------------------------------
output "cloud_run_service_name" {
  value = google_cloud_run_v2_service.this.name
}

output "api_name" {
  value = google_cloud_run_v2_service.this.template
}

output "cloudrun_url" {
  value = google_cloud_run_v2_service.this.uri
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------