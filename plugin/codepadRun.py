from plugin.codepad import *

def codepadRun():
  url = codepadGet(run=True)

  import vim

  vim.command("call setreg('*', '%s')" % url)

  import webbrowser
  webbrowser.open(url)
