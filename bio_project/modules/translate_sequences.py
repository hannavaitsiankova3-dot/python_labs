import os

def translate(data_list, output_file):
    """
    Сохраняет список полученных данных трансляции в выходной файл.
    """
    if not data_list:
        print("Нет данных для сохранения.")
        return

    with open(output_file, "w") as output_handle:
        for item in data_list:
            output_handle.write(f"{item['id']}: {item['description']}\n")
            output_handle.write(f"Coding sequence location={item['location']}({item['strand']})\n")
            output_handle.write(f"Translation=\n{item['translation']}\n\n")
            
    print(f"Успешно сохранено {len(data_list)} записей в файл '{output_file}'")