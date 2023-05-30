# Near-Earth Object Explorer

The Near-Earth Object (NEO) Explorer is a Python script that allows you to explore a dataset of near-Earth objects and their close approaches to Earth. It provides functionality to query for specific close approaches and inspect individual NEOs.

## Dependencies

- Python 3.6 or above

## Installation

1. Clone the repository: 
	$ git clone [https://github.com/your_username/neo-explorer.git](https://github.com/your_username/neo-explorer.git) 
	$ cd neo-explorer
2. Install the requrited dependencies.

## Usage 
The script can be invoked from the command line with the following subcommands: 
### Inspect 
To inspect an NEO by primary designation or name, use the `inspect` subcommand:
1. $ python3 main.py inspect --pdes 1P 
2. $ python3 main.py inspect --name Halley 
3. $ python3 main.py inspect --verbose --name Halley

The `--pdes` option specifies the primary designation of the NEO, while the `--name` option specifies the IAU name of the NEO. Use the `--verbose` flag to display all known close approaches of the NEO.

### Query

To search for close approaches that match specific criteria, use the `query` subcommand:
1. $ python3 main.py query --date 2022-05-29 $ python3 main.py query --start-date 2023-01-01 --end-date 2023-12-31 --max-distance 0.025 
2. $ python3 main.py query --start-date 2023-01-01 --min-distance 0.1 --min-velocity 50 $ python3 main.py query --date 2023-05-29 --max-velocity 25 --min-diameter 0.5 --hazardous 
3. $ python3 main.py query --start-date 2023-01-01 --max-diameter 0.1 --not-hazardous 
4. $ python3 main.py query --hazardous --max-distance 0.05 --min-velocity 30

You can specify various filters such as date, distance, velocity, diameter, and hazard status using the corresponding options. The `--limit` option can be used to restrict the number of matches returned. The results can be saved to an output file using the `--outfile` option.

### Interactive Shell

The script also provides an interactive shell that allows you to repeatedly execute `inspect` and `query` commands without reloading the database each time:

$ python3 main.py interactive

In the interactive shell, you can use the `inspect` and `query` commands with the same options as described above. You can exit the shell by typing `exit` or pressing Ctrl+C.

## Data Files

By default, the script loads the NEO data from the `data/neos.csv` file and the close approach data from the `data/cad.json` file. If you want to use custom data files, you can specify the paths using the `--neofile` and `--cadfile` options.

For more details about the project and the data files, refer to the [project documentation](https://github.com/CorrosiveMoon/Near-Earth-Objects).








