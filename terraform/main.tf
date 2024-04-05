terraform {
  required_providers {
    aci = {
      source = "CiscoDevNet/aci"
      version = "0.7.0"
    }
  }
}

provider "aci" {
  # cisco-aci user name
  username = "username"
  # cisco-aci password
  password = "password"
  # cisco-aci url
  url      = "https://10.252.134.140/"
  insecure = true
}