import datetime
import os

class Logger:
    def __init__(self):
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        self.file_name = f"{logs_dir}/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    def write_log_to_file(self, data: str):
        with open(self.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    def add_start_step(self, url: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"\n-----\nTest: {test_name}\nStart time: {str(datetime.datetime.now())}\nStart URL: {url}\n\n"
        self.write_log_to_file(data_to_add)

    def add_end_step(self, url: str, method: str):
        data_to_add = f"End time: {str(datetime.datetime.now())}\nEnd name method: {method}\nURL: {url}\n\n-----\n"
        self.write_log_to_file(data_to_add)