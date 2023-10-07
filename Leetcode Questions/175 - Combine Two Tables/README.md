# SQL Challenge: Join Person and Address Tables

## Introduction

In this challenge, you'll be working with two tables: `Person` and `Address`.

## Tables Structure

### Person Table

| Column Name | Type    |
|-------------|---------|
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |

**Note**: `personId` is the primary key for this table.

The `Person` table contains information about the ID of some persons and their first and last names.

### Address Table

| Column Name | Type    |
|-------------|---------|
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |

**Note**: `addressId` is the primary key for this table.

Each row of the `Address` table contains information about the city and state of one person with ID = `PersonId`.

## Problem Statement

Write a SQL query to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.

Return the result table in any order.

## Example

### Input

**Person table**:

| personId | lastName | firstName |
|----------|----------|-----------|
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |

**Address table**:

| addressId | personId | city          | state      |
|-----------|----------|---------------|------------|
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |

### Output

| firstName | lastName | city          | state    |
|-----------|----------|---------------|----------|
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |

### Explanation

There is no address in the `Address` table for the `personId = 1` so we return `null` in their city and state.
`addressId = 1` contains information about the address of `personId = 2`.
