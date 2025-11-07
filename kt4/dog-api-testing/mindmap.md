# Mindmap for Dog CEO API

## Overview
- **API Base URL**: https://dog.ceo/api/
- **Purpose**: Provides dog breed information and images
- **Response Format**: JSON
- **Authentication**: None required

## Main Endpoints

### 1. List All Breeds
- **Endpoint**: `/breeds/list/all`
- **Method**: GET
- **Description**: Returns a JSON object with all breeds and sub-breeds
- **Response Structure**:
  - `message`: Object with breed names as keys, sub-breeds as arrays
  - `status`: "success"

### 2. Random Image
- **Endpoint**: `/breeds/image/random`
- **Method**: GET
- **Description**: Returns a random dog image
- **Response Structure**:
  - `message`: URL string of the image
  - `status`: "success"

### 3. Images by Breed
- **Endpoint**: `/breed/{breed}/images`
- **Method**: GET
- **Description**: Returns all images for a specific breed
- **Response Structure**:
  - `message`: Array of image URLs
  - `status`: "success"

### 4. Random Image by Breed
- **Endpoint**: `/breed/{breed}/images/random`
- **Method**: GET
- **Description**: Returns a random image for a specific breed
- **Response Structure**:
  - `message`: URL string of the image
  - `status`: "success"

### 5. Sub-breeds
- **Endpoint**: `/breed/{breed}/list`
- **Method**: GET
- **Description**: Returns sub-breeds for a specific breed
- **Response Structure**:
  - `message`: Array of sub-breed names
  - `status`: "success"

### 6. Random Image by Sub-breed
- **Endpoint**: `/breed/{breed}/{sub-breed}/images/random`
- **Method**: GET
- **Description**: Returns a random image for a specific sub-breed
- **Response Structure**:
  - `message`: URL string of the image
  - `status`: "success"

### 7. Images by Sub-breed
- **Endpoint**: `/breed/{breed}/{sub-breed}/images`
- **Method**: GET
- **Description**: Returns all images for a specific sub-breed
- **Response Structure**:
  - `message`: Array of image URLs
  - `status`: "success"

## Entities
- **Breed**: Main category (e.g., "hound", "retriever")
- **Sub-breed**: Sub-category within a breed (e.g., "afghan" under "hound")
- **Image**: URL to a dog image

## Error Handling
- **Invalid Breed**: Returns `{"status": "error", "message": "Breed not found", "code": 404}`
- **Invalid Sub-breed**: Returns `{"status": "error", "message": "Breed not found", "code": 404}`

## Additional Notes
- All images are hosted on dog.ceo
- API is free to use
- No rate limiting mentioned
- CORS enabled for web use
