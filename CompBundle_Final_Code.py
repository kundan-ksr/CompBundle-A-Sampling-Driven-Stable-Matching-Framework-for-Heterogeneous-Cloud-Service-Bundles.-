Original file is located at    https://colab.research.google.com/drive/1Z7lob67wEYT_NQSjmfwBW5kiIx-z-L6d?usp=sharing




import pandas as pd
import numpy as np
import random

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

!pip install pandas numpy requests scipy scikit-learn seaborn matplotlib

aws_data = [
# General Purpose (t3)
("AWS","t3.nano",0.5,2,0.0052),
("AWS","t3.micro",1,2,0.0104),
("AWS","t3.small",2,2,0.0208),
("AWS","t3.medium",4,2,0.0416),
("AWS","t3.large",8,2,0.0832),
("AWS","t3.xlarge",16,4,0.1664),
("AWS","t3.2xlarge",32,8,0.3328),

# M5 Series
("AWS","m5.large",8,2,0.096),
("AWS","m5.xlarge",16,4,0.192),
("AWS","m5.2xlarge",32,8,0.384),
("AWS","m5.4xlarge",64,16,0.768),
("AWS","m5.8xlarge",128,32,1.536),

# C5 Series
("AWS","c5.large",4,2,0.085),
("AWS","c5.xlarge",8,4,0.17),
("AWS","c5.2xlarge",16,8,0.34),
("AWS","c5.4xlarge",32,16,0.68),

# R5 Series
("AWS","r5.large",16,2,0.126),
("AWS","r5.xlarge",32,4,0.252),
("AWS","r5.2xlarge",64,8,0.504),
("AWS","r5.4xlarge",128,16,1.008)
]

df_aws = pd.DataFrame(aws_data, columns=[
    "provider","instance_type","memory_gb","vcpu","price_per_hour"
])

print("Total AWS instances:", len(df_aws))
df_aws_sorted = df_aws.sort_values(by=["vcpu"]).reset_index(drop=True)

print("🔹 AWS Full Table (Sorted by vCPU)")
df_aws_sorted

# AZURE DATASET

azure_data = [

# ---- Dps v6 ----
("Azure","D2ps_v6",8,2,0.0792),
("Azure","D4ps_v6",16,4,0.1580),
("Azure","D8ps_v6",32,8,0.3170),
("Azure","D16ps_v6",64,16,0.6340),
("Azure","D32ps_v6",128,32,1.2670),

# ---- Dpds v6 ----
("Azure","D2pds_v6",8,2,0.1040),
("Azure","D4pds_v6",16,4,0.2080),
("Azure","D8pds_v6",32,8,0.4150),
("Azure","D16pds_v6",64,16,0.8300),
("Azure","D32pds_v6",128,32,1.6610),

# ---- Dpls v6 ----
("Azure","D2pls_v6",4,2,0.0702),
("Azure","D4pls_v6",8,4,0.1400),
("Azure","D8pls_v6",16,8,0.2810),
("Azure","D16pls_v6",32,16,0.5620),
("Azure","D32pls_v6",64,32,1.1230),

# ---- Das v7 ----
("Azure","D2as_v7",8,2,0.0908),
("Azure","D4as_v7",16,4,0.1820),
("Azure","D8as_v7",32,8,0.3630),
("Azure","D16as_v7",64,16,0.7260),
("Azure","D32as_v7",128,32,1.4530),

# ---- Dads v7 ----
("Azure","D2ads_v7",8,2,0.1140),
("Azure","D4ads_v7",16,4,0.2280),
("Azure","D8ads_v7",32,8,0.4560),
("Azure","D16ads_v7",64,16,0.9120),
("Azure","D32ads_v7",128,32,1.8240),

# ---- Ds v6 ----
("Azure","D2s_v6",8,2,0.1140),
("Azure","D4s_v6",16,4,0.2280),
("Azure","D8s_v6",32,8,0.4560),
("Azure","D16s_v6",64,16,0.9110),
("Azure","D32s_v6",128,32,1.8220),

]

df_azure = pd.DataFrame(
    azure_data,
    columns=["provider","instance_type","memory_gb","vcpu","price_per_hour"]
)

print("Azure instances:", len(df_azure))
df_azure.sort_values(by=["vcpu"]).reset_index(drop=True)

