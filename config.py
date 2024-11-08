# config.py
import os
from pathlib import Path
from typing import Any, Dict, Optional, List
from dotenv import load_dotenv
import logging
from datetime import datetime

class ConfigurationError(Exception):
    """Custom exception for configuration-related errors"""
    pass

class Configuration:
    """Enhanced configuration management with validation and error handling"""
    
    def __init__(self, env_path: Optional[str] = None, required_vars: Optional[List[str]] = None):
        """
        Initialize configuration manager
        
        Args:
            env_path: Optional path to .env file. Defaults to '.env' in current directory
            required_vars: List of required environment variables
        """
        # Setup logging
        self.setup_logging()
        
        # Default required variables if none provided
        self.required_vars = required_vars or [
            'account_sid',
            'auth_token',
            'twilio_from',
            'my_phone',
            'APPID',
            'ALPHA_ADVANTAGE_API_KEY',
            'NEWS_API_KEY',
            'PIXELA_USERNAME',
            'TOKEN',
            'GRAPH_ID',
            'NutritionIX_API_Key',
            'NutritionIX_APP_ID',
            'SHEETY_API_URL',
            'SHEETY_API_TOKEN',
            'SHEETY_FLIGHT_SHEET_ID',
            'SHEETY_FLIGHT_API_TOKEN',
            'AMADEUS_CLIENT_ID',
            'AMADEUS_CLIENT_SECRET'
        ]
        
        # Load configuration
        self.config: Dict[str, Any] = {}
        self.load_configuration(env_path)
        
    def setup_logging(self) -> None:
        """Configure logging for the configuration management"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(f'config_{datetime.now().strftime("%Y%m%d")}.log')
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_configuration(self, env_path: Optional[str] = None) -> None:
        """
        Load and validate configuration from environment variables
        
        Args:
            env_path: Optional path to .env file
        
        Raises:
            ConfigurationError: If configuration loading fails or validation fails
        """
        try:
            # Determine .env file path
            if env_path:
                env_file = Path(env_path)
            else:
                env_file = Path('.') / '.env'
            
            # Check if .env file exists
            if not env_file.exists():
                raise ConfigurationError(
                    f".env file not found at: {env_file.absolute()}\n"
                    "Please create a .env file with required variables"
                )
            
            # Load .env file
            self.logger.info(f"Loading configuration from: {env_file.absolute()}")
            if not load_dotenv(dotenv_path=env_file):
                raise ConfigurationError("Failed to load .env file")
            
            # Load all required variables
            for var in self.required_vars:
                value = os.getenv(var)
                if value is None:
                    raise ConfigurationError(f"Missing required environment variable: {var}")
                self.config[var] = value
                
            # Validate configuration
            self.validate_configuration()
            
            self.logger.info("Configuration loaded successfully")
            
        except Exception as e:
            self.logger.error(f"Configuration error: {str(e)}")
            raise ConfigurationError(f"Failed to load configuration: {str(e)}")

    def validate_configuration(self) -> None:
        """
        Validate the loaded configuration values
        
        Raises:
            ConfigurationError: If validation fails
        """
        try:
            # Validate Twilio credentials format
            if not self.config['account_sid'].startswith('AC'):
                raise ConfigurationError("Invalid account_sid format - should start with 'AC'")
            
            # Validate phone number format (basic check)
            for phone_var in ['twilio_from', 'my_phone']:
                if not self.config[phone_var].startswith('+'):
                    raise ConfigurationError(f"Invalid {phone_var} format - should start with '+'")
            
            # Validate minimum length requirements
            min_lengths = {
                'auth_token': 32,
                'account_sid': 34,
                'APPID': 8
            }
            
            for var, min_length in min_lengths.items():
                if len(self.config[var]) < min_length:
                    raise ConfigurationError(
                        f"{var} appears to be invalid - "
                        f"length should be at least {min_length} characters"
                    )
                    
        except KeyError as e:
            raise ConfigurationError(f"Missing configuration key: {str(e)}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Safely get a configuration value
        
        Args:
            key: Configuration key to retrieve
            default: Default value if key doesn't exist
        
        Returns:
            Configuration value or default
        """
        return self.config.get(key, default)
    
    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-style access to configuration"""
        try:
            return self.config[key]
        except KeyError:
            raise ConfigurationError(f"Configuration key not found: {key}")
    
    def debug_info(self) -> Dict[str, Any]:
        """
        Get debug information about the configuration
        
        Returns:
            Dictionary with debug information
        """
        return {
            'loaded_vars': list(self.config.keys()),
            'required_vars': self.required_vars,
            'missing_vars': [var for var in self.required_vars if var not in self.config],
            'extra_vars': [var for var in self.config if var not in self.required_vars]
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize configuration
        config = Configuration()
        
        # Example of accessing values
        print(f"Using Twilio number: {config['twilio_from']}")
        
        # Example of debug info
        debug_info = config.debug_info()
        print("\nConfiguration Debug Info:")
        for key, value in debug_info.items():
            print(f"{key}: {value}")
            
    except ConfigurationError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")