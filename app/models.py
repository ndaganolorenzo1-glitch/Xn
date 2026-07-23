"""SQLAlchemy models for database schema"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database import Base


class Account(Base):
    """Instagram account model"""
    __tablename__ = "accounts"

    id = Integer(primary_key=True, index=True)
    username = String(255, unique=True, index=True)
    user_id = String(255, unique=True, index=True)
    encrypted_password = Text()
    display_name = String(255)
    bio = Text(nullable=True)
    profile_pic_url = Text(nullable=True)
    follower_count = Integer(default=0)
    following_count = Integer(default=0)
    post_count = Integer(default=0)
    is_verified = Boolean(default=False)
    is_private = Boolean(default=False)
    engagement_rate = Float(default=0.0)
    last_sync = DateTime(nullable=True)
    created_at = DateTime(default=datetime.utcnow, index=True)
    updated_at = DateTime(default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    followers = relationship("Follower", back_populates="account", cascade="all, delete-orphan")
    posts = relationship("Post", back_populates="account", cascade="all, delete-orphan")
    targeting_history = relationship("TargetingHistory", back_populates="account", cascade="all, delete-orphan")
    analytics = relationship("Analytics", back_populates="account", cascade="all, delete-orphan")


class Follower(Base):
    """Follower tracking model"""
    __tablename__ = "followers"

    id = Integer(primary_key=True, index=True)
    account_id = Integer(ForeignKey("accounts.id"), index=True)
    follower_user_id = String(255, index=True)
    follower_username = String(255, index=True)
    follower_name = String(255, nullable=True)
    follower_count = Integer(default=0)
    is_following_back = Boolean(default=False)
    engagement_score = Float(default=0.0)
    last_interaction = DateTime(nullable=True)
    is_active = Boolean(default=True)
    followed_at = DateTime(index=True)
    unfollowed_at = DateTime(nullable=True)
    created_at = DateTime(default=datetime.utcnow, index=True)
    updated_at = DateTime(default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    account = relationship("Account", back_populates="followers")

    __table_args__ = (
        UniqueConstraint('account_id', 'follower_user_id', name='uq_account_follower'),
        Index('idx_account_active', 'account_id', 'is_active'),
    )


class Post(Base):
    """Instagram post model"""
    __tablename__ = "posts"

    id = Integer(primary_key=True, index=True)
    account_id = Integer(ForeignKey("accounts.id"), index=True)
    post_id = String(255, unique=True, index=True)
    caption = Text(nullable=True)
    media_type = String(50)  # CAROUSEL, IMAGE, VIDEO, etc.
    likes_count = Integer(default=0)
    comments_count = Integer(default=0)
    shares_count = Integer(default=0)
    saves_count = Integer(default=0)
    engagement_rate = Float(default=0.0)
    hashtags = Text(nullable=True)  # JSON or comma-separated
    posted_at = DateTime()
    created_at = DateTime(default=datetime.utcnow, index=True)
    updated_at = DateTime(default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    account = relationship("Account", back_populates="posts")

    __table_args__ = (
        Index('idx_account_posted', 'account_id', 'posted_at'),
    )


class TargetingHistory(Base):
    """Targeting action history model"""
    __tablename__ = "targeting_history"

    id = Integer(primary_key=True, index=True)
    account_id = Integer(ForeignKey("accounts.id"), index=True)
    action_type = String(50)  # FOLLOW, UNFOLLOW, LIKE, COMMENT, DM
    target_user_id = String(255)
    target_username = String(255)
    success = Boolean(default=True)
    reason = String(500, nullable=True)
    created_at = DateTime(default=datetime.utcnow, index=True)

    # Relationships
    account = relationship("Account", back_populates="targeting_history")

    __table_args__ = (
        Index('idx_account_action_date', 'account_id', 'action_type', 'created_at'),
    )


class Analytics(Base):
    """Daily analytics snapshot model"""
    __tablename__ = "analytics"

    id = Integer(primary_key=True, index=True)
    account_id = Integer(ForeignKey("accounts.id"), index=True)
    date = DateTime(index=True)
    follower_count = Integer()
    following_count = Integer()
    new_followers = Integer(default=0)
    lost_followers = Integer(default=0)
    follows_made = Integer(default=0)
    unfollows_made = Integer(default=0)
    total_engagements = Integer(default=0)
    avg_engagement_rate = Float(default=0.0)
    created_at = DateTime(default=datetime.utcnow)

    # Relationships
    account = relationship("Account", back_populates="analytics")

    __table_args__ = (
        UniqueConstraint('account_id', 'date', name='uq_account_date'),
        Index('idx_account_date', 'account_id', 'date'),
    )