gcp_data = [
("GCP","e2-micro",1,2,0.008),
("GCP","e2-small",2,2,0.016),
("GCP","e2-medium",4,2,0.033),
("GCP","n1-standard-1",3.75,1,0.0475),
("GCP","n1-standard-2",7.5,2,0.095),
("GCP","n1-standard-4",15,4,0.19),
("GCP","n1-standard-8",30,8,0.38),
("GCP","n1-highmem-2",13,2,0.118),
("GCP","n1-highmem-4",26,4,0.236),
("GCP","n1-highmem-8",52,8,0.472),
("GCP","n1-highcpu-2",1.8,2,0.070),
("GCP","n1-highcpu-4",3.6,4,0.14),
("GCP","n1-highcpu-8",7.2,8,0.28),
("GCP","n2-standard-2",8,2,0.097),
("GCP","n2-standard-4",16,4,0.194)
]

df_gcp = pd.DataFrame(gcp_data, columns=[
    "provider","instance_type","memory_gb","vcpu","price_per_hour"
])
df_gcp_sorted = df_gcp.sort_values(by=["vcpu"]).reset_index(drop=True)

print("🔹 GCP Full Table (Sorted by vCPU)")
df_gcp_sorted

df_real = pd.concat([df_aws, df_azure, df_gcp], ignore_index=True)

from IPython.display import display

display(df_real)

print("AWS:", len(df_aws))
print("Azure:", len(df_azure))
print("GCP:", len(df_gcp))

df_real = pd.concat([df_aws, df_azure, df_gcp], ignore_index=True)

print("Total real VM instances:", len(df_real))

import random
import numpy as np
import pandas as pd

NUM_SERVICES = 200
services = []

max_real_price = df_real["price_per_hour"].max()

provider_reputation = {
    "AWS": 0.90,
    "Azure": 0.88,
    "GCP": 0.87
}

for i in range(NUM_SERVICES):

    row = df_real.sample(1).iloc[0]

    provider = row["provider"]
    instance_type = row["instance_type"]
    vm_memory = row["memory_gb"]
    vcpu = row["vcpu"]

    cost = round(row["price_per_hour"] * random.uniform(0.9, 1.1), 4)

    storage = int(np.random.lognormal(6, 1))

    latency = int(max(np.random.normal(65 - vcpu * 1.5, 12), 10))

    bandwidth = int(max(np.random.normal(vcpu * 550, 200), 100))

    base_trust = provider_reputation[provider]
    cost_factor = min(cost / max_real_price, 1)

    trust_score = round(
        0.6 * base_trust +
        0.3 * cost_factor +
        0.1 * np.random.uniform(0, 1),
        2
    )

    trust_score = min(trust_score, 1.0)

    services.append({
        "service_id": f"S_{i}",
        "provider": provider,
        "instance_type": instance_type,
        "vm_memory": vm_memory,
        "vcpu": vcpu,
        "storage": storage,
        "latency": latency,
        "bandwidth": bandwidth,
        "cost": cost,
        "trust_score": trust_score
    })

df_services = pd.DataFrame(services)

print("Total Services Generated:", len(df_services))
df_services.head()

# TRUST SCORE SUMMARY

print("\n TRUST SCORE SUMMARY")

min_trust = df_services["trust_score"].min()
max_trust = df_services["trust_score"].max()
avg_trust = df_services["trust_score"].mean()

print(f"Minimum Trust Score  : {round(min_trust, 3)}")
print(f"Maximum Trust Score  : {round(max_trust, 3)}")
print(f"Average Trust Score  : {round(avg_trust, 3)}")

print("\n Explanation:")
print("Trust score is influenced by provider reputation and cost tier.")
print("Higher-cost and premium-provider services tend to have higher trust.")
print("Small random variation is added to simulate real-world SLA uncertainty.")


# TRUST SCORE EXAMPLE COMPARISON

print("\n Example Comparison Between Two Services:")

# Sort services by cost
sorted_services = df_services.sort_values("cost")

# Take one lower-cost and one higher-cost example
low_cost_service = sorted_services.iloc[0]
high_cost_service = sorted_services.iloc[-1]

print("\nLower-Cost Service Example:")
print(f"Service ID      : {low_cost_service['service_id']}")
print(f"Provider        : {low_cost_service['provider']}")
print(f"Cost            : {low_cost_service['cost']}")
print(f"Trust Score     : {low_cost_service['trust_score']}")

