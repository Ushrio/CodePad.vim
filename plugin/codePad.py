def codepadLang(vimLang):
  filetypeMap = {
    'c':'C',
    'cpp':'C++',
    'd':'D',
    'haskell':'Haskell',
    'lua':'Lua',
    'ocaml':'OCaml',
    'php':'PHP',
    'perl':'Perl',
    'python':'Python',
    'ruby':'Ruby',
    'scheme':'Scheme',
    'tcl':'Tcl'
  }
  return filetypeMap.get(vimLang, 'Plain Text')

def codepadGet(run):
  import urllib
  import vim

  url = 'http://codepad.org'
  data = {
    'code':'\n'.join(vim.current.buffer),
    'lang':codepadLang(vim.eval('&filetype')),
    'submit':'Submit'
  }
  if run:
    data['run'] = True

  response = urllib.urlopen(url, urllib.urlencode(data))
  return response.geturl()

def codepadPaste():
  url = codepadGet(run=False)
  import vim
  vim.command("call setreg('+', '%s')" % url)
  vim.command("call setreg('*', '%s')" % url)
  import webbrowser
  webbrowser.open(url)

def codepadRun():
  url = codepadGet(run=True)
  import vim
  vim.command("call setreg('+', '%s')" % url)
  vim.command("call setreg('*', '%s')" % url)
  import webbrowser
  webbrowser.open(url)

