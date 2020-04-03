Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-esp32connection/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/esp32connection/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/jimbobbennett/CircuitPython_ESP32Connection/workflows/Build%20CI/badge.svg
    :target: https://github.com/jimbobbennett/CCircuitPython_ESP32Connection/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A WiFi connection helper for ESP32-based boards. This works on PyBadges with Airlift FeatherWings, or PyPortals.
It may work on other ESP32 devices, but hasn't been tested. 

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-esp32connection/>`_. To install for current user:

.. code-block:: shell

    pip3 install circuitpython-esp32connection

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-esp32connection

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-esp32connection

Usage Example
=============

.. code-block:: python

    esp32connection.connect(secrets["ssid"], secrets["password"], True)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/jimbobbennett/CircuitPython_ESP32Connection/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
