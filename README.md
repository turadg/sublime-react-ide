# React IDE for Sublime

This plugin contains some commands to assist in developing React components.

- Switch between component and test
- Switch between component and stylesheet
- Make import for current file

If the test isn't defined yet, the command will attempt to run [LazySpec](https://github.com/turadg/lazyspec) to autogenerate one.


## Caveats

If you're using Atom, [Nuclide](https://nuclide.io/) is way better. I built this because I still prefer Sublime.

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

## Install

e.g. if you were to `git clone` this to `~/Code/sublime-react-ide`.

**Sublime Text 3**

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
$ ln -s ~/Code/sublime-react-ide .
```

**Sublime Text 2**

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
$ ln -s ~/Code/sublime-react-ide .
```

Sublime should pick up the changes automatically, without having to restart.
