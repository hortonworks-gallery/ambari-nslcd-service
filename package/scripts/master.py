import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call

class Master(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    import params

    Execute('cd /tmp; wget ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/okelet/RedHat_RHEL-6/x86_64/nss-pam-ldapd-0.8.12-rhel6.13.1.x86_64.rpm')
    Execute('cd /tmp; rpm -iv nss-pam-ldapd*.rpm')

    Execute('sed -i "s/passwd:.*files/passwd: files  ldap/g" /etc/nsswitch.conf')
    Execute('sed -i "s/group:.*files/group: files  ldap/g" /etc/nsswitch.conf')

    Execute('sed -i "s/gid nslcd/gid root/g" /etc/nslcd.conf')
    Execute('sed -i "s/base dc=example,dc=com/base '+params.dist_name+'/g" /etc/nslcd.conf') 
    Execute('sed -i "s#uri ldap://127.0.0.1/#uri ldap://'+params.ldap_url+'/#g" /etc/nslcd.conf')


    Execute('sed -i "s/#base.*group.*ou=Groups,dc=example,dc=com/base   group '+params.groups_name+'/g" /etc/nslcd.conf')
    Execute('sed -i "s/#base   passwd ou=People,dc=example,dc=com/base   passwd '+params.users_name+'/g" /etc/nslcd.conf')
    Execute('sed -i "s/#filter passwd (objectClass=aixAccount)/filter passwd (objectClass=posixaccount)/g" /etc/nslcd.conf')

    Execute('sed -i "s/#map.*passwd uidNumber.*uid/map    passwd uidNumber         uidNumber/g" /etc/nslcd.conf')
    Execute('sed -i "s/#map.*passwd gidNumber.*gid/map    passwd gidNumber         gidNumber/g" /etc/nslcd.conf')
    Execute('sed -i "s/#filter group  (objectClass=aixAccessGroup)/filter group  (objectClass=posixgroup)/g" /etc/nslcd.conf')

    Execute('service nslcd start')
    Execute('chkconfig nslcd on')


  def configure(self, env):
    import params
    env.set_params(params)

  def stop(self, env):
    import params
    Execute('service nslcd stop')
      
  def start(self, env):
    import params
    Execute('service nslcd start')
	

  def status(self, env):
    import params
    Execute('service nslcd status')

if __name__ == "__main__":
  Master().execute()
