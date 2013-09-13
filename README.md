gedit-customhighlighter
=======================

In short, this custom hightlighter plugin for gedit, offers:
* highlight words which are in custom lists
* these lists are stored in ~/.config/gedit/custom-highlight
* this highlighting will be overruling standard syntax highlighting
* each list of words can have custom highlighting:
  * font color
  * background color
  * regular/bold/italic/bolditalic
* each list can be language specific (use spell check language)
* highlight length of word, sentence and paragraph

Rationale: this custom highlighting can be a writing aid to:

1. Warn for certain know writing errors (independent of spelling and
grammar checking) mainly in proper names not supported by these
checkers. Also to detect these mistakes in documents created by others.

2. Warn for words a user know he or she uses too often and want to keep
track of. For example, I tend to use the word 'also' a lot. Each time I
have to search my text for occurrences and rewrite it to use 'too' or
another contrustion. I would like to be notified for each time is use
that word. Similarly, I like to be notified for usage of words such as
therefore, nevertheless, despite, however, albeit, and alike. Preloaded
lists of this kind can be offered with the plugin.
