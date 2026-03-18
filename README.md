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

Load the tox into your project:

1. drag into your project
2. Common -> Enable External .tox = ON
3. Common -> External .tox Path = set to tox file
4. Common -> Reload custom parameters = OFF

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

Callbacks will inform over status:

| Callback           | Description                        |
| :----------------- | :--------------------------------- |
| `onUpdateStart`    | Download of configuration started  |
| `onUpdateFinished` | Download of configuration finished |
| `onUpdateFailure`  | Download of configuration failed   |
