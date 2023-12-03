variable "project_name" {
  type        = string
  description = "Project name"
}

variable "region" {
  type        = string
  default     = "europe-west1"
  description = "GCP region"
}

variable "subnet" {
  type        = string
  description = "VPC subnet used for deployment"
}

variable "machine_type" {
  type        = string
  default     = "e2-medium"
  description = "Machine type to use for both worker and master nodes"
}

variable "image_version" {
  type    = string
  default = "2.1.27-ubuntu20"
}

variable "preemptible_num_instances" {
  type = number
  default     = 0
  description = "The number of preemptible/spot instances"
}

variable "num_workers" {
  default     = 2
  description = "The number of worker nodes for the Dataproc cluster"
}
