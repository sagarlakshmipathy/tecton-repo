This repository contains a collection of code and resources that can be used to build and deploy feature engineering pipelines using Tecton.

### Getting Started
To get started with this repository, you will need to have a Tecton account and have the Tecton CLI installed on your local machine. If you do not have a Tecton account, you can sign up for a free trial on the Tecton website.

Repository Structure
This repository is organized into several directories, each of which contains code and resources for a specific aspect of feature engineering with Tecton. Here is a brief overview of each directory:

```
.
├── README.md
└── fraud
    ├── data_sources
    │   ├── fraud_users.py
    │   └── transactions.py
    ├── entities.py
    ├── feature_services
    │   ├── orders_from_big_cities_feature_service.py
    │   └── transaction_hemisphere_feature_service.py
    ├── features
    │   ├── batch_feature_views
    │   │   └── percentage_of_orders_from_big_cities.py
    │   └── on_demand_feature_views
    │       └── transaction_latitudinal_hemisphere.py
    └── tests
        └── merchant_is_north.py

```

data_sources: This directory contains code and resources for defining data sources in Tecton. Data sources are the raw data inputs that are used to generate feature views.

entities.py: In Tecton, entities are the core building blocks of feature engineering pipelines. They represent the business objects or concepts that you want to generate features for, and are used to define the inputs and outputs of your feature views.

feature_services: This directory contains code and resources for deploying feature services in Tecton. Feature services are REST APIs that expose feature views to downstream applications.

batch_feature_views: This directory contains code and resources for building batch feature views in Tecton. Batch feature views are precomputed features that are generated on a regular schedule (e.g., daily, hourly) for use in downstream applications.

on_demand_feature_views: This directory contains code and resources for building on-demand feature views in Tecton. On-demand feature views are computed on-the-fly in response to user requests and are typically used in real-time applications.

tests: This directory contains the essential unit tests run before deploying the feature views.

Usage
To use this repository, you can start by exploring the code and resources in each directory. 

To deploy a feature engineering pipeline using Tecton, you will typically need to follow these steps:

1. Define your data sources in the data_source directory.
2. Define your batch and on-demand feature views in the batch_feature_views and on_demand_feature_views directories, respectively.
3. Deploy your feature views using the Tecton CLI.
4. Define your feature services in the feature_services directory.
5. Deploy your feature services using the Tecton CLI.
6. For more detailed instructions on how to use Tecton, please refer to the Tecton documentation.
