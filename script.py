import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data into a DataFrame
file_path = "D:\\phishing.csv"
dataset = pd.read_csv(file_path)

# Display the first few rows of the dataset and check information
print(dataset.head())
print(dataset.info())

# Select relevant features
selected_features = ["Index", "UsingIP", "LongURL",	"ShortURL", "Symbol@", "Redirecting//",
                     "PrefixSuffix-", "SubDomains", "HTTPS", "DomainRegLen", "Favicon",
                     "NonStdPort", "HTTPSDomainURL", "RequestURL",	"AnchorURL",
                     "LinksInScriptTags", "ServerFormHandler",	"InfoEmail", "AbnormalURL",
                     "WebsiteForwarding", "StatusBarCust", "DisableRightClick",	"UsingPopupWindow",
                     "IframeRedirection", "AgeofDomain", "DNSRecording", "WebsiteTraffic",
                     "PageRank",	"GoogleIndex",	"LinksPointingToPage",	"StatsReport", "class"]

new_dataset = dataset[selected_features]

# Split the data into features (X) and target variable (y)
X = new_dataset.drop("CLASS_LABEL", axis=1)
y = new_dataset["CLASS_LABEL"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
