import sublime
import sublime_plugin
import re
import os


filter_ext=['.html']

class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    #self.view.insert(edit, 0, "Hello, World!")
    #self.view.run_command("insert", {"characters": "Unicode Character"})
    count = 0
    print("Open files is '%s'" % (len(sublime.active_window().views())))
    for view in sublime.active_window().views():
      file_name = view.file_name()
      if file_name is None: continue
      print("Opening file '%s'" % (file_name))
      file_path, file_extension = os.path.splitext(file_name)
      print(file_extension)
      for fext in filter_ext:
        if file_extension == fext: break
      else: continue
      #replace in <table> all ' ' and '\n'
      region = view.find('<table(.|\n)*</table>',0);
      if region is None or region.empty(): continue
      txt = view.substr(region)
      txt = re.sub('\s*\n\s*\n+', '\n', txt)
      view.replace(edit, region, txt)
      view.sel().clear()
      view.sel().add(region)
      count=count+1;

    print("Modified %s files." %str(count))
    return

