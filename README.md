# Headdown: Downgrade Headings

Automatically demote those pesky headings!

## What?

This is a plugin for [Python-Markdown][pmd] to automatically downgrade headings by a given number of levels. This is useful when, for example, using a static site generator, such as [Pelican][pelican].

## Why?

I didn't want to have to write standalone markdown files whose structure was dictated by the constraints of my website; nor did I want to sacrifice the structure of my website because of my markdown files. A number of [3rd party Python-Markdown extensions][3ppmdx] already exist to do this ([here][p1] and [here][p2]), but I was unable to get them to work with Python-Markdown 3.

## How?

Download this repository and place the folder containing `__init__.py` somewhere on your path, or install via pip.

```
pip install markdown-headdown
```

Now, just add `mdx_headdown` to your `markdown` `extensions` and feel the magic.

You can optionally provide an `offset` parameter, which tells `headdown` by how many levels to downgrade all headings. The default is `1`.

Note
: This value will be converted to an integer and absolutised. Failure to provide a numeric option may lead to unexpected results.

For example, if using with [Pelican][pelican], your [configuration][pelicanconf] might look something like this:

```python
...
MARKDOWN = {
    'extensions': ['mdx_headdown',],
    'extension_configs': {
        'mdx_headdown': {
            'offset': 2,
        },
    },
}
...
```

## Credit

Thanks are owed to the author of [mdx_downheader][p2], whose code I examined for inspiration; and the contributers to the [default python-markdown extensions][pmdx], whose code I examined to get a better idea of what the [manual][pmdapi] was talking about.

This project is copyright 2018 by Sascha Cowley under the [MIT License](LICENSE).


[pmd]: https://python-markdown.github.io/
[pelican]: https://getpelican.com/
[p1]: https://code.google.com/archive/p/markdown-downheader/
[p2]: https://github.com/cprieto/mdx_downheader
[pmdx]: https://python-markdown.github.io/extensions/
[pmdapi]: https://python-markdown.github.io/extensions/
[pelicanconf]: http://docs.getpelican.com/en/stable/settings.html
[3ppmdx]: https://github.com/Python-Markdown/markdown/wiki/third-party-extensions