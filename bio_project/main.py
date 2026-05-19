"""Лабораторная работа 4, вариант 4 
Предметная область: Brassica oleracea, Solanum lycopersicum"""

from modules import analyze_gc, translate_sequences, fetch_sequences

ANALYZE_GC_OUTPUT = "output/analyze_gc_output.txt"
TRANSLATE_SEQUENCES_OUTPUT  = "output/translate_sequences_output.txt"
INPUT_FILE = "sequences.gb"

if __name__ == "__main__":
    try:
        analyze_gc.analyze(INPUT_FILE,ANALYZE_GC_OUTPUT)

        cds_results = fetch_sequences.fetch_cds_data(INPUT_FILE)
        translate_sequences.translate(cds_results,TRANSLATE_SEQUENCES_OUTPUT)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{INPUT_FILE}' не найден.")
