"""Application configuration"""

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = False
    encryption_key: str = "your-secret-key-change-in-production"

    # Database Configuration
    database_url: str = "postgresql://user:password@localhost:5432/instagram_growth"
    database_echo: bool = False

    # Redis Configuration
    redis_url: str = "redis://localhost:6379/0"
    redis_socket_timeout: int = 5

    # Instagram Configuration
    instagram_username: str
    instagram_password: str

    # Targeting Configuration
    follow_rate: int = 50  # Follows per day
    unfollow_rate: int = 50  # Unfollows per day
    min_follower_count: int = 100
    max_follower_count: int = 100000
    target_engagement_rate: float = 0.05

    # Content Configuration
    post_analysis_window_days: int = 30
    optimal_posting_times: str = "9,13,18,21"

    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/app.log"

    # Feature Flags
    enable_auto_follow: bool = True
    enable_auto_unfollow: bool = True
    enable_dm_outreach: bool = False
    enable_story_interactions: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = False

    def get_optimal_posting_times(self) -> list[int]:
        """Parse optimal posting times from config"""
        return [int(h) for h in self.optimal_posting_times.split(",")]


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
