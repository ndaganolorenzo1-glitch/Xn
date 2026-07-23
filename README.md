# Instagram Growth AI

An intelligent AI-powered system that helps grow your Instagram account by tracking audience metrics, intelligently following/unfollowing users, and optimizing content reach.

## Features

- 📊 **Audience Analytics**: Track follower growth, engagement rates, and audience demographics
- 🤖 **Smart Following**: AI-driven targeting to follow users in your niche
- 📈 **Content Optimization**: Analyze top-performing posts and recommend posting times
- 🎯 **Targeted Outreach**: Reach your followers with personalized content recommendations
- 💾 **Database Tracking**: Store audience data and interaction history
- 📱 **Multi-Account Support**: Manage multiple Instagram accounts
- 🔔 **Real-time Monitoring**: Track unfollowers and new followers in real-time

## Tech Stack

- **Backend**: Python 3.11 + FastAPI
- **Database**: PostgreSQL + SQLAlchemy ORM
- **Instagram Integration**: Instagrapi (Instagram Private API)
- **ML/Analytics**: Scikit-learn, Pandas, NumPy
- **Task Queue**: Celery + Redis
- **Frontend**: React + TypeScript (optional dashboard)
- **Deployment**: Docker + Docker Compose

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ndaganolorenzo1-glitch/Xn.git
   cd Xn
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Instagram credentials and database URL
   ```

5. **Initialize the database**
   ```bash
   python scripts/init_db.py
   ```

6. **Start the services**

   Option A: Using Docker Compose
   ```bash
   docker-compose up
   ```

   Option B: Manual startup
   ```bash
   # Terminal 1: Start Redis
   redis-server

   # Terminal 2: Start Celery worker
   celery -A app.tasks worker --loglevel=info

   # Terminal 3: Start FastAPI server
   uvicorn app.main:app --reload
   ```

7. **Access the API**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Structure

```
Xn/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py               # Configuration settings
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   ├── database.py             # Database connection
│   ├── tasks.py                # Celery tasks
│   ├── api/
│   │   ├── __init__.py
│   │   ├── accounts.py         # Account management endpoints
│   │   ├── analytics.py        # Analytics endpoints
│   │   ├── targeting.py        # Following/unfollowing endpoints
│   │   ├── content.py          # Content optimization endpoints
│   │   └── auth.py             # Authentication endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── instagram_client.py # Instagram API wrapper
│   │   ├── analytics_engine.py # Analytics & metrics
│   │   ├── targeting_engine.py # Smart following logic
│   │   ├── content_optimizer.py# Content recommendations
│   │   └── outreach_engine.py  # Audience outreach
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py          # Utility functions
│       └── constants.py        # Constants
├── tests/
│   ├── __init__.py
│   ├── test_analytics.py
│   ├── test_targeting.py
│   └── test_content.py
├── scripts/
│   ├── init_db.py              # Database initialization
│   ├── seed_data.py            # Seed test data
│   └── cleanup.py              # Cleanup tasks
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Docker image definition
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## API Endpoints

### Accounts
- `POST /api/accounts/add` - Add Instagram account
- `GET /api/accounts` - List connected accounts
- `DELETE /api/accounts/{account_id}` - Remove account

### Analytics
- `GET /api/analytics/{account_id}/overview` - Get account overview
- `GET /api/analytics/{account_id}/followers` - Follower analytics
- `GET /api/analytics/{account_id}/engagement` - Engagement metrics
- `GET /api/analytics/{account_id}/top-posts` - Top performing posts

### Targeting
- `POST /api/targeting/follow` - Start following targeting
- `POST /api/targeting/unfollow` - Auto-unfollow inactive followers
- `GET /api/targeting/queue` - View follow queue
- `POST /api/targeting/pause` - Pause operations

### Content
- `GET /api/content/recommendations` - Get posting recommendations
- `GET /api/content/best-times` - Optimal posting times
- `POST /api/content/analyze` - Analyze post performance

## Configuration

Edit `.env` file to configure:

```env
# Instagram
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password

# Database
DATABASE_URL=postgresql://user:password@localhost/instagram_growth

# Redis
REDIS_URL=redis://localhost:6379

# API
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Targeting
FOLLOW_RATE=50  # Follows per day
UNFOLLOW_RATE=50  # Unfollows per day
MIN_FOLLOWER_COUNT=100
MAX_FOLLOWER_COUNT=100000
```

## Usage Examples

### Add Instagram Account
```python
curl -X POST "http://localhost:8000/api/accounts/add" \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}'
```

### Get Analytics
```python
curl -X GET "http://localhost:8000/api/analytics/1/overview"
```

### Start Targeting
```python
curl -X POST "http://localhost:8000/api/targeting/follow" \
  -H "Content-Type: application/json" \
  -d '{"account_id":1,"hashtags":["python","coding"],"limit":50}'
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Notes

- **Never commit credentials** - Use `.env` files
- **Rate limiting** - Instagram has strict rate limits; built-in delays prevent bans
- **Account safety** - Use at your own risk; Instagram may flag unusual activity
- **Data privacy** - Store all data securely and comply with Instagram ToS

## Troubleshooting

### Connection Refused
- Ensure PostgreSQL and Redis are running
- Check connection strings in `.env`

### Instagram Login Failed
- Verify credentials are correct
- Check if 2FA is enabled (may need app-specific password)
- Instagram may temporarily block automated access

### Celery Tasks Not Running
- Ensure Redis is running
- Check Celery worker logs
- Verify task queue is not full

## License

MIT License - see LICENSE file for details

## Disclaimer

This project is for educational purposes. Using automation on Instagram may violate their Terms of Service. Use responsibly and at your own risk.

## Support

For issues and questions, please open an GitHub issue.
