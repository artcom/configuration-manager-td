import logging
from pathlib import Path
import requests


class ConfigurationController:

    def __init__(self, ownerComp):
        self._owner_comp = ownerComp
        self._logger = logging.getLogger(self.__class__.__name__)

    def OnConfigurationChange(self):
        self._logger.info("configuration changed")
        self.DownloadConfiguration()

    def _create_download_directories(self, bootstrap_config_file: str, app_config_file: str):
        Path(bootstrap_config_file).parent.mkdir(parents=True, exist_ok=True)
        Path(app_config_file).parent.mkdir(parents=True, exist_ok=True)

    def DownloadConfiguration(self):
        self._logger.info("downloading configuration")
        config = self._owner_comp.op('config').result
        bootstrap_config = config['bootstrapConfig']
        bootstrap_config_file = config['bootstrapConfigFile']
        app_config = config['appConfig']
        app_config_file = config['appConfigFile']

        self._create_download_directories(
            bootstrap_config_file,
            app_config_file
        )

        self._download_file(bootstrap_config, bootstrap_config_file)
        self._download_file(app_config, app_config_file)

        self._logger.info("download complete")
        self._refresh_configuration()

    def _refresh_configuration(self):
        self._owner_comp.op('bootstrap_config_json').par.refresh.pulse()
        self._owner_comp.op('app_config_json').par.refresh.pulse()

    def _download_file(self, url: str, filepath: str) -> dict:
        try:
            with requests.get(url, stream=True, timeout=10) as r:
                r.raise_for_status()
                with open(filepath, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
        except requests.Timeout as e:
            self._logger.error(e)
        except Exception as e:
            self._logger.error(e)
