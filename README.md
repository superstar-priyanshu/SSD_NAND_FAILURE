# NAND Flash Failure Simulation and Analysis - Kumar Priyanshu's original work

![Project](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## Project Overview

This project simulates the wear and failure patterns of NAND flash memory blocks to better understand how SSD memory devices degrade over time under intensive use. The simulation uses Python to model program/erase cycles and analyze failure rates as the number of cycles increases. This is especially useful in designing and optimizing test strategies for embedded Flash products like SSDs or mobile memory.

## Features

- **Simulates NAND Block Wear and Tear**: Models the wear of memory blocks over time as they undergo program/erase cycles.
- **Failure Detection**: Tracks when blocks fail after crossing a defined wear threshold.
- **Data Visualization**: Provides graphs showing the failure rate and average wear across all memory blocks over time.
- **Configurable Parameters**: Adjust the number of blocks, cycles, and failure thresholds to match real-world scenarios.

## How It Works

- The project initializes a set number of memory blocks (1,000 by default) and simulates wear on these blocks through a specified number of program/erase cycles (5,000 by default).
- Each block has a wear threshold (set to 3,000 cycles), after which it is marked as failed.
- The simulation tracks and plots the number of failed blocks and the average wear level throughout the cycles.

### Visualizations

The project provides two key visualizations:
1. **Failure Rate Over Time**: Shows the number of memory blocks that fail as the number of cycles increases.
2. **Average Block Wear**: Tracks the average wear across all blocks over time.

## Usage

To run this simulation, ensure you have Python installed and the necessary libraries.

### Prerequisites

You'll need the following Python libraries:

```bash
pip install numpy matplotlib
