import json
import re

# load ap, epg, bd content
with open('list/list_epg.json') as f:
    ap_epg_bd_var = json.load(f)

# load static path content
with open('list/list_static_paths.json') as f:
    static_paths_var = json.load(f)

# find matching static paths according to epg relation
print('')
print('#Static Paths')
for static_path in static_paths_var['static_paths'][0]['List1']:
    static_path_epg = re.sub(r'.*/epg-(.*?)/.*', r"\1", static_path['Associated_EPG_Path'])
    static_path_interface = re.sub(r'.*/rspathAtt-\[(.*?\])\]', r"\1", static_path['Associated_EPG_Path'])
    for epg_lists in ap_epg_bd_var['list_epg_in_ap']:
        for epg_list in epg_lists['EPG_LIST']:
            if static_path_epg == epg_list['EPG_NAME']:
                print(static_path_epg + " --> " + static_path_interface)

# load consumer contract content
with open('list/list_contracts_consumer.json') as f:
    contract_consumer_var = json.load(f)

# find matching consumer contracts according to epg relation
print('')
print('#Consumer Contracts')
for consumer_contract in contract_consumer_var['consumer_contracts'][0]['List1']:
    cons_contr_epg = re.sub(r'.*/epg-(.*?)/.*', r"\1", consumer_contract['Associated_EPG_Consumed_Contract'])
    for epg_lists in ap_epg_bd_var['list_epg_in_ap']:
        for epg_list in epg_lists['EPG_LIST']:
            if cons_contr_epg == epg_list['EPG_NAME']:
                print(cons_contr_epg + " --> " + consumer_contract['Topology_Object'])

# load provider contract content
with open('list/list_contracts_provider.json') as f:
    contract_provider_var = json.load(f)

# find matching provider contracts according to epg relation
print('')
print('#Provider Contracts')
for provider_contract in contract_provider_var['provider_contracts'][0]['List1']:
    prov_contr_epg = re.sub(r'.*/epg-(.*?)/.*', r"\1", provider_contract['Associated_EPG_Provided_Contract'])
    for epg_lists in ap_epg_bd_var['list_epg_in_ap']:
        for epg_list in epg_lists['EPG_LIST']:
            if prov_contr_epg == epg_list['EPG_NAME']:
                print(prov_contr_epg + " --> " + provider_contract['Topology_Object'])

# load domains content
with open('list/list_domains.json') as f:
    domains_var = json.load(f)

# find matching domains according to epg relation
print('')
print('#Domains')
for domain in domains_var['domains'][0]['List1']:
    domain_epg = re.sub(r'.*/epg-(.*?)/.*', r"\1", domain['Associated_EPG_Domain'])
    for epg_lists in ap_epg_bd_var['list_epg_in_ap']:
        for epg_list in epg_lists['EPG_LIST']:
            if domain_epg == epg_list['EPG_NAME']:
                print(domain_epg + " --> " + domain['Topology_Object'])

# list matching bd according to epg relation
print('')
print('#Bridge Domains')
for ap_epg_bd_outer in ap_epg_bd_var['list_epg_in_ap']:
    for ap_epg_bd_inner in ap_epg_bd_outer['EPG_LIST']:
        print(ap_epg_bd_inner['EPG_NAME'] + " --> " + ap_epg_bd_inner['BD_NAME'])

# load domains content
with open('list/list_subnets.json') as f:
    subnets_var = json.load(f)

# find matching BD subnets according to epg relation
print('')
print('#Subnets')
for ap_epg_bd_outer in ap_epg_bd_var['list_epg_in_ap']:
    for ap_epg_bd_inner in ap_epg_bd_outer['EPG_LIST']:
        for subnet in subnets_var['subnets']:
            subnet_bd = re.sub(r'.*/BD-(.*?)/.*', r"\1", subnet['Subnet_DN'])
            if subnet_bd == ap_epg_bd_inner['BD_NAME']:
                print(ap_epg_bd_inner['EPG_NAME'] + " --> " + ap_epg_bd_inner['BD_NAME'] + " --> " + subnet['IP_subnet'])
