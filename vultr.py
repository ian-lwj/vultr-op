import argparse
import json
from os.path import expanduser
import requests
import socket
import sys


APIKey = 


class Vultr:
    headers = {'API-Key': APIKey}

    def list_vms(self):
        r = requests.get('https://api.vultr.com/v1/server/list',
            headers=Vultr.headers, timeout=9)
        print r.status_code, r.content

    def destroy_vm(self, subid):
        payload = {'SUBID': subid}
        r = requests.post('https://api.vultr.com/v1/server/destroy',
            headers=Vultr.headers, data=payload)
        print r.status_code, r.content

    def create_vm(self):
        payload = {'DCID': '5', 'VPSPLANID': '200', 'OSID': 302}
        r = requests.post('https://api.vultr.com/v1/server/create',
            headers=Vultr.headers, data=payload, timeout=9)
        print r.status_code, r.content

    def add_ssh_key(self):
        home = expanduser("~")
        with open(home + "/.ssh/id_rsa.pub", "r") as f:
            key = f.read()
            payload = {'name': socket.gethostname(), 'ssh_key': key}
            r = requests.post('https://api.vultr.com/v1/sshkey/create',
                    header=Vultr.headers, data=payload)
            print r.status_code, r.content

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=sys.argv[0], description='tool of vultr api.')
    subparsers = parser.add_subparsers(help='sub-command help', dest="obj")
    parser_vm = subparsers.add_parser('vm', help='vm opertation.')
    parser_vm.add_argument('operation', choices=['list', 'create', 'destroy'])
    parser_vm.add_argument('subid', nargs='?', help="SUBID for destroy.")

    parser_sshkey = subparsers.add_parser('sshkey', help='sshkey operation.')
    parser_sshkey.add_argument('operation', choices=['list', 'add', 'delete'])
    parser_sshkey.add_argument('sshkeyid', nargs='?', help='SSHKEYID for delete.')

    args = parser.parse_args()

    vul = Vultr()
    if args.obj == 'vm':
        if args.operation == 'list':
            vul.list_vms()
        elif args.operation == 'create':
            vul.create_vm()
        elif args.operation == 'destroy':
            subid = args.subid
            vul.destroy_vm(subid)
    elif args.obj == 'sshkey':
        if args.operation == 'list':
            pass
        elif args.operation == 'add':
            vul.add_sshkey()
        elif args.operation == 'delete':
            pass

