output "api_gateway_sa" {
  value       = google_service_account.api_gateway_sa.email
  description = "The email of the API Gateway Service Account"
}

output "api_run_sa" {
  value       = google_service_account.api_run_sa.email
  description = "The email of the cloud run Service Account"
}
