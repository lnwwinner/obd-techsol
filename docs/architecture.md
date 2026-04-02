# 🧠 System Architecture

## Overview
ระบบ OBD TechSol ถูกออกแบบให้เป็น AI Fleet Intelligence Platform

## Flow
Vehicle → OBD Device → Internet (SIM) → API Server → Database → AI Engine → Dashboard

## Components

### 1. Device Layer
- OBD Tracker
- GPS / Speed / DTC

### 2. Backend Layer
- FastAPI
- Data ingestion
- Alert processing

### 3. Data Layer
- SQLite (MVP)
- PostgreSQL (future)

### 4. Intelligence Layer
- Rule-based alert
- Future: AI / Data Twin

### 5. Presentation Layer
- Dashboard (future)

## Key Principle
- Simple first
- Scalable later