print("\nHigher-Cost Service Example:")
print(f"Service ID      : {high_cost_service['service_id']}")
print(f"Provider        : {high_cost_service['provider']}")
print(f"Cost            : {high_cost_service['cost']}")
print(f"Trust Score     : {high_cost_service['trust_score']}")

print("\n Observation:")
if high_cost_service["trust_score"] >= low_cost_service["trust_score"]:
    print("The higher-cost service shows equal or higher trust, reflecting SLA-based modeling.")
else:
    print("Trust remains realistic with slight variation due to modeled uncertainty.")

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

sns.kdeplot(df_real["price_per_hour"], label="Real Cloud Pricing")
sns.kdeplot(df_services["cost"], label="Calibrated Synthetic Pricing")

plt.legend()
plt.title("Real vs Synthetic Pricing Distribution")
plt.show()

from scipy.stats import ks_2samp

real_prices = df_real["price_per_hour"]
synthetic_prices = df_services["cost"]

ks_stat, p_value = ks_2samp(real_prices, synthetic_prices)

print("KS Statistic:", ks_stat)
print("P-value:", p_value)

if p_value > 0.05:
    print("Synthetic pricing distribution is statistically similar to real pricing.")
else:
    print("Synthetic distribution differs significantly from real pricing.")

import numpy as np
import random

NUM_CLIENTS = 100

def assign_tier(budget):
    if budget >= 4: return "Platinum"
    elif budget >= 3: return "Gold"
    elif budget >= 2: return "Silver"
    elif budget >= 1: return "Bronze"
    else: return "Iron"

clients = []

for i in range(NUM_CLIENTS):
    budget = round(np.random.lognormal(0.5,0.7),2)

    clients.append({
        "client_id": f"C_{i}",
        "vm_memory_req": random.choice([1,2,4,8,16,32,64]),
        "total_storage_req": int(np.random.lognormal(6,1)),

        # Removed (unrealistic bandwidth)
        "max_latency_req": random.choice([80, 120, 150, 200]),
        "min_bandwidth_req": random.choice([50,200,500,1000]),

        "total_budget": budget,
        "economic_tier": assign_tier(budget),

        "min_trust_required": round(np.random.uniform(0.6, 0.85),2)
    })

df_clients = pd.DataFrame(clients)
df_clients.head()

client_prefs = {}

for _, client in df_clients.iterrows():
    valid_services = df_services[
        (df_services["vm_memory"] >= client["vm_memory_req"]) &
        (df_services["cost"] <= client["total_budget"]) &
        (df_services["latency"] <= client["max_latency_req"]) &
        (df_services["bandwidth"] >= client["min_bandwidth_req"]) &
        (df_services["trust_score"] >= client["min_trust_required"])
    ].copy()

    ranked = valid_services.sort_values("cost")

    client_prefs[client["client_id"]] = list(ranked["service_id"])

service_prefs = {}

for _, service in df_services.iterrows():

    interested_clients = []

    for _, client in df_clients.iterrows():
        if service["vm_memory"] >= client["vm_memory_req"]:
            interested_clients.append((client["client_id"], client["total_budget"]))

    ranked_clients = sorted(interested_clients, key=lambda x: x[1], reverse=True)

    service_prefs[service["service_id"]] = [c[0] for c in ranked_clients]
    # so is this way of generating service preference list correct ? shouldn't generation of preference list be dependent upon cost only

# GALE-SHAPLEY STABLE MATCHING

free_clients = list(client_prefs.keys())
engaged = {}  # service_id -> client_id
client_next_proposal = {c: 0 for c in client_prefs}

iteration_count = 0
proposal_count = 0

while free_clients:
    iteration_count += 1

    client = free_clients.pop(0)
    prefs = client_prefs[client]

    if client_next_proposal[client] >= len(prefs):
        continue

    service = prefs[client_next_proposal[client]]
    client_next_proposal[client] += 1
    proposal_count += 1

    if service not in engaged:
        engaged[service] = client
    else:
        current_client = engaged[service]
        service_pref_list = service_prefs[service]

        if service_pref_list.index(client) < service_pref_list.index(current_client):
            engaged[service] = client
            free_clients.append(current_client)
        else:
            free_clients.append(client)

print(" Stable Matching Completed")
print("Total Iterations:", iteration_count)
print("Total Proposals Made:", proposal_count)
print("Total Stable Matches:", len(engaged))

# CONVERT ENGAGEMENTS TO MATCH REPORT

matches = []

