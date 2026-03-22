# TouchDesigner Configuration Manager Component

TD Component to download configuration files from ACMS.

## Requirements

- Touchdesigner  >= 2023.12370
- Python 3.11

## Installation

Add this dependency to your `requirements.txt`:

```sh
configuration-manager-td @ git+https://github.com/artcom/configuration-manager-td.git@0.1.0#egg=configuration-manager-td
```

Load the tox into your project:

1. create a baseCOMP
2. Common -> External .tox Path = `mod.configuration_manager_td.ToxFile`
3. Common -> Enable External .tox = ON
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
