#!/bin/python

import boto3
import json
def get_hosts(ec2,fv):
  f={'Name':'tag:Ansible','Values':[fv]}
  hosts=[] 
  for i in ec2.instances.filter(Filters=[f]):
     # print i.private_ip_address
      hosts.append(i.private_ip_address)  
  return hosts
def main():
   ec2=boto3.resource("ec2")
   db_group=get_hosts(ec2,"db")
   app_group=get_hosts(ec2,"App")
   
   all_groups= {
                'db': {
                   'hosts':db_group,
                   'vars': {
                          'group_name': 'Database group'
                           }
                       },
                 'app': {
                   'hosts':app_group,
                   'vars': {
                          'group_name': 'app group'
                           }
                       }
                }
   print json.dumps(all_groups)
if __name__=="__main__":
 main()

