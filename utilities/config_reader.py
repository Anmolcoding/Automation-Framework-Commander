from pathlib import Path
import yaml


class ConfigReader:
    """Utility to load environment and browser configuration from YAML files."""

    def __init__(self, config_path: str = None):
        self.config_path = config_path or Path("configs/config.yaml")
        self._config = self._load_config()

    def _load_config(self) -> dict:
        config_file = Path(self.config_path)
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        with config_file.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)

    def get(self, key: str, default=None):
        return self._config.get(key, default)

    def get_default_config(self) -> dict:
        return self._config.get("default", {})

    def get_environment_config(self) -> dict:
        default_config = self.get_default_config().copy()
        env_name = default_config.get("environment", "qa")
        env_config = self._config.get("environments", {}).get(env_name, {})
        merged = {**default_config, **env_config}
        merged["environment"] = env_name
        return merged

    def get_environment_name(self) -> str:
        return self.get_default_config().get("environment", "qa")
