#!/usr/bin/env python
"""Initialize database with tables"""

import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

try:
    from app.database import init_db, engine
    from app.models import Base  # noqa: F401 - Import all models

    logger.info("Initializing database...")
    init_db()
    logger.info("✓ Database initialized successfully!")
    logger.info(f"Database URL: {engine.url}")
    sys.exit(0)

except Exception as e:
    logger.error(f"✗ Error initializing database: {str(e)}")
    sys.exit(1)
