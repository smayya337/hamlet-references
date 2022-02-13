# Hamlet Reference Recognizer

"Is that a *Hamlet* reference?"

---

This little program takes a string input and finds the closest match to it in the text of Shakespeare's *Hamlet* using
a [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index).

To use it, run `references.py <YOUR TEXT HERE>` (e.g. `references.py "The puppy plays too much"`).

It's still a work in progress - it can pick up some easy sentences but not substrings (including the famous "To be or
not to be").
