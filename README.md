# Graph Ping

Graph Ping is a tool designed to visualize network latency over time using graphical representations. It helps in understanding the network performance and identifying potential issues.

## Features

- **Network Latency Measurement**: Continuously pings a specified host and measures the round-trip time.
- **Graphical Visualization**: Displays the latency data in a graphical format for easier analysis.
- **Customizable**: Allows users to specify the target host, interval, and duration of the pings.

## Installation

To use Graph Ping, you need to have Python installed on your machine. Follow the steps below to install the necessary dependencies and run the project:

1. Clone the repository:
    ```sh
    git clone https://github.com/EarlHikky/graph-ping.git
    cd graph-ping
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start using Graph Ping, run the following command:

```sh
python ping.py --host example.com --interval 1 --duration 60
```

- `--host`: The target host to ping (default is `example.com`).
- `--interval`: Time interval between pings in seconds (default is `1` second).
- `--duration`: Total duration for which the pings should be sent in seconds (default is `60` seconds).

## Example

Here is an example command to ping `google.com` every second for one minute and visualize the results:

```sh
python graph_ping.py --host google.com --interval 1 --duration 60
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
