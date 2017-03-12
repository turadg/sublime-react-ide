import os
import re
import shutil
import sublime

from collections import defaultdict
from sublime import Region
from sublime_plugin import TextCommand, WindowCommand
from threading import Timer
from distutils.dir_util import mkpath

class Config:
  def __init__(self, settings):
    self.src = settings.get('src')
    self.extensions = ["js", "jsx"]

settings = sublime.load_settings('ReactIDE.sublime-settings')
config = Config(settings)

def remove_src_root(filename):
  if filename.find(config.src) == 0:
    return filename[len(config.src):]

  return filename

def attempt_lazyspec(asset):
  cmd_exists = lambda x: shutil.which('lazyspec') is not None
  if cmd_exists:
    abs_path = os.path.join(config.src, asset['path'])
    os.system('lazyspec %s' % abs_path)


def asset_info(abs_path):
  rel_path = remove_src_root(abs_path)
  (asset_dir, asset_filename) = os.path.split(rel_path)

  (basename, ext) = os.path.splitext(asset_filename)

  name = re.sub('-test$', '', basename)

  require_path = os.path.join(asset_dir, basename)

  return {
    'path': rel_path,
    'dir': asset_dir,
    'filename': asset_filename,
    'name': name,
    'ext': ext,
    'require_path': require_path,
  }

class SwitchComponentStylesheet(TextCommand):
  """
  Cycle between:
  - React component (components/Foo.jsx)
  - Stylesheet for component (components/styles/Foo.scss)

  Makes any file that doesn't yet exist.
  """
  def run(self, edit):
    asset = asset_info(self.view.file_name())

    next_filepath = ""

    if asset['ext'] == '.jsx':
      # go to stylesheet
      styles_dir = os.path.join(config.src, asset['dir'], 'styles')
      mkpath(styles_dir) # ensure it exists

      next_filepath = os.path.join(styles_dir, asset['name'] + '.scss')

    elif asset['ext'] == '.scss':
      # go to component
      component_dir = os.path.join(config.src, asset['dir'], '..')
      mkpath(component_dir) # ensure it exists
      next_filepath = os.path.join(component_dir, asset['name'] + '.jsx')

    else:
      sublime.error_message("Unprocessable file type %s" % asset['ext'])

    self.view.window().run_command('open_file', {
      'file': next_filepath
    })


class SwitchComponentTest(TextCommand):
  """
  Cycle between:
  - React component (components/Foo.jsx)
  - Test of component (components/__tests__/Foo-test.js)

  Makes any file that doesn't yet exist.
  """
  def run(self, edit):
    next_filepath = ""

    asset = asset_info(self.view.file_name())

    if asset['ext'] == '.jsx':
      # go to test
      component_dir = os.path.dirname(asset['path'])
      tests_dir = os.path.join(config.src, component_dir, '__tests__')
      mkpath(tests_dir) # ensure it exists

      next_filepath = os.path.join(tests_dir, asset['name'] + '-test.js')
      if not os.path.exists(next_filepath):
        attempt_lazyspec(asset)

    elif asset['ext'] == '.js':
      # go to component
      component_dir = os.path.join(config.src, asset['dir'], '..')

      mkpath(component_dir) # ensure it exists
      next_filepath = os.path.join(component_dir, asset['name'] + '.jsx')
    else:
      sublime.error_message("Unprocessable file type %s" % asset['ext'])

    self.view.window().run_command('open_file', {
      'file': next_filepath
    })

class MakeImport(TextCommand):
  """
  Make an import statement for the current file, and copy to the clipboard
  """
  def run(self, edit):
    asset = asset_info(self.view.file_name())

    line = "import %s from '%s';\n" % (asset['name'], asset['require_path'])

    sublime.set_clipboard(line)
