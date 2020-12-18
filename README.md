# I take no credit for the creation of this plugin.
## The initial creators of this plugin are: Nicolas Weber and Johannes Hoff.
 
I am only forking the plugin to update it and create a repo on GitHub.
**The original plugin can be found [here](https://www.vim.org/scripts/script.php?script_id=2298).**

# CodePad.vim
This plugin is a simple plugin that adds [CodePad](http://codepad.org) support to Vim.


# Use (Copied from the original plugin)
The plugin adds two new commands:

**:CPPaste**  
    to send the current buffer to http://codepad.org, open your pasted code
    in your webbrowser, and copy the URL of the pasted snippet to the
    clipboard.


**:CPRun**  
    to send the current buffer to http://codepad.org, execute it on their server,
    and open both the pasted source and the program output in your browser.
    The URL of the pasted snippets is copied to the clipboard as well.


The correct filetype is automatically detected through the 'filetype' option.

# Goals
- [ ] Add support for Python 3 and keep backwards compatibility with Python 2
- [ ] Add comments to the code to allow for easier future development
- [ ] Clean up file and folder structure to be more in line with typical Vim plugin design
- [ ] Host the plugin on GitHub allowing for easier future development

# License
This program is licensed under the standard MIT license.
