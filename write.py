"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    # with open(filename, 'w', newline= '') as outfile:
        # writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # writer.writeheader()
        # for approach in results:
        #     neo = approach.neo
        #     row = {
        #         'datetime_utc': approach.time_str,
        #         'distance_au': approach.distance,
        #         'velocity_km_s': approach.velocity,
        #         'designation': neo.designation,
        #         'name': neo.name or '',
        #         'diameter_km': neo.diameter or '',
        #         'potentially_hazardous': str(neo.hazardous) if neo.hazardous is not None else ''
        #     }
        #     writer.writerow(row)
    with open(filename, "w", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                content = {**result.serialize(), **result.neo.serialize()}
                content["name"] = content["name"] if content["name"] is not None else ""
                content["potentially_hazardous"] = "True" if content["potentially_hazardous"] else "False"
                writer.writerow(content)



def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.

    json_list = []
    for approach in results:
        neo = approach.neo
        entry = {
            'datetime_utc': datetime_to_str(approach.time),
            'distance_au': approach.distance,
            'velocity_km_s': approach.velocity,
            'neo': {
                'designation': neo.designation,
                'name': neo.name or '',
                'diameter_km': neo.diameter or float('nan'),
                'potentially_hazardous': neo.hazardous
            }

        }
        json_list.append(entry)
    with open(filename, 'w') as outfile:
        json.dump(json_list, outfile, indent=2)