for service, client in engaged.items():

    service_row = df_services[df_services["service_id"] == service].iloc[0]
    client_row = df_clients[df_clients["client_id"] == client].iloc[0]

    matches.append({
        "client_id": client,
        "vm_memory_required": client_row["vm_memory_req"],
        "total_budget": client_row["total_budget"],
        "latency_required": client_row["max_latency_req"],
        "bandwidth_required": client_row["min_bandwidth_req"],
        "min_trust_required": client_row["min_trust_required"],
        "economic_tier": client_row["economic_tier"],

        "service_id": service,
        "provider": service_row["provider"],
        "vm_memory": service_row["vm_memory"],
        "bundle_cost": service_row["cost"],
        "latency": service_row["latency"],
        "bandwidth": service_row["bandwidth"],
        "trust_score": service_row["trust_score"]
    })

df_matches = pd.DataFrame(matches)

print("\n FULL STABLE MATCHING OUTPUT:")
display(df_matches)

print("\nTotal Stable Matches:", len(df_matches))

# PROFIT ANALYSIS SECTION

# Calculate Operational Cost (Assume 70%)
df_matches["operational_cost"] = df_matches["bundle_cost"] * 0.7

# Calculate Profit Per Match
df_matches["profit"] = df_matches["bundle_cost"] - df_matches["operational_cost"]

# Total Platform Profit
total_profit = df_matches["profit"].sum()

# Profit Per Provider
profit_per_provider = df_matches.groupby("provider")["profit"].sum()

# Profit Per Economic Tier
profit_by_tier = df_matches.groupby("economic_tier")["profit"].sum()

# Average Profit Per Match
avg_profit = df_matches["profit"].mean()

# PRINT RESULTS CLEANLY

print(" Total Platform Profit:", round(total_profit,4))
print("\n Average Profit per Match:", round(avg_profit,4))

print("\n Profit per Provider:")
print(profit_per_provider)

print("\n Profit by Economic Tier:")
print(profit_by_tier)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.barplot(x=profit_per_provider.index, y=profit_per_provider.values)
plt.title("Profit Distribution per Provider")
plt.ylabel("Total Profit")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.histplot(df_matches["trust_score"], kde=True)
plt.title("Distribution of Trust Scores in Matched Services")
plt.show()

tier_match_counts = df_matches["economic_tier"].value_counts()

plt.figure(figsize=(8,5))
sns.barplot(x=tier_match_counts.index, y=tier_match_counts.values)
plt.title("Matches by Economic Tier")
plt.ylabel("Number of Matches")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x="provider", data=df_matches)
plt.title("Distribution of Providers in Matched Solutions")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df_matches["bundle_cost"], bins=15, kde=True)
plt.title("Distribution of Bundle Costs")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="bundle_cost", y="latency", hue="provider", data=df_matches)
plt.title("Cost vs Latency by Provider")
plt.show()

# BASELINE COMPARISON AND STABILITY EVALUATION

print("\n" + "="*60)
print("STABLE MATCHING EVALUATION AND BASELINE COMPARISON")
print("="*60 + "\n")


# 1️ GREEDY BASELINE

greedy_matches = []
used_services = set()

for _, client in df_clients.iterrows():

    valid_services = df_services[
        (df_services["vm_memory"] >= client["vm_memory_req"]) &
        (df_services["cost"] <= client["total_budget"]) &
        (df_services["latency"] <= client["max_latency_req"]) &
        (df_services["bandwidth"] >= client["min_bandwidth_req"]) &
        (df_services["trust_score"] >= client["min_trust_required"])
    ].copy()



    if valid_services.empty:
        continue

    valid_services = valid_services.sort_values("cost")

    for _, service in valid_services.iterrows():

        if service["service_id"] not in used_services:

            greedy_matches.append({
                "client_id": client["client_id"],
                "service_id": service["service_id"],
                "economic_tier": client["economic_tier"]
            })

            used_services.add(service["service_id"])
            break

df_greedy = pd.DataFrame(greedy_matches)


# 2️ RANDOM BASELINE

random_matches = []
available_services = set(df_services["service_id"])

