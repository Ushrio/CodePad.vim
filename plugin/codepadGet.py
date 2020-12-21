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
  import urllib.request
  import urllib.parse
  import vim

  url = 'http://codepad.org'
  data = {
    'code':'\n'.join(vim.current.buffer),
    'lang':codepadLang(vim.eval('&filetype')),
    'submit':'Submit'
  }
  # if run is true than add the run key to the data dict with the value True
  if run:
    data['run'] = True

  response = urllib.request.urlopen(url, urllib.parse.urlencode(data))
  return response.geturl()
