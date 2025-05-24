#!/bin/bash
docker build -f docker/Dockerfile.train -t image-classifier-train .
docker run --rm -v $(pwd)/output:/app/output image-classifier-train
