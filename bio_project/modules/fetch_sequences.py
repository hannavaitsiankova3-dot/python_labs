""""Модуль для получения CDS"""

from Bio import SeqIO, Entrez
from Bio.Seq import UndefinedSequenceError

Entrez.email = "hannavaitsiankova3@gmail.com"

def fetch_cds_data(input_file):
    """
    Считывает GenBank файл, извлекает CDS, транслирует их 
    и возвращает список словарей с результатами.
    """
    results = []

    try:
        records = list(SeqIO.parse(input_file, "genbank"))
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return results

    for record in records:
        try:
            if not record.seq or len(record.seq) == 0:
                continue
        except UndefinedSequenceError:
            continue

        for feature in record.features:
            if feature.type == "CDS":
                try:
                    # 1. Извлекаем нуклеотидную последовательность CDS
                    cds_seq = feature.extract(record.seq)
                    # 2. Транслируем в белок
                    protein_seq = cds_seq.translate(to_stop=True)
                    # 3. Получаем информацию о локации и цепи
                    location = feature.location
                    strand_val = location.strand

                    if strand_val == 1:
                        strand_str = "+"
                    elif strand_val == -1:
                        strand_str = "-"
                    else:
                        strand_str = "?"

                    # 4. Формируем словарь с данными для текущей CDS
                    cds_data = {
                        "id": record.id,
                        "description": record.description,
                        "location": location,
                        "strand": strand_str,
                        "translation": protein_seq
                    }
                    results.append(cds_data)

                except Exception as e:
                    print(f"Предупреждение: Ошибка при обработке CDS в {record.id}: {e}")

    return results


def fetch_from_ncbi(accession_number, output_file="fetched_sequence.gb"):
    """
    Получает последовательность из NCBI по номеру аккессии
    и сохраняет её в формате GenBank.
    """
    try:
        print(f"Получаю последовательность {accession_number} из NCBI...")
        
        handle = Entrez.efetch(
            db="nucleotide", 
            id=accession_number, 
            rettype="gb",  # GenBank формат
            retmode="text"
        )
        
        # Парсим результат
        record = SeqIO.read(handle, "genbank")
        handle.close()
        
        # Сохраняем в файл
        SeqIO.write(record, output_file, "genbank")
        print(f"✓ Последовательность сохранена в {output_file}")
        print(f"  ID: {record.id}")
        print(f"  Длина: {len(record.seq)} нуклеотидов")
        print(f"  Описание: {record.description}")
        
        return record
        
    except Exception as e:
        print(f"Ошибка при получении последовательности: {e}")
        return None


def fetch_sequences(accession_list: list, output_file="fetched_sequence.gb"):
    """
    Получает несколько последовательностей из NCBI
    и сохраняет их в один файл.
    """
    records = []
    
    for accession in accession_list:
        try:
            print(f"Получаю {accession}...")
            handle = Entrez.efetch(
                db="nucleotide",
                id=accession,
                rettype="gb",
                retmode="text"
            )
            record = SeqIO.read(handle, "genbank")
            handle.close()
            records.append(record)
            print(f"  ✓ {accession} получена ({len(record.seq)} нуклеотидов)")
            
        except Exception as e:
            print(f"  ✗ Ошибка при получении {accession}: {e}")
    
    if records:
        SeqIO.write(records, output_file, "genbank")
        print(f"\n✓ {len(records)} последовательность(й) сохранена(ны) в {output_file}")
    
    return records
