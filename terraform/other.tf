resource "aci_tenant" "Labor" {
  name = "Labor"
}
resource "aci_application_profile" "AP1" {
  tenant_dn = "${aci_tenant.Labor.id}"
  name = "AP1"
}
resource "aci_application_epg" "VLAN10-EPG" {
  application_profile_dn = "${aci_application_profile.AP1.id}"
  name = "VLAN10-EPG"
}