# Getting Started with Macros

## Simple Example
The example below is a macro that returns a simple hello world message. We will assume the following is in the macros folder under hello.html
```
{% macro hello() %}
  <h1>Hello Flask!<h1>
{% endmacro %}
```

To use the macro we need to import it into our template. Our import will assume the templates folder is the root location so keep this in mind when importing your macro. Once imported you can call the macro and see the return. 
```
{% from "macros/hello.html" import hello %}
{{ hello() }}
```

## Adding parameters
Sometimes you need to be able to pass data to your macro. In our example above we will update the macro to expect a message parameter.
```
{% macro hello(msg) %}
  <h1>Hello {{msg}}!<h1>
{% endmacro %}
```

Now we can update the macro we imported earlier and pass an argument to the macro.
```
{% from "macros/hello.html" import hello %}
{{ hello("World") }}
```

For more information you can visit the [Jinja docs for Macros](https://jinja.palletsprojects.com/en/3.1.x/templates/#macros). 
