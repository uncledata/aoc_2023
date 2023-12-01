from helpers import read_file_str, INPUTS_PATH, DEMO_PATH, download_input

IS_PROD = True
DAY = 2

if __name__ == "__main__":
    if IS_PROD:
        download_input(str(DAY))
    file_path = INPUTS_PATH.format(str(DAY)) if IS_PROD else DEMO_PATH.format(str(DAY))
    lines = read_file_str(file_path)
