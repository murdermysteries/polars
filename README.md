# Polars Murder Mysteries

A collection of interactive murder mystery notebooks that help users learn data analysis with the Polars library.

## About the Project

Polars Murder Mysteries combines engaging murder mystery scenarios with data analysis using the powerful Polars library. Each mystery provides datasets that you'll analyze to solve the case, learning Polars features along the way.

The mysteries are presented as interactive Jupyter notebooks running entirely in your browser using JupyterLite and WebAssembly - no installation required!

## Available Cases

### Death at the Aurora Theater

A renowned actor has been found dead at the Aurora Theater after the evening performance. As the lead detective, you must analyze police records, witness statements, theater access logs, and staff information to identify the killer.

**Skills you'll learn:** Filtering data, joining tables, grouping and aggregation, and working with timestamps in Polars.

## Technical Details

This project uses:

- [JupyterLite](https://jupyterlite.readthedocs.io/en/latest/) for browser-based notebook execution
- [Polars](https://pola.rs/) for data analysis
- GitHub Actions for automated deployment
- GitHub Pages for hosting

## Local Development

To run this project locally:

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Build the JupyterLite environment:
   ```
   jupyter lite build
   ```
4. Serve the built files:
   ```
   python -m http.server -d _output
   ```
5. Open your browser to http://localhost:8000/landing.html

## Accessing the Notebooks

When running locally or after deployment, you can access the notebooks in two ways:

1. **Landing Page**: Open `landing.html` in the root directory to see the project landing page with links to all available notebooks.

2. **Direct Access**: Navigate to the JupyterLite Lab interface and open the notebook from the files panel:
   - Local: http://localhost:8000/lab/index.html
   - After deployment: https://murdermysteries.github.io/polars/lab/index.html

The notebooks are located in the `files` directory within the JupyterLite environment.

## Deployment

This project is automatically deployed to GitHub Pages using GitHub Actions whenever changes are pushed to the main branch.

## Acknowledgements

This project is inspired by the [SQL Murder Mystery](https://mystery.knightlab.com/).
