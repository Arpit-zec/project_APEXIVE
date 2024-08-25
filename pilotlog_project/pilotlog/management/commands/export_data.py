import os
import csv
from django.core.management.base import BaseCommand
from pilotlog.models import Aircraft, Flight  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Export aircraft and flight data to CSV files'

    def handle(self, *args, **kwargs):
        file_path = os.path.join('pilotlog_project', 'pilotlog', 'required_resource')
        file_aircraft = file_path + '\export_aircraft.csv'
        file_flight = file_path + '\export_flight.csv'

        try:
            self.export_aircraft_to_csv(file_aircraft)
            self.export_flights_to_csv(file_flight)
            self.stdout.write(self.style.SUCCESS(f'Successfully exported data to {file_aircraft} and {file_flight}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))

    def export_aircraft_to_csv(self, file_path):
        """Exports aircraft data to a CSV file."""
        
        # Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Define the headers
        headers = [
            "AircraftID", "EquipmentType", "TypeCode", "Year", "Make", "Model", "Category",
            "Class", "GearType", "EngineType", "Complex", "HighPerformance", "Pressurized", "TAA"
        ]

        # Retrieve all aircraft data
        aircrafts = Aircraft.objects.all()

        # Prepare data for CSV
        data = []
        for aircraft in aircrafts:
            row = {
                "AircraftID": aircraft.guid,
                "EquipmentType": "",  # Placeholder
                "TypeCode": "",       # Placeholder
                "Year": aircraft.record_modified,  # Assuming 'record_modified' maps to 'Year'
                "Make": aircraft.make,
                "Model": aircraft.model,
                "Category": aircraft.category,
                "Class": aircraft.aircraft_class,
                "GearType": "",       # Placeholder
                "EngineType": "",     # Placeholder
                "Complex": 'Yes' if aircraft.complex else 'No',
                "HighPerformance": 'Yes' if aircraft.high_perf else 'No',
                "Pressurized": '',    # Placeholder
                "TAA": 'Yes' if aircraft.aerobatic else 'No'
            }
            data.append(row)

        # Write data to CSV file
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

    def export_flights_to_csv(self, file_path):
        """Exports flight data to a CSV file."""
        
        # Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Define the headers
        headers = [
            "Date", "AircraftID", "From", "To", "Route", "TimeOut", "TimeOff", "TimeOn", "TimeIn",
            "OnDuty", "OffDuty", "TotalTime", "PIC", "SIC", "Night", "Solo", "CrossCountry",
            "NVG", "NVGOps", "Distance", "DayTakeoffs", "DayLandingsFullStop", "NightTakeoffs",
            "NightLandingsFullStop", "AllLandings", "ActualInstrument", "SimulatedInstrument",
            "HobbsStart", "HobbsEnd", "TachStart", "TachEnd", "Holds", "Approach1", "Approach2",
            "Approach3", "Approach4", "Approach5", "Approach6", "DualGiven", "DualReceived",
            "SimulatedFlight", "GroundTraining", "InstructorName", "InstructorComments", 
            "Person1", "Person2", "Person3", "Person4", "Person5", "Person6", "FlightReview", 
            "Checkride", "IPC", "NVGProficiency", "FAA6158", "[Text]CustomFieldName",
            "[Numeric]CustomFieldName", "[Hours]CustomFieldName", "[Counter]CustomFieldName",
            "[Date]CustomFieldName", "[DateTime]CustomFieldName", "[Toggle]CustomFieldName",
            "PilotComments"
        ]

        # Retrieve all flight data
        flights = Flight.objects.select_related('aircraft_id').all()

        # Open the file for writing
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            
            # Writing the data rows
            for flight in flights:
                row = [
                    flight.date, flight.aircraft_id.id if flight.aircraft_id else None,
                    flight.from_airport, flight.to_airport, flight.route,
                    flight.time_out, flight.time_off, flight.time_on, flight.time_in,
                    flight.on_duty, flight.off_duty, flight.total_time, flight.pic, flight.sic,
                    flight.night, flight.solo, flight.cross_country, flight.nvg, flight.nvg_ops,
                    flight.distance, flight.day_takeoffs, flight.day_landings_full_stop,
                    flight.night_takeoffs, flight.night_landings_full_stop, flight.all_landings,
                    flight.actual_instrument, flight.simulated_instrument, flight.hobbs_start,
                    flight.hobbs_end, flight.tach_start, flight.tach_end, flight.holds,
                    flight.approach, flight.instructor_name, flight.instructor_comments,
                    flight.pilot_comments, flight.flight_review, flight.checkride, flight.ipc
                ]
                writer.writerow(row)
