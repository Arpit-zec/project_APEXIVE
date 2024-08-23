import json
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from pilotlog.models import Aircraft, Flight  

class Command(BaseCommand):
    
    help = "Import data from JSON file into the database"

    def handle(self, *args, **kwargs):
        # Path to the JSON file (modify as needed)
        json_file_path = os.path.join(
            settings.BASE_DIR, 'pilotlog', 'required_resource', 'import - pilotlog_mcc.json'
        )
        print("successfully open")
        print(json_file_path)
         
        # Open and load the JSON data
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Iterate over each record in the JSON data
        for record in data:
            table_name = record['table'].lower()  # Convert table name to lowercase
            
            # Handle Aircraft table data
            if table_name == 'aircraft':
                self.import_aircraft(record)
                # Print progress
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {table_name} record: {record["guid"]}'))
                
            # Add other table handling here if necessary
            elif table_name == 'flight':
                self.import_flights(record)
                # Print progress
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {table_name} record: {record["guid"]}'))

    def import_aircraft(self, record):
        # Extract the meta data
        meta = record['meta']

        # Create or update the Aircraft record
        aircraft, created = Aircraft.objects.update_or_create(
            guid=record['guid'],
            defaults={
                'user_id': record['user_id'],
                'platform': record['platform'],
                '_modified': record['_modified'],
                'make': meta.get('Make', ''),
                'model': meta.get('Model', ''),
                'category': meta.get('Category', 0),
                'aircraft_class': meta.get('Class', 0),
                'power': meta.get('Power', 0),
                'seats': meta.get('Seats', 0),
                'active': meta.get('Active', False),
                'reference': meta.get('Reference', ''),
                'tailwheel': meta.get('Tailwheel', False),
                'complex': meta.get('Complex', False),
                'high_perf': meta.get('HighPerf', False),
                'aerobatic': meta.get('Aerobatic', False),
                'fnpt': meta.get('FNPT', 0),
                'kg5700': meta.get('Kg5700', False),
                'rating': meta.get('Rating', ''),
                'company': meta.get('Company', ''),
                'cond_log': meta.get('CondLog', 0),
                'fav_list': meta.get('FavList', False),
                'sub_model': meta.get('SubModel', ''),
                'record_modified': meta.get('Record_Modified', 0),
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created new Aircraft: {aircraft.reference}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated Aircraft: {aircraft.reference}'))
            
    def import_flights(self, record):
        # Extract the meta data
        meta = record['meta']

        # Create or update the Flight record
        flight, created = Flight.objects.update_or_create(
            guid=record['guid'],
            defaults={
                'user_id': record['user_id'],
                'platform': record['platform'],
                '_modified': record['_modified'],
                'aircraft_id': meta.get('AircraftID', ''),
                'from_airport': meta.get('From', ''),
                'to_airport': meta.get('To', ''),
                'route': meta.get('Route', ''),
                'date': meta.get('Date', None),
                'time_out': meta.get('TimeOut', ''),
                'time_off': meta.get('TimeOff', ''),
                'time_on': meta.get('TimeOn', ''),
                'time_in': meta.get('TimeIn', ''),
                'on_duty': meta.get('OnDuty', ''),
                'off_duty': meta.get('OffDuty', ''),
                'total_time': meta.get('TotalTime', 0),
                'pic': meta.get('PIC', 0),
                'sic': meta.get('SIC', 0),
                'night': meta.get('Night', 0),
                'solo': meta.get('Solo', 0),
                'cross_country': meta.get('CrossCountry', 0),
                'nvg': meta.get('NVG', 0),
                'nvg_ops': meta.get('NVGOps', 0),
                'distance': meta.get('Distance', 0),
                'day_takeoffs': meta.get('DayTakeoffs', 0),
                'day_landings_full_stop': meta.get('DayLandingsFullStop', 0),
                'night_takeoffs': meta.get('NightTakeoffs', 0),
                'night_landings_full_stop': meta.get('NightLandingsFullStop', 0),
                'all_landings': meta.get('AllLandings', 0),
                'actual_instrument': meta.get('ActualInstrument', 0),
                'simulated_instrument': meta.get('SimulatedInstrument', 0),
                'hobbs_start': meta.get('HobbsStart', 0),
                'hobbs_end': meta.get('HobbsEnd', 0),
                'tach_start': meta.get('TachStart', 0),
                'tach_end': meta.get('TachEnd', 0),
                'holds': meta.get('Holds', 0),
                'approach1': meta.get('Approach1', ''),
                'approach2': meta.get('Approach2', ''),
                'approach3': meta.get('Approach3', ''),
                'approach4': meta.get('Approach4', ''),
                'approach5': meta.get('Approach5', ''),
                'approach6': meta.get('Approach6', ''),
                'dual_given': meta.get('DualGiven', 0),
                'dual_received': meta.get('DualReceived', 0),
                'simulated_flight': meta.get('SimulatedFlight', 0),
                'ground_training': meta.get('GroundTraining', 0),
                'instructor_name': meta.get('InstructorName', ''),
                'instructor_comments': meta.get('InstructorComments', ''),
                'pilot_comments': meta.get('PilotComments', '')
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created new Flight: {flight.guid}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated Flight: {flight.guid}'))'''

