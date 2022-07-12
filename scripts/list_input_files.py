import sys
import pathlib


def main(files_dir='/tmp/'):
    lines = []
    for vid_file in pathlib.Path(files_dir).iterdir():
        if vid_file.is_file() and vid_file.suffix != '.txt':
            lines.append(f'file {vid_file.name}\n')

    concat_file_path = pathlib.Path(files_dir) / 'concat.txt'
    with open(concat_file_path, 'w', encoding='utf-8') as concat_file:
        concat_file.writelines(sorted(lines))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
