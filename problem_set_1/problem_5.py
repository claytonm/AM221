import requests
import pandas as pd
import sys

# read file into Pandas DataFrame
def get_logs(url: str) -> str:
    log_file = requests.get(url)
    logs = [log.split('\t') for log in log_file.text.split('\n')]
    return pd.DataFrame(logs, columns = ['timestamp','IP_address'])

def get_top_addresses(logs: pd.DataFrame) -> pd.DataFrame:
    top_addresses = (logs
                     .groupby('IP_address')
                     .count()
                     .sort_values('timestamp', ascending=False)
                     .head(10)
                     )
    return top_addresses



if __name__ == '__main__':
    logs = get_logs(sys.argv[1])
    top_addresses = get_top_addresses(logs)
    top_addresses.to_csv(sys.argv[2])
