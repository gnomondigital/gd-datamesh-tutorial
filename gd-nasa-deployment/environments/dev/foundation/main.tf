
#-------------------------------------------------------------------------------
#                              --- Enable projects ---
#-------------------------------------------------------------------------------
resource "google_project_service" "api" {
  service            = "apigateway.googleapis.com"
  disable_on_destroy = false
}

resource "google_project_service" "this" {
  service            = "run.googleapis.com"
  disable_on_destroy = false
}

#-------------------------------------------------------------------------------
#                              --- Run Service  ---
#-------------------------------------------------------------------------------
resource "google_service_account" "api_run_sa" {
  account_id   = "api-run-sa"
  display_name = "API Cloud Run service Account"
  project      = var.project_id
}

resource "google_project_iam_member" "api_run_admin" {
  for_each = toset(["roles/run.admin", "roles/bigquery.admin"])
  role     = each.value
  member   = "serviceAccount:${google_service_account.api_run_sa.email}"
  project  = var.project_id
}

resource "google_project_iam_member" "api_run_bigquery_admin" {
  role    = "roles/bigquery.admin"
  member  = "serviceAccount:${google_service_account.api_run_sa.email}"
  project = var.project_id_bq
}

#-------------------------------------------------------------------------------
#                              --- API GATEWAY SERVICE ---
#-------------------------------------------------------------------------------

resource "google_service_account" "api_gateway_sa" {
  account_id   = "api-gateway-sa"
  display_name = "API Gateway Service Account"
  project      = var.project_id
}

resource "google_project_iam_member" "api_gateway_invoker" {
  role    = "roles/run.invoker"
  member  = "serviceAccount:${google_service_account.api_gateway_sa.email}"
  project = var.project_id
}

resource "google_project_iam_member" "api_gateway_admin" {
  role    = "roles/apigateway.admin"
  member  = "serviceAccount:${google_service_account.api_gateway_sa.email}"
  project = var.project_id
}
