This doc is summarized from Martin Flower's book [Refactoring (the 2nd Edition)](https://martinfowler.com/books/refactoring.html).
## Refactoring is all about Change
* You may inverse previous refactorings as software grows
* You may change names of a function/parameter/varible/... as you learn
## How to use this doc
Go to a section of code smell, and the refactoring techniques to that smell are written in `Pascal Case` under the **Solution** section. Refer to the book's catalog to get detailed examples and explainations for each refactoring technique.

## Table of Code Smells

* [Mysterious Name](#mysterious-name)
* [Duplicated Code](#duplicated-code)
* [Long Function](#long-function)
* [Long Parameter List](#long-parameter-list)
* [Global Data](#global-data)
* [Mutable Data](#mutable-data)
* [Divergent Change](#divergent-change)
* [Shotgun Surgery](#shotgun-surgery)
* [Feature Envy](#feature-envy)
* [Data Clumps](#data-clumps)
* [Primitive Obsession](#primitive-obsession)
* [Repeated Switches](#repeated-switches)
* [Loops](#loops)
* [Lazy Element](#lazy-element)
* [Speculative Generality](#speculative-generality)
* [Temporary Field](#temporary-field)
* [Message Chains](#message-chains)
* [Middle Man](#middle-man)
* [Insider Trading](#insider-trading)
* [Large Class](#large-class)
* [Alternative Classes with Different Interfaces](#alternative-classes-with-different-interfaces)
* [Data Class](#data-class)
* [Refused Bequest](#refused-bequest)
* [Comments](#comments)

## Mysterious Name

**Motivation**

- A good name can save hours of puzzled incomprehension in the future
- When you can't think of a good name for something, it's often a sign of a deeper design malaise

**Solution**

- `Change Function Declaration`
- `Rename Variable`
- `Rename Field`

## Duplicated Code

**Issue**

- Duplication wastes time on comparing and modifying the duplicates

**Solution**

- Same expressions: `Extract Function`
- Similar but not identical expressions: `Slide Statements`, then `Extract Function`
- Duplicate fragments in subclasses of a common base class: `Pull Up Method`

## Long Function

> In our experience, the programs that live best and longest are those with short functions.
>
> -- Martin Fowler and Kent Beck

**Motivation**

- Small function supports explanation, sharing, and choosing **Prerequisite: good naming,** So that you don't need to look at the function body to understand.

**When to decompose functions**

Heuristics, not rules.

- Whenever we feel the need to comment something

**Solution**

- For a single logic group: `Extract Function`
  - IF Non-pure: `Replace Temp with Query`
  - IF Long lists of parameters: `Introduce Parameter Object`; `Preserve Whole Object`
  - IF still not resolved: `Replace Function with Command`
- For conditional:
  - For conditional expressions: Decomposed Conditional
  - For big a switch statement: `Extract Function` on its legs
  - More than one switch statements switching on the same condition: `Replace Conditional with Polymorphism`
- For loops:
  - IF your loop is doing multiple things (can't be well named): `Split Loop`
  - ELSE: Extract the loop and its body into its own method.

## Long Parameter List

**Issue**

Long parameter list is better than using global data, but still can be confusing.

**Solution**

- IF a parameter can be derived by the other: `Replace Parameter with Query`
- IF parameters were pulled out from an object: `Preserve Whole Object`
- IF several parameters always fit together: `Introduce Parameter Object`
- IF a parameter is a flag to dispatch different behavior: `Remove Flag Argument`
- IF multiple functions share several parameter values: `Combine Functions into Class`

## Global Data

**Issue**

The problem with global data is that it can be modified from anywhere in the code base, and there’s no mechanism to discover which bit of code touched it.

**Forms of Global Data**

- Global variables
- Class variables
- Singletons

**Solution**

- `Encapsulate Variable`

## Mutable Data

**Issue**

- You can do harmful things by changing mutable data without realizing it.
- A rich source of confusion and bugs.

**Solution**

- `Encapsulate Variable`
- IF **a variable is being updated to store different things**: `Split Variable`
- IF there are **side-effect-free code together with dirty code**, THEN try to separate side-effect-free code: `Slide Statements` + `Extract Function`
- IF **a function with side-effect has a return value**: Separate Query from Modifier (Any function that returns a value should not have observable side effects)
- Always if possible: `Remove Setting Method`
- IF a **function modifies non-local data**: `Replace Derived Variable with Query`
- IF much code is needed to update a variable: `Combine Functions into Class`; `Combine Functions into Transform`
- IF **an object contains data object in its property**, replace instead of modifying it in place: `Change Reference to Value`

## Divergent Change

**Symptom**

- You often change a single module in different ways for different reasons

**Issue**

- You have to always understand/remember more than you need to make a simple change

**Cause**

- The module has too many different responsibilities!
- Context boundaries are unclear in the early days of a program; Continue to shift as a software system's capabilities change.

**Solution**

- IF **changes have different contexts**: split the module into separate ones
- IF **two aspects naturally form a sequence**: `Split Phase` and have a clear data structure between phases
- IF there is **more back-and-forth in the calls**: create appropriate modules, then split them by `Move Function`
- IF **one function has two types of processing**: split them via `Extract Function`
- IF the module is a **class**: split it via `Extract Class`

## Shotgun Surgery

The opposite of Divergent Change.

**Symptom**

- Every time you make a change, you have to make a lot of little edits to a lot of different classes

**Issue**

- You might forget to change somewhere

**Solution**

- `Move Function` and `Move Field`, to put all the changes into a single module
- IF **a set of functions operate on similar data**: `Combine Functions into Class`
- IF a **set of functions transform or enrich a data structure**: `Combine Functions into Transform`
- IF the common functions can combine their logic for a consuming phase of logic: `Split Phase` ❓
- `Inline Function` or `Inline Class `, if possible, to avoid jumping around. (May even find more suitable split after putting them together)

## Feature Envy

Put things together that change together. (data and the behavior that references that data)

**Symptom**

- A function in one module spends more time communicating with functions or data inside another module than it does within its own module.

**Motivation**

When modularize a program, we want to:

- Maximize the interaction inside a zone
- Minimize the interaction between zones

**Solution**

- a function invoking half-a-dozen getter methods on another object to calculate some value: move the function to the data using `Move Function`
- IF only a part of a function suffers from envy: `Extract Function`, then `Move Function`
- IF a function envies several modules: break the function into several pieces by `Extract Function`, then `Move Function`. Or directly move to the module which the function envies the most.
- Strategy and Visitor design pattern.

## Data Clumps

**Symptom**

- You see three or four data items together in lots of places: as fields in multiple classes, or as parameters in multiple functions.

**Solution**

- For repetitive class fields: use `Extract Class` to turn them into an object.
- For repetitive function parameters: use `Introduce Parameter Object` or `Preserve Whole Object` to slim them down.

**Note**

- Don't worry about data clumps that use only some of the fields of the new object. You'll benefit from it as long as you're replacing two or more fields with the new object.
- Test if your extraction makes sense: deleting one of the object properties makes the others become non-sense.

**Benefit**

- Improves readability: you can shrink a lot of parameter lists and simplify method calling
- Helps solving Feature Envy problem

## Primitive Obsession

**Symptom**

- You're using primitive data type to do something more than simple printing.
- Common cases: use string to store money, coordinates, ranges, phone numbers, etc.

**Solution**

- In most cases: Replace Primitive with Object
- IF the primitive acts as type code controlling conditional behavior: `Replace Type Code with Subclasses`, then `Replace Conditional with Polymorphism`

**Benefit**

- Having a class makes it easier to put behavioral specific code

## Repeated Switches

**Symptom**

- The same conditional switching logic pops up in different places

**Issue**

- Whenever you add a clause, you have to find and update all the duplicate switches

**Solution**

- `Replace Conditional with Polymorphism`

## Loops

**Solution**

- Replace Loop with Pipeline

**Benefit**

- Readability: Using pipelines help us quickly see the elements that are included in the processing and what is done with them.

## Lazy Element

**Symptom**

- A function whose content and name are equally easy to read
- A class/subclass that is essentially one simple function

**Cause**

- We want to add structure so badly
- You expect the function/class to grow in the future (YAGNI)
- The class/function was reduced after refactoring

**Issue**

- Unnecessary structures reduce code readability

**Solution**

- `Inline Function`, or `Inline Class `
- For subclass: `Collapse Hierarchy`

## Speculative Generality

**Symptom**

- Have over-general purposed code because you think you will need it In the future (YAGNI)

**Issue**

- Often difficult to understand and maintain

**Solution**

- Abstracted classes that aren't doing much: `Collapse Hierarchy`
- Unnecessary delegation: `Inline Function`, `Inline Class `
- Functions with unused/unneeded parameters: `Change Function Declaration`
- Then only users of the function/class are test cases: delete test, then Remove Dead Code

## Temporary Field

**Symptom**

- A field of a class is set only in certain circumstances

**Issue**

- Code is difficult to understand since you will wonder why a property isn't needed

**Solution**

- For the poor orphan fields: `Extract Class`; then move related function with `Move Function`
- For conditional code: Introduce Special Case

## Message Chains

**Symptom**

- A client asks one object for another object, which asks for yet another object, and so on

**Issue**

- The client is coupled to the structure of the navigation: any change to the intermediate object/structure means the client has also to change

**Solution**

- `Hide Delegation`. (May create Middle Man)
- Even better: observe, and see if you can `Extract Function` and `Move Function` to avoid the chain

## Middle Man

**Symptom**

Half of a class's methods are delegating to another class.

**Solution**

- `Remove Middle Man`
- ❓IF only a few class methods are not delegating: use `Inline Function` to inline them into the caller
- If there is additional behavior other than delegation: `Replace Superclass with Delegate`; `Replace Subclass with Delegate`

## Insider Trading

**Symptom**

- Modules are trading data around too much

**Issue**

- Increased coupling

**Solution**

- Modules whisper to each other: separate them by `Move Function` and `Move Field`
- Modules have common interests: create a third module for the commonality, or Hide Delegate
- `Replace Subclass with Delegate` or `Replace Superclass with Delegate`

## Large Class

**Symptom**

- A class has too many fields
- A class has too much code

**Root Cause**

- The class is doing too much

**Solution**

- IF some variables make sense to be in a component: `Extract Class`
  - Common prefixes/suffixes are also a sign of grouping
- IF the component makes sense with inheritance: `Extract Superclass` or `Replace Type Code with Subclasses`
- IF a class has too much code: find and remove duplicated code

## Alternative Classes with Different Interfaces

**Issue**

- You want different classes to be able to substitute with each other.

**Solution**

- `Change Function Declaration` to make functions match up
- `Move Function` to move behavior into classes until they match
- IF leads to duplication: `Extract Superclass`

## Data Class

**Symptom**

- A class has fields, getters and setters for the fields, and nothing else

**Issue**

- Data classes are often being manipulated in far too much detail by other classes

**Root Cause**

- Usually: You put the behavior on the data in the wrong place: they should be moved into the data class itself.
- Exception: the result is being used by a distinct function invocation (for example, client)

**Solution**

- `Encapsulate Record`
- `Remove Setting Method` on any filed that should not be changed
- IF these getters and setters are used by other classes: `Move Function` to move behavior into the data class. IF not directly movable: `Extract Function` on the movable part first.

## Refused Bequest

| Symptom                                                      | Root Cause             | Solution                                                     |
| ------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ |
| Subclasses don't need the methods and data of their parents  | The hierarchy is wrong | Create a new sibling class, then Push Down Method and Push Down Field |
| Subclasses reuse the behavior but does not want to support the superclass's interface |                        | `Replace Subclass with Delegate` `Replace Superclass with Delegate` |

## Comments

In most cases: comments are there because the code is bad.

**Issue**

- Comments rot
- Comments are a deodorant for bad code

**Solution**

- IF you need to explain what a block of code does: `Extract Function`
- IF you need to explain what a method does: `Change Function Declaration` to rename the function
- IF you need to state some rules about the required state of the system: `Introduce Assertion`
# tecnicas-refactorizacion
