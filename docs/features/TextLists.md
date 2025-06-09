# Text Lists

Text Lists provide a simple way to manage and store strings locally (like error messages or descriptions). Instead of hardcoding text, you can reference a string by its ID which keeps your code clean, maintainable, and sets you up for multi-language support.

---

## Purpose

Text Lists are useful for:

- Keeping user-visible strings out of logic code

- Making your project multi-language friendly

- Centralizing text descriptions (e.g., alarm messages, motor errors)

- Saving memory compared to long constant string arrays

## How-To

### Adding a text list to your project
To add a property to your function block:

--> Right-click the Application node

--> Select Add Object

--> Choose Text List

![Insert POU](/ooip-tutorial-library/private/images/TextLists/add-list.png){ width=500 }

### Adding Entries
Double-click the text list to open it. Then start adding rows. Each entry has:

ID - A string used in your code to look up the description

Default Text - The English (or fallback) version of the message

Language columns - Add additional languages like de, fr, etc.

You can see the additional column with the header 'de' providing German translations.

![Insert POU](/ooip-tutorial-library/private/images/TextLists/text-list.png){ width=400 }

### Accessing strings in code
To simplify text list access I created a GetText function. 

This wraps up the DynamicTextGetText function allowing you to pass a language and a default return value.

In my motor function block I can get and error descriptions from my text file in any of my configured languages.

![Insert POU](/ooip-tutorial-library/private/images/TextLists/motor-class.png){ width=400 }

Finally we can call the get method on the ErrorDescription property in MotorA.

![Insert POU](/ooip-tutorial-library/private/images/TextLists/main.png){ width=400 }

## Example

Clone and check out the project in the examples folder!