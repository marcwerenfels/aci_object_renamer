resource "aci_epg_to_static_path" "leaf_111_eth1_20" {
  application_epg_dn  = "${aci_application_epg.VLAN10-EPG.id}"
  tdn  = "topology/pod-1/paths-111/pathep-[eth1/20]"
  encap  = "vlan-10"
  instr_imedcy = "immediate"
  mode  = "regular"
}

resource "aci_epg_to_static_path" "leaf_111_eth1_21" {
  application_epg_dn  = "${aci_application_epg.VLAN10-EPG.id}"
  tdn  = "topology/pod-1/paths-111/pathep-[eth1/21]"
  encap  = "vlan-10"
  instr_imedcy = "immediate"
  mode  = "regular"
}

resource "aci_epg_to_static_path" "leaf_111_eth1_22" {
  application_epg_dn  = "${aci_application_epg.VLAN10-EPG.id}"
  tdn  = "topology/pod-1/paths-111/pathep-[eth1/22]"
  encap  = "vlan-10"
  instr_imedcy = "immediate"
  mode  = "regular"
}