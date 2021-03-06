"""This is the description of the {{ cookiecutter.first_module_name }} module."""
{%- if cookiecutter.use_fire == "y" %}
import fire
import fire_workarounds
{%- endif %}


def hello(name='world'):
    """Returns a greeting.
    """
    return f'Hello, {name}!'


if __name__ == '__main__':
{%- if cookiecutter.use_fire == "y" %}
    fire_workarounds.apply()
    fire.Fire({
        "hello": hello
    })
{%- else %}
    print(hello())
{%- endif %}
