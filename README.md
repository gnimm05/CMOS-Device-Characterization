# CMOS Device Characterization

## 1. Project Purpose and Justification
The purpose of this project is to bridge theoretical solid-state device physics with practical simulation techniques. By characterizing NMOS and PMOS devices using an industry-standard open-source process design kit (PDK), the project validates fundamental semiconductor behaviors and establishes a verifiable baseline for future, more complex integrated circuit (IC) designs.

## 2. Project Objectives
* **Design and Simulate**: Develop robust SPICE testbenches for single-transistor NMOS and PMOS configurations.
* **Parameter Extraction**: Accurately extract critical device parameters, specifically I-V (current-voltage) characteristics and threshold voltages ($V_t$).
* **Behavioral Analysis**: Evaluate transfer curves and subthreshold behaviors to understand off-state leakage and turn-on characteristics.
* **Data Automation**: Utilize Python to process simulation output data and generate clear, analytical visualizations.

## 3. Project Scope
### In Scope
* Writing and executing Ngspice netlists for DC sweep analyses.
* Integration of the SkyWater 130nm PDK libraries into the simulation environment.
* Generation of output characteristics (I_d-V_ds) and transfer characteristics (I_d-V_g).
* Calculation of threshold voltage and subthreshold swing.
* Python scripting for data parsing and plotting.

## 4. Deliverables
* **Simulation Environment Setup**: A configured directory with the Sky130 PDK and base Ngspice simulation files.
* **Testbench Suite**: A collection of `.spice` netlist files for NMOS and PMOS characterization.
* **Python Codebase**: Scripts developed to automate the reading of Ngspice raw data and the generation of I-V plots.
* **Characterization Log/Report**: Documented findings comparing the simulated transfer curves and subthreshold behaviors against theoretical solid-state physics models.

## 5. Tools and Technologies
* **Simulation Engine**: Ngspice
* **Technology Node**: SkyWater 130nm PDK (Sky130)
* **Data Analysis & Visualization**: Python (libraries such as `numpy`, `pandas`, and `matplotlib`)

## 6. Success Criteria
* Simulations converge successfully without netlist or PDK integration errors.
* Generated I-V curves accurately reflect the expected behaviors of short-channel devices at the 130nm node (e.g., velocity saturation, channel length modulation).
* Threshold voltages and subthreshold parameters are successfully quantified and align with the PDK's nominal documentation.
