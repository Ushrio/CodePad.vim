from plugin.codepad import *

def codepadPaste():
  url = codepadGet(run=False)

  import vim
  vim.command("call setreg('+', '%s')" % url)
  vim.command("call setreg('*', '%s')" % url)

  import webbrowser
  webbrowser.open(url)
