# Usage

<!-- `heading-offset: 1` shifts the headings included from USAGE.md one level
deeper, so that they nest inside this page's "Usage" section. Without it, MyST's
include would make them siblings of "Usage" at the document root, and the Sphinx
man page builder would silently drop the top-level section headings (SYNOPSIS,
COMMANDS, …) and uppercase the flag headings (`-h, --host=HOST` would render as
`-H, --HOST=HOST`). -->

```{include} ../../USAGE.md
:heading-offset: 1
:relative-docs: true
:relative-images: true
```
