import time
import os
from pprint import pprint

# def get_file_lines(file_name):
#     with open(file_name) as f:
#         line = f.readline()
#         while line != '':
#             yield line
#             line = f.readline()

# lines = []
# with open('DATA/cinema/name.basics.tsv') as f:
#     for i in range(3):
#         lines.append(f.readline())
# print(lines)
# def find_lines_2():
#     reader = iter(get_file_lines('DATA/cinema/name.basics.tsv'))
#     for i in reader:
#         person = i.strip().split('\t')
#         # print(next(reader).strip().split('\t'))
#         if person[1] == 'Lord Byron':
#             print(person)

# faster
def find_person():
    with open('DATA/cinema/name.basics.tsv') as f:
        for line in iter(f.readline, ''):
            person = line.strip().split('\t')
            if person[1] == 'Lord Byron':
                print(person)

def find_person_films(person):
    films = []
    with open('DATA/cinema/title.crew.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            writers = info[2].split(',')
            if person in writers:
                films.append(info[0])
    return films

def find_films_info(title_ids):
    infos = []
    cp_ids = title_ids.copy()
    with open('DATA/cinema/title.akas.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if (info[0] in cp_ids):
                infos.append(info)
                cp_ids.remove(info[0])
    return infos


def read_first_lines(file_name: str, rows_number: int):
    print(file_name)
    print('-' * 10)
    with open(file_name) as f:
        for _ in range(rows_number):
            print(f.readline().strip())
    print('-' * 10)
    print()

def main():
    directory = './DATA/cinema/'
    # files = [os.path.join(directory, short_name)
    #         for short_name in os.listdir(directory)]
    # for f_name in files:
    #     read_first_lines(f_name, 5)
    person = 'nm0126406'
    title_ids = find_person_films(person)
    infos = find_films_info(title_ids)
    pprint(infos)

start_time = time.time()
main()
print(time.time() - start_time)
