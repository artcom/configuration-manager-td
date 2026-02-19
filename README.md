# TouchDesigner Configuration Manager Component

Component to download configuration files from ACMS.

## Requirements

- Touchdesigner  >= 2023.12370
- Python 3.11

## Installation

Copy this directory into the "external" folder on the base directory of your project:

```sh
./external/configuration-manager
```

Load the tox into your project

In the "Common" page set "Reload custom parameters" to "OFF"

## Usage

Parameters on page "Input":

| Parameter    | Description                     |
| :----------- | :------------------------------ |
| `ConfigPath` | Path th the local `config.json` |
| `Download`   | Manual trigger for download     |

To download configurations use method call:

```py
op.ConfigurationManager.DownloadConfiguration()
```
