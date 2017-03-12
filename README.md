# React IDE for Sublime

This plugin contains some commands to assist in developing React components.

- Switch between component and test
- Switch between component and stylesheet
- Make import for current file

If the test isn't defined yet, the command will attempt to run [LazySpec](https://github.com/turadg/lazyspec) to autogenerate one.


## Related

If you're using Atom, [Nuclide](https://nuclide.io/) is way better. I built this because I still prefer Sublime.

If you want snippets, try [React Development Snippets](https://github.com/jeantimex/react-sublime-snippet).

## Caveats

It makes some huge assumptions about how your files are organized. PRs welcomed to relax these.

It doesn't yet support more than one project.


## Required configuration

Open `Preferences > Package Settings > React IDE > Settings - User` and make it look like this:

```
{
  "src": "/Users/<username>/path/to/your/project/"
}
```

(Note the trailing slash.)

## Installation ##

### Using Package Control ###

WIP: https://github.com/wbond/package_control_channel/pull/6185

### Without Package Control ###

Navigate to your Sublime Text packages folder and git clone this project.

#### MacOS ####
"/Users/{user}/Library/Application Support/Sublime Text {2|3}/Packages"

#### Windows ####
"C:\Users\{user}\AppData\Roaming\Sublime Text {2|3}\Packages"

```
git clone https://github.com/turadg/sublime-react-ide.git
```

Sublime should pick up the changes automatically, without having to restart.
