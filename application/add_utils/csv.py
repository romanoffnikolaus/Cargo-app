import csv
import time

from application.models import Location


def import_csv_to_database(csv_file_path):
    start_time = time.time()
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        existing_zip_codes = Location.objects.values_list('zip_code', flat=True)
        print('Проверка данных из csv файла...')
        
        new_locations = []
        
        for row in reader:
            zip_code = row['zip']
            if not int(zip_code) in list(existing_zip_codes):
                location = Location(
                    zip_code=row['zip'],
                    latitude=row['lat'],
                    longitude=row['lng'],
                    city=row['city'],
                    state_id=row['state_id'],
                    state_name=row['state_name'],
                    zcta=True if row['zcta'].lower() == 'true' else False,
                    parent_zcta=row['parent_zcta'],
                    population=None if row['population'] == '' else row['population'],
                    density=None if row['density'] == '' else row['density'],
                    county_fips=row['county_fips'],
                    county_name=row['county_name'],
                    county_weights=row['county_weights'],
                    county_names_all=row['county_names_all'],
                    county_fips_all=row['county_fips_all'],
                    imprecise=True if row['imprecise'].lower() == 'true' else False,
                    military=True if row['military'].lower() == 'true' else False,
                    timezone=row['timezone'],
                )
                new_locations.append(location)

        Location.objects.bulk_create(new_locations)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Время выполнения import_csv_to_database: {total_time} секунд")

