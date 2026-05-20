"""Модуль для анализа последовательностей по условию задания 2"""
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from Bio.Seq import UndefinedSequenceError

def analyze(input_file, output_file):
    """Задание 2: Считать все записи, вычислить GC-состав и
   вывести последовательности в порядке возрастания GC-состава."""
    print("--- Задание 2: GC-составы (в порядке возрастания) ---")
    records = list(SeqIO.parse(input_file, "genbank"))
    gc_list = []
    for record in records:
        # Вычисляем GC-состав для всей последовательности записи
        # gc_fraction возвращает значение от 0 до 1
        try:
            # Проверяем, определена ли последовательность
            if len(record.seq) == 0:
                print(f"Пропуск {record.id}: Последовательность пуста.")
                continue
            # Пытаемся вычислить GC
            gc_val = gc_fraction(record.seq)

            info_line = f"{record.id}: {record.description}, GC= {gc_val}"
            gc_list.append((gc_val, info_line))

        except UndefinedSequenceError:
            print(f"Содержимое последовательности {record.id} не определено")
            continue
    gc_list.sort(key=lambda x: x[0])
    
    with open(output_file, "w",encoding="utf-8") as output_handle:
        for _, line in gc_list:
            output_handle.write(line+'\n')
        print(f"Сохранено в файл '{output_file}'")
