Title: Types as function arguments in Julia
Date: 2013-06-27 12:25
Category: Julia
Tags: types as tags
Slug: types-as-function-arguments-in-julia
Author: Nick Foti

The multiple dispatch mechanism in Julia makes passing types as arguments to
functions desirable.  This technique is sometimes referred to as "types as
tags" and a contrived example is presented below.

``` julia
type A
end

type B
end

f(::Type{A}) = println("f with type A")
f(::Type{B}) = println("f with type B")

f(A)
f(B)
```
