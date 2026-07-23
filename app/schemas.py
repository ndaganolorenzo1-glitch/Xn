"""Pydantic schemas for request/response validation"""

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


# Account Schemas
class AccountBase(BaseModel):
    username: str
    display_name: Optional[str] = None


class AccountCreate(BaseModel):
    username: str
    password: str


class AccountUpdate(BaseModel):
    display_name: Optional[str] = None


class AccountResponse(AccountBase):
    id: int
    user_id: str
    follower_count: int
    following_count: int
    post_count: int
    engagement_rate: float
    is_verified: bool
    is_private: bool
    last_sync: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Follower Schemas
class FollowerResponse(BaseModel):
    id: int
    follower_user_id: str
    follower_username: str
    follower_name: Optional[str] = None
    follower_count: int
    is_following_back: bool
    engagement_score: float
    last_interaction: Optional[datetime] = None
    followed_at: datetime
    unfollowed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Post Schemas
class PostResponse(BaseModel):
    id: int
    post_id: str
    caption: Optional[str] = None
    media_type: str
    likes_count: int
    comments_count: int
    engagement_rate: float
    posted_at: datetime

    class Config:
        from_attributes = True


# Analytics Schemas
class AnalyticsResponse(BaseModel):
    id: int
    date: datetime
    follower_count: int
    following_count: int
    new_followers: int
    lost_followers: int
    follows_made: int
    unfollows_made: int
    total_engagements: int
    avg_engagement_rate: float

    class Config:
        from_attributes = True


class AccountOverviewResponse(BaseModel):
    account: AccountResponse
    todays_analytics: AnalyticsResponse
    follower_growth: int
    engagement_trend: float
    top_post: Optional[PostResponse] = None


# Targeting Schemas
class FollowingRequest(BaseModel):
    account_id: int
    hashtags: List[str] = Field(default_factory=list)
    limit: int = Field(default=50, le=500)
    min_followers: int = Field(default=100)
    max_followers: int = Field(default=100000)
    exclude_follower_of: Optional[List[str]] = None


class UnfollowRequest(BaseModel):
    account_id: int
    days_inactive: int = Field(default=7, ge=1)
    min_follow_duration: int = Field(default=3, ge=1)  # days
    limit: int = Field(default=50, le=500)


class TargetingStatusResponse(BaseModel):
    account_id: int
    is_running: bool
    queue_size: int
    last_action: Optional[datetime] = None
    actions_today: int
    status: str  # IDLE, RUNNING, PAUSED, ERROR


# Health Schemas
class HealthResponse(BaseModel):
    status: str
    database: str
    redis: str
    timestamp: datetime


# Error Schemas
class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    timestamp: datetime
