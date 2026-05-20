"""Лабораторная работа 4, вариант 4 
Предметная область: Brassica oleracea, Solanum lycopersicum"""
from modules import analyze_gc, translate_sequences, fetch_sequences

ANALYZE_GC_OUTPUT = "output/analyze_gc_output.txt"
TRANSLATE_SEQUENCES_OUTPUT  = "output/translate_sequences_output.txt"
input_file = "sequences.gb"

if __name__ == "__main__":
    while(True):
        validator = input("Подгрузить данные или использовать существующие?(y or n)")
        if(validator == "y"):
            fetch_sequences.fetch_sequences(["PL494176.1","PL494175.1","PL494174.1",
                                             "PL494172.1", "PL494173.1","CM100936.1",
                                             "CM100938.1","CM100940.1","JBJXBP010000005.1",
                                             "CM100935.1"])
            input_file = "fetched_sequence.gb"
            break
        if(validator == "n"):
            break
        print("Неверный формат  ввода,введите y или n")
    try:
        analyze_gc.analyze(input_file,ANALYZE_GC_OUTPUT)

        cds_results = fetch_sequences.fetch_cds_data(input_file)
        translate_sequences.translate(cds_results,TRANSLATE_SEQUENCES_OUTPUT)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{FileNotFoundError.filename}' не найден.")
