# Load necessary libraries
library(dplyr)
library(caret)

# Import Netflix streaming data as a data frame
data <- read.csv("netflix_data.csv")

# Preprocess the data (if necessary)
# ...

# Split the data into training and test sets
set.seed(123)
train_ind <- createDataPartition(data$viewing_history, p = 0.75, list = FALSE)
train <- data[train_ind, ]
test <- data[-train_ind, ]

# Build the predictive model using a machine learning algorithm
model <- train(viewing_history ~ ., data = train, method = "knn")

# Test the model on the test set
predictions <- predict(model, test)

# Export the model to a file
saveRDS(model, file = "netflix_recommender.rds")
