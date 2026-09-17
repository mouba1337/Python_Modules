import importlib.metadata


def check_dependencies() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    packages = {
        'pandas': 'Data manipulation ready',
        'requests': 'Network access ready',
        'matplotlib': 'Visualization ready',
        'numpy': 'Numerical computation ready'
    }

    missing_packages = []

    for pkg, success_msg in packages.items():
        try:
            version = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - {success_msg}")
        except importlib.metadata.PackageNotFoundError:
            missing_packages.append(pkg)

    if missing_packages:
        print("\n[ERROR] Missing dependencies detected!")
        print("The following packages are not installed:",
              ", ".join(missing_packages))
        print("\nWelcome to the Real World of Data Engineering")
        print("To install using pip, run:")
        print("  pip install -r requirements.txt")
        print("\nTo install using Poetry, run:")
        print("  poetry install")
        print("  poetry run python loading.py")
        return False
    return True


def analyze_matrix_data() -> None:
    """Simulates Data analysis using pandas, numpy, and matplotlib."""
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    np.random.seed(42)
    time_series = range(1000)
    anomaly_scores = np.random.randn(1000).cumsum()

    df = pd.DataFrame({
        'time': time_series,
        'anomaly': anomaly_scores
    })

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['anomaly'], color='green', linewidth=1.5)
    plt.title('Matrix Network Anomaly Detection')
    plt.xlabel('Time Sequence')
    plt.ylabel('Anomaly Signature')
    plt.grid(True, linestyle='--', alpha=0.7)
    filename = 'matrix_analysis.png'
    plt.savefig(filename)
    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


def main() -> None:
    """Main execution orchestrator."""
    if check_dependencies():
        analyze_matrix_data()


if __name__ == "__main__":
    main()
