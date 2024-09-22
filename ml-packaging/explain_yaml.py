import yaml

def explain_yaml(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    print(config['model']['type'])

    
    print("Configuration Overview:")
    print("=========================")
    
    for section, settings in config.items():
        print(f"{section.capitalize()} Settings:")
        for key, value in settings.items():
            print(f"  - {key}: {value}")
        print()  # Add a new line for better readability

    print("Importance of the YAML Configuration File:")
    print("===========================================")
    print("- Centralized configuration for easy management.")
    print("- Flexibility to switch between environments.")
    print("- Human-readable format promotes clarity.")
    print("- Easy adjustments for hyperparameters.")
    print("- Separation of configuration from application logic.")
    print("- Change tracking through version control.")

if __name__ == "__main__":
    explain_yaml("config1.yaml")
