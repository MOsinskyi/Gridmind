# Gridmind

_Charge wisely. Sell at the right time._

## Table of Contents

1. [Overview](#overview)
2. [Getting appId and appSecret](#getting-appid-and-appsecret)
3. [Run locally with Docker](#run-locally-with-docker)
   - [Prerequisites](#0-prerequisites)
4. [Usecase](#use-case-diagram)
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


## Use-case diagram

![usecase-diagram](/docs/images/usecase-diagram.png)

## Entity Relationship Diagram

![entity-relationship-diagram](/docs/images/entity-relation-diagram.png)




