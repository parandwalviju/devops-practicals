from ansible.module_utils.basic import*

def return_powershell(username):
  try:
    import pwd
    return [entry.pw_shell for entry in pwd.getpwall() if entry.pw_name==username][0]
  except:
    module.fail_json(msg="power shell not found.")

def main():
  module = AnsibleModule(argument_spec = dict(username = dict(required=True)))
  username = module.params.get("username")

  power_shell = return_powershell(username)
 
  module.exit_json(changed=True, msg=power_shell)


main()

