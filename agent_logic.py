# @title 🎯 RUN NARRATIVE SNIPER AGENT
# Click the "Play" button (▶️) on the left to start the scan.

import requests
import json
from datetime import datetime, timedelta
import time

# --- 1. CONFIGURATION ---
# ⚠️ REPLACE THIS WITH YOUR ACTUAL GITHUB TOKEN ⚠️
GITHUB_TOKEN = "PASTE_YOUR_GITHUB_TOKEN_HERE" 

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# --- 2. THE SCANNER (Dev Signal) ---
def scan_github_signals():
    print("📡 INITIALIZING SOLANA NARRATIVE SCAN...")
    print("------------------------------------------------")
    
    # Look for Solana repos created in the last 14 days
    date_cutoff = (datetime.now() - timedelta(days=14)).strftime('%Y-%m-%d')
    query = f"topic:solana created:>{date_cutoff} sort:stars"
    url = f"https://api.github.com/search/repositories?q={query}&per_page=20"
    
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code}")
            print("   (Did you forget to add your GitHub Token?)")
            return []
            
        repos = response.json().get("items", [])
        print(f"✅ FOUND {len(repos)} EMERGING PROJECTS (Created after {date_cutoff})")
        return repos
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return []

# --- 3. THE ANALYZER (Narrative Engine) ---
def analyze_narratives(repos):
    print("🧠 ANALYZING DEV ACTIVITY FOR PATTERNS...")
    time.sleep(1) # Simulating "thinking" time
    
    signals = {
        "AI Agents": 0,
        "DePIN": 0,
        "DeFi 2.0": 0,
        "Meme Infra": 0,
        "Gaming": 0
    }
    
    top_repos = []

    for repo in repos:
        name = repo['name']
        desc = (repo['description'] or "").lower()
        topics = " ".join(repo.get('topics', [])).lower()
        combined_text = desc + " " + topics
        stars = repo['stargazers_count']
        url = repo['html_url']

        # Determine Narrative Category
        category = "Unknown"
        if "ai" in combined_text or "agent" in combined_text or "bot" in combined_text:
            category = "AI Agents"
            signals["AI Agents"] += 1
        elif "depin" in combined_text or "compute" in combined_text:
            category = "DePIN"
            signals["DePIN"] += 1
        elif "pump" in combined_text or "meme" in combined_text:
            category = "Meme Infra"
            signals["Meme Infra"] += 1
        elif "swap" in combined_text or "dex" in combined_text:
            category = "DeFi 2.0"
            signals["DeFi 2.0"] += 1
        
        top_repos.append(f"⭐ [{stars}] {name} ({category}) -> {url}")

    # Identify Top Trend
    sorted_signals = sorted(signals.items(), key=lambda x: x[1], reverse=True)
    top_trend = sorted_signals[0][0]
    
    return top_trend, signals, top_repos

# --- 4. THE REPORTER (Output) ---
def generate_report(top_trend, signals, top_repos):
    print("\n" + "="*50)
    print(f"🚀 SOLANA NARRATIVE REPORT: {datetime.now().strftime('%B %Y')}")
    print("="*50)
    
    print(f"\n🚨 DOMINANT NARRATIVE DETECTED: {top_trend.upper()}")
    print(f"   Strength: {signals[top_trend]} new repositories in 14 days.")
    print(f"   Analysis: Developer focus has shifted heavily towards {top_trend}.")
    
    print("\n📊 SIGNAL DISTRIBUTION:")
    for k, v in signals.items():
        if v > 0:
            bar = "█" * v
            print(f"   {k.ljust(12)} | {bar} ({v})")
            
    print("\n💎 TOP 5 EMERGING REPOS (ALPHA):")
    for r in top_repos[:5]:
        print(f"   {r}")
        
    print("\n💡 GENERATED BUILD IDEAS:")
    if top_trend == "AI Agents":
        print("   1. 'Agent-Only' DEX Interface: An SDK for bots to swap without UI overhead.")
        print("   2. Autonomous Pump.fun Manager: Agent that launches & manages tokens automatically.")
        print("   3. Verifiable Compute Market: Rent GPU power to agents for inference.")
    elif top_trend == "Meme Infra":
        print("   1. Self-Hosted Trading Terminal: Privacy-focused dashboard for memecoins.")
        print("   2. Sniping-as-a-Service API: Enterprise grade sniper for retail.")
    else:
        print("   1. Cross-Chain Yield Aggregator: Auto-compounder for new stablecoins.")
        print("   2. Social-Fi Identity Layer: Connect X reputation to on-chain wallet.")
        
    print("\n" + "="*50)
    print("✅ REPORT GENERATION COMPLETE.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    found_repos = scan_github_signals()
    if found_repos:
        trend, sigs, top_list = analyze_narratives(found_repos)
        generate_report(trend, sigs, top_list)
