<p align="center"><img src="/docs/images/logo-512x512.png" width="128" alt="Gridmind logo"></p>
# Gridmind

_Charge wisely. Sell at the right time._

## Table of Contents

1. [Overview](#overview)
2. [Getting appId and appSecret](#getting-appid-and-appsecret)
3. [Run locally with Docker](#run-locally-with-docker)
   - [Prerequisites](#0-prerequisites)
   - [Run docker container](#1-run-docker-container)
   - [Access the application](#2-access-the-application)
4. [Use-case Diagram](#use-case-diagram)
5. [Entity Relationship Diagram](#entity-relationship-diagram)

## Overview

An AI platform for the autonomous management of battery systems 
in Ukraine’s day-ahead market.

We're working with the official [Deye API](https://developer.deyecloud.com/api).

> ⚠️ **Supported Device Type:** 3Phase & 1Phase Hybrid inverter; Micro Storage System(no voltage setting)

## Getting appId and appSecret

1. Go to [DeyeCloud](https://developer.deyecloud.com/);
2. Navigate to [Application](https://developer.deyecloud.com/app);
3. Log in with your credentials to a Deye account;
4. Create a new application;
5. Copy the appId and appSecret;
6. Paste them into your settings;

## Run locally with Docker

### 0. Prerequisites

- Docker and Docker Compose are installed on your system.
- You have a Deye account.
- A properly configured environment file `.env` according
to file `.env.template` inside `backend/` directory.

### 1. Run docker container

You can run the application with docker-compose: 

```shell
docker compose -f docker-compose.dev.yml up -d
```

### 2. Access the application

Once the application build was completed, you can access the application at [`http://localhost:5173`](http://localhost:5173).
The Swagger documentation is available at [`http://localhost:8000/docs`](http://localhost:8000/docs).


## Use-case diagram

![usecase-diagram](/docs/images/usecase-diagram.png)

## Entity Relationship Diagram

![entity-relationship-diagram](/docs/images/entity-relation-diagram.png)




