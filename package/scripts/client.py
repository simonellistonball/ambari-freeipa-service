import sys, os, pwd, signal, time, socket
from resource_management import *
from subprocess import call

class Slave(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    import params

    cmd = 'ipa-client-install'
    cmd = cmd + ' --hostname=' + socket.getfqdn()
    cmd = cmd + ' --server=' + params.server_hostname
    cmd = cmd + ' --domain=' + params.server_domain
    cmd = cmd + ' --realm=' + params.server_realm
    cmd = cmd + ' --password=' + params.admin_password
    cmd = cmd + ' --principal=admin' +
    cmd = cmd + ' --admin-password=' + params.admin_password
    cmd = cmd + ' --realm=' + params.server_realm
    cmd = cmd + ' --mkhomedir'
    cmd = cmd + ' --unattended'

    Execute(cmd)
    #echo hortonworks | kinit admin
    Execute('echo ' + params.admin_password + ' | kinit admin')

  def configure(self, env):
    print 'Configure the IPA Client';


if __name__ == "__main__":
  Client().execute()
