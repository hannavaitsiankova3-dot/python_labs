from Bio import SeqIO
from Bio.Seq import UndefinedSequenceError

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
        # Пропускаем записи без последовательности
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