for _, client in df_clients.iterrows():

    valid_services = df_services[
        (df_services["vm_memory"] >= client["vm_memory_req"]) &
        (df_services["cost"] <= client["total_budget"]) &
        (df_services["latency"] <= client["max_latency_req"]) &
        (df_services["bandwidth"] >= client["min_bandwidth_req"]) &
        (df_services["trust_score"] >= client["min_trust_required"])
    ]

    valid_services = valid_services[
        valid_services["service_id"].isin(available_services)
    ]

    if valid_services.empty:
        continue

    service = valid_services.sample(1).iloc[0]

    random_matches.append({
        "client_id": client["client_id"],
        "service_id": service["service_id"],
        "economic_tier": client["economic_tier"]
    })

    available_services.remove(service["service_id"])

df_random = pd.DataFrame(random_matches)


# METRIC FUNCTIONS

def client_satisfaction(match_df):

    ranks = []

    for client, prefs in client_prefs.items():

        match = match_df[match_df["client_id"] == client]

        if match.empty:
            continue

        service = match.iloc[0]["service_id"]

        if service in prefs:
            ranks.append(prefs.index(service) + 1)

    if len(ranks) == 0:
        return None

    return sum(ranks) / len(ranks)


def provider_satisfaction(match_df):

    ranks = []

    for _, row in match_df.iterrows():

        service = row["service_id"]
        client = row["client_id"]

        prefs = service_prefs.get(service, [])

        if client in prefs:
            ranks.append(prefs.index(client) + 1)

    if len(ranks) == 0:
        return None

    return sum(ranks) / len(ranks)


def blocking_pairs(match_df):

    pairs = 0

    client_to_service = dict(zip(match_df["client_id"], match_df["service_id"]))
    service_to_client = dict(zip(match_df["service_id"], match_df["client_id"]))

    for client, prefs in client_prefs.items():

        if client not in client_to_service:
            continue

        current_service = client_to_service[client]

        if current_service not in prefs:
            continue

        current_rank = prefs.index(current_service)

        preferred_services = prefs[:current_rank]

        for service in preferred_services:

            if service not in service_to_client:
                pairs += 1
                continue

            current_client = service_to_client[service]

            service_pref = service_prefs.get(service, [])

            if client in service_pref and current_client in service_pref:

                if service_pref.index(client) < service_pref.index(current_client):
                    pairs += 1

    return pairs


def tier_match_rate(match_df):

    tier_total = df_clients["economic_tier"].value_counts()
    tier_match = match_df["economic_tier"].value_counts()

    tier_table = pd.DataFrame({
        "Total Clients": tier_total,
        "Matched Clients": tier_match
    }).fillna(0)

    tier_table["Match Rate"] = tier_table["Matched Clients"] / tier_table["Total Clients"]

    return tier_table


# COMPUTE METRICS

results = pd.DataFrame({
    "Metric": [
        "Match Count",
        "Blocking Pairs",
        "Avg Client Satisfaction Rank",
        "Avg Provider Satisfaction Rank"
    ],
    "Stable Matching": [
        len(df_matches),
        blocking_pairs(df_matches),
        client_satisfaction(df_matches),
        provider_satisfaction(df_matches)
    ],
    "Greedy Baseline": [
        len(df_greedy),
        blocking_pairs(df_greedy),
        client_satisfaction(df_greedy),
        provider_satisfaction(df_greedy)
    ],
    "Random Baseline": [
        len(df_random),
        blocking_pairs(df_random),
        client_satisfaction(df_random),
        provider_satisfaction(df_random)
    ]
})


# DISPLAY METRIC TABLE

print("\n" + "-"*60)
print("ALGORITHM PERFORMANCE COMPARISON")
print("-"*60 + "\n")

display(results)


# ECONOMIC FAIRNESS BY TIER

print("\n" + "-"*60)
print("MATCH RATE BY ECONOMIC TIER")
print("-"*60 + "\n")

print("Stable Matching")
display(tier_match_rate(df_matches))

print("Greedy Baseline")
display(tier_match_rate(df_greedy))

print("Random Baseline")
display(tier_match_rate(df_random))


# VISUAL MATCH COUNT COMPARISON

import seaborn as sns
import matplotlib.pyplot as plt

match_counts = pd.DataFrame({
    "Algorithm": ["Stable Matching", "Greedy", "Random"],
    "Matches": [
        len(df_matches),
        len(df_greedy),
        len(df_random)
    ]
})

plt.figure(figsize=(8,5))
sns.barplot(x="Algorithm", y="Matches", data=match_counts)
plt.title("Match Count Comparison Across Algorithms")
plt.ylabel("Number of Matches")
plt.show()


print("\n" + "="*60)
print("EVALUATION COMPLETE")
print("="*60)
