# extracting-windows-registry-keys-using-regex

takes a text blob and returns a list of valid windows registry keys in that text i.e., looking at their case, spacing etc



### Regular Expression in python:

text = "Hello, I have 10 apples and 5 oranges."


### Matching Patterns:

The re.match() function is used to match a pattern at the beginning of a string.

The re.search() function is used to search for a pattern anywhere in the string.

The re.findall() function returns all non-overlapping matches of a pattern in a string.


### Common patterns used:

Commonly used characters:
.: Matches any character except a newline.

^: Matches the start of a string.

$: Matches the end of a string.

[]: Matches any character within the brackets.

|: Matches either the pattern before or after the pipe.

*: Matches zero or more occurrences of the preceding pattern.

+: Matches one or more occurrences of the preceding pattern.

?: Matches zero or one occurrence of the preceding pattern.

\: Escapes special characters or indicates special sequences.

### Example pattern usage:

pattern = r"hello": Matches the exact string "hello".

pattern = r"[aeiou]": Matches any vowel character.

pattern = r"^\d+": Matches one or more digits at the beginning of a string.
