# Band-stop Filter

|           |                                                                                       |
| --------- | ------------------------------------------------------------------------------------- |
| name      | Band-stop Filter                                                                      |
| version   | v1.0.1                                                                                |
| DockerHub | [beetaone/bandstop-filter](https://hub.docker.com/r/beetaone/bandstop-filter) |
| authors   | Paul Gaiduk                                                                           |

***
## Table of Content

- [Band-stop Filter](#band-stop-filter)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the beetaone Agent on the edge-node](#set-by-the-beetaone-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
***

## Description

Module that filters out frequencies.

## Environment Variables

| Environment Variables | type   | Description                                                     |
| --------------------- | ------ | --------------------------------------------------------------- |
| FREQUENCY_RANGES      | string | Ranges of acceptable frequencies (in Hz) separated by semicolon |

### Module Specific

### Set by the beetaone Agent on the edge-node

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| INGRESS_HOST          | string | Host where app is running                      |
| INGRESS_PORT          | string | Port where app is running                      |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module         |

## Dependencies

The following are module dependencies:

* bottle
* requests

The following are developer dependencies:

* pytest
* flake8
* black

## Input

Input to this module is a JSON array, that contains "frequency" fields:

```json
[
    {
        "frequency": 270,
        "magnitude": 2
    },
    {
        "frequency": 6,
        "magnitude": 25
    }
]
```


## Output
Output of this module is JSON body the same as input data, but only containing the entries, whose frequencies DON'T fit into FREQUENCY_RANGES:

```json
[
    {
        "frequency": 6,
        "magnitude": 25
    }
]
```