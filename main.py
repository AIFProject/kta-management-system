import argparse
import sys

def run_validate():
    from scripts.validation.validate_members import validate_members
    validate_members()

def run_report():
    from scripts.reporting.generate_report import generate_report
    generate_report()

def run_generate_kta():
    from scripts.processing.generate_kta_number import generate_kta_number
    generate_kta_number()

def main():
    parser = argparse.ArgumentParser(
        description="KTA Management System CLI"
    )
    
    parser.add_argument(
        "command",
        choices=["validate", "report", "generate-kta"],
        help="Command to run: validate data, generate report, or generate KTA numbers"
    )
    
    args = parser.parse_args()
    
    if args.command == "validate":
        run_validate()
    elif args.command == "report":
        run_report()
    elif args.command == "generate-kta":
        run_generate_kta()
    else:
        print(f"Unknown command: {args.command}")
        sys.exit(1)

if __name__ == "__main__":
    main()