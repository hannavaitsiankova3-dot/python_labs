"""Лабораторная работа 4, вариант 4"""
"""Предметная область: Brassica oleracea, Solanum lycopersicum"""
import modules
from modules import analyze_gc, translate_sequences, fetch_sequences

analyze_gc_output = "output/analyze_gc_output.txt"
translate_sequences_output  = "output/transate_sequences_output.txt"
input_file = "sequences.gb"

if __name__ == "__main__":
    try:
        analyze_gc.analyze(input_file,analyze_gc_output)
        
        cds_results = fetch_sequences.fetch_cds_data(input_file)
        translate_sequences.translate(cds_results,translate_sequences_output)
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")