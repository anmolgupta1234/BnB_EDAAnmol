import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="30-Day Advanced Stock EDA", layout="wide")
st.title("📊 Advanced 30-Day Stock EDA")

# -----------------------------
# Fixed Companies
# -----------------------------
companies = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Reliance": "RELIANCE.NS",
    "HDFC Bank": "HDFCBANK.NS"
}

index_map = {
    "Apple": "^GSPC",
    "Tesla": "^GSPC",
    "Reliance": "^NSEI",
    "HDFC Bank": "^NSEI"
}

selected = st.multiselect(
    "Select up to 2 companies",
    list(companies.keys()),
    default=["Apple", "Tesla"],
    max_selections=2
)

@st.cache_data
def load_data(tickers):
    return yf.download(tickers, period="45d", group_by="ticker")

if selected:

    tickers = [companies[name] for name in selected]
    data = load_data(tickers)

    returns_df = pd.DataFrame()
    volatility_dict = {}

    # -----------------------------
    # Closing Price Comparison
    # -----------------------------
    st.subheader("📈 Closing Price (Last 30 Trading Days)")
    fig1, ax1 = plt.subplots()

    for name in selected:
        ticker = companies[name]
        df = data[ticker].dropna().tail(30)

        ax1.plot(df["Close"], label=name)

        df["Daily Return"] = df["Close"].pct_change()
        returns_df[name] = df["Daily Return"]

        volatility = df["Daily Return"].std()
        volatility_dict[name] = volatility

    ax1.legend()
    st.pyplot(fig1)

    # -----------------------------
    # Trading Volume Comparison
    # -----------------------------
    st.subheader("📊 Trading Volume Comparison")
    fig2, ax2 = plt.subplots()

    for name in selected:
        ticker = companies[name]
        df = data[ticker].dropna().tail(30)
        ax2.plot(df["Volume"], label=name)

    ax2.legend()
    st.pyplot(fig2)

    # -----------------------------
    # Correlation Matrix
    # -----------------------------
    if len(selected) > 1:
        st.subheader("🔗 Correlation Matrix")

        aligned_returns = returns_df.dropna()
        corr_matrix = aligned_returns.corr()

        st.write(corr_matrix)

        fig3, ax3 = plt.subplots()
        cax = ax3.matshow(corr_matrix)
        plt.colorbar(cax)
        ax3.set_xticks(range(len(selected)))
        ax3.set_yticks(range(len(selected)))
        ax3.set_xticklabels(selected)
        ax3.set_yticklabels(selected)
        st.pyplot(fig3)

    # -----------------------------
    # Growth vs Market Index
    # -----------------------------
    st.subheader("📈 Growth vs Market Index (Base = 100)")

    fig4, ax4 = plt.subplots()

    for name in selected:
        ticker = companies[name]
        df = data[ticker].dropna().tail(30)

        index_ticker = index_map[name]
        index_data = yf.download(index_ticker, period="45d")
        index_df = index_data.dropna().tail(30)

        stock_norm = df["Close"] / df["Close"].iloc[0] * 100
        index_norm = index_df["Close"] / index_df["Close"].iloc[0] * 100

        ax4.plot(stock_norm, label=name)
        ax4.plot(index_norm, linestyle="--", label=f"{name} Index")

    ax4.legend()
    st.pyplot(fig4)

    # -----------------------------
    # Volatility Ranking
    # -----------------------------
    st.subheader("⚡ Volatility Ranking (30-Day Std Dev)")

    vol_df = pd.DataFrame.from_dict(
        volatility_dict, orient="index", columns=["Volatility"]
    )

    vol_df = vol_df.sort_values(by="Volatility", ascending=False)
    st.write(vol_df)