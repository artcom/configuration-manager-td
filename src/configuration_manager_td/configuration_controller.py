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
        self._owner_comp.DoCallback('onUpdateStart')

        config = self._owner_comp.op('config').result
        bootstrap_config = config['bootstrapConfig']
        bootstrap_config_file = config['bootstrapConfigFile']
        app_config = config['appConfig']
        app_config_file = config['appConfigFile']

        self._create_download_directories(
            bootstrap_config_file,
            app_config_file
        )

        err_boostrap = self._download_file(
            bootstrap_config, bootstrap_config_file)
        if err_boostrap:
            info = {'error': err_boostrap}
            self._owner_comp.DoCallback('onUpdateFailure', info)

        err_app = self._download_file(app_config, app_config_file)
        if err_app:
            info = {'error': err_app}
            self._owner_comp.DoCallback('onUpdateFailure', info)

        if err_boostrap is None and err_app is None:
            self._logger.info("download complete")
            self._refresh_configuration()
            self._owner_comp.DoCallback('onUpdateFinished')

    def _refresh_configuration(self):
        self._owner_comp.op('bootstrap_config_json').par.refresh.pulse()
        self._owner_comp.op('app_config_json').par.refresh.pulse()

    def _download_file(self, url: str, filepath: str) -> bool:
        try:
            with requests.get(url, stream=True, timeout=10) as r:
                r.raise_for_status()
                with open(filepath, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            return None
        except requests.Timeout as e:
            self._logger.error(e)
            return e
        except Exception as e:
            self._logger.error(e)
            return e
