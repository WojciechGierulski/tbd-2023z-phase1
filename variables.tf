variable "project_name" {
  type        = string
  description = "Project name"
}

variable "region" {
  type        = string
  default     = "europe-west1"
  description = "GCP region"
}

variable "ai_notebook_instance_owner" {
  type        = string
  description = "Vertex AI workbench owner"
}

variable "dataproc_num_preemptible_nodes" {
  type = number
  description = "The number of preemptible/spot instances for the Dataproc cluster"
  default     = 0
}

variable "jupyterlab_machine_type" {
  description = "The machine type for the JupyterLab instance"
  default     = "e2-standard-2"
}

variable "dataproc_machine_type" {
  description = "The machine type for the Dataproc cluster"
  default     = "e2-standard-2"
}

variable "dataproc_num_worker_nodes" {
  description = "The number of worker nodes for the Dataproc cluster"
  default     = 2
}