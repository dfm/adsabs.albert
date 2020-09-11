# adsabs.albert

An [Albert](https://albertlauncher.github.io/) extension to support NASA ADS searches

## Installation

First, clone this repository to the [Albert exentension module](https://albertlauncher.github.io/docs/extensions/python/) directory:

```bash
git clone https://github.com/dfm/adsabs.albert.git ~/.local/share/albert/org.albert.extension.python/modules/adsabs
```

Then enable this extension in the Albert settings by navigating to the `Extensions` tab and selecting `Python` and then `NASA ADS`.

## Usage

To get started you can just open Albert and type `ads ` to start searching. This workflow is
designed to search authors and years only. For example, if you want to search for papers by an
author named "Spergel" in 2015, you can execute:

```
ads spergel 2015
```

If you only want to search for the first author, use:

```
ads ^spergel 2015
```

You can list multiple authors, if you want:

```
ads ^mandel agol 2002
```

Or year ranges:

```
ads ^mandel agol 2000 2004
```

And you can include first names, initials, etc. using quotes:

```
ads "^mandel, k" "agol, e" 2000 2004
```

## Issues

If you run into any problems, please [report the issue on GitHub](https://github.com/dfm/adsabs.albert/issues).

## License

Copyright 2020 Dan Foreman-Mackey.

This is free software made available under the MIT License. For details see the LICENSE file.
