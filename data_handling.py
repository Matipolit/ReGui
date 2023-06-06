from pathlib import Path
import logging
import json
import praw
import webbrowser

from get_code_server import get_code


class DataHandler:
    data_struct = {"token": ""}

    def __init__(self):
        self.program_path = Path.home().joinpath(".regui")
        if not self.program_path.exists():
            logging.debug("creating program dir")
            self.program_path.mkdir()

        self.settings_file = self.program_path.joinpath("settings.json")
        if not self.settings_file.exists():
            logging.debug("creating settings file")
            self.settings_file.touch()

        self.data_file = self.program_path.joinpath("data.json")
        if not self.data_file.exists():
            logging.debug("creating data file")
            self.data_file.touch()
            self.write_dict_to_file(self.data_file, DataHandler.data_struct)

        self.data = self.get_dict_from_file(self.data_file)

    def write_dict_to_file(self, file_path: Path, dict: dict):
        file = file_path.open("w")
        file.write(json.dumps(dict))
        file.close

    def get_dict_from_file(self, file_path: Path) -> dict:
        file = file_path.open("r")
        json_str = file.read()
        file.close()
        return json.loads(json_str)

    def save_data(self):
        self.write_dict_to_file(self.data_file, self.data)

    def get_token(self) -> str | None:
        if self.data["token"] == "":
            return None
        else:
            return self.data["token"]

    def authorize_first_time(self, reddit: praw.Reddit):
        auth_url = reddit.auth.url(
            scopes=[
                "account",
                "edit",
                "identity",
                "vote",
                "mysubreddits",
                "read",
                "save",
                "submit",
                "subscribe",
            ],
            state="1",
            duration="permanent",
        )
        logging.debug(auth_url)
        webbrowser.open(auth_url)
        code = get_code()
        logging.debug(f"received code: {code}")

        refresh_token = reddit.auth.authorize(code)
        self.data["token"] = refresh_token
        self.save_data()
