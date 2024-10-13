from decouple import config

crypto_data = [
    {
        "ticker": "BTC",
        "name": "Bitcoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BTC.png"
    },
    {
        "ticker": "ETH",
        "name": "Ethereum",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ETH.png"
    },
    {
        "ticker": "USDT",
        "name": "Tether USDt",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/USDT.png"
    },
    {
        "ticker": "BNB",
        "name": "BNB",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BNB.png"
    },
    {
        "ticker": "SOL",
        "name": "Solana",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/SOL.png"
    },
    {
        "ticker": "USDC",
        "name": "USDC",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/USDC.png"
    },
    {
        "ticker": "XRP",
        "name": "XRP",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/XRP.png"
    },
    {
        "ticker": "DOGE",
        "name": "Dogecoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/DOGE.png"
    },
    {
        "ticker": "TRX",
        "name": "TRON",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/TRX.png"
    },
    {
        "ticker": "TON",
        "name": "Toncoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/TON.png"
    },
    {
        "ticker": "ADA",
        "name": "Cardano",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ADA.png"
    },
    {
        "ticker": "AVAX",
        "name": "Avalanche",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/AVAX.png"
    },
    {
        "ticker": "SHIB",
        "name": "Shiba Inu",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/SHIB.png"
    },
    {
        "ticker": "LINK",
        "name": "Chainlink",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/LINK.png"
    },
    {
        "ticker": "BCH",
        "name": "Bitcoin Cash",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BCH.png"
    },
    {
        "ticker": "DOT",
        "name": "Polkadot",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/DOT.png"
    },
    {
        "ticker": "SUI",
        "name": "Sui",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/SUI.png"
    },
    {
        "ticker": "NEAR",
        "name": "NEAR Protocol",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/NEAR.png"
    },
    {
        "ticker": "LEO",
        "name": "UNUS SED LEO",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/LEO.png"
    },
    {
        "ticker": "DAI",
        "name": "Dai",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/DAI.png"
    },
    {
        "ticker": "APT",
        "name": "Aptos",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/APT.png"
    },
    {
        "ticker": "LTC",
        "name": "Litecoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/LTC.png"
    },
    {
        "ticker": "UNI",
        "name": "Uniswap",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/UNI.png"
    },
    {
        "ticker": "TAO",
        "name": "Bittensor",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/TAO.png"
    },
    {
        "ticker": "PEPE",
        "name": "Pepe",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/PEPE.png"
    },
    {
        "ticker": "ICP",
        "name": "Internet Computer",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ICP.png"
    },
    {
        "ticker": "FET",
        "name": "Artificial Superintelligence Alliance",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FET.png"
    },
    {
        "ticker": "KAS",
        "name": "Kaspa",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/KAS.png"
    },
    {
        "ticker": "FDUSD",
        "name": "First Digital USD",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FDUSD.png"
    },
    {
        "ticker": "XMR",
        "name": "Monero",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/XMR.png"
    },
    {
        "ticker": "POL",
        "name": "POL (ex-MATIC)",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/POL.png"
    },
    {
        "ticker": "WIF",
        "name": "dogwifhat",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/WIF.png"
    },
    {
        "ticker": "ETC",
        "name": "Ethereum Classic",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ETC.png"
    },
    {
        "ticker": "RENDER",
        "name": "Render",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/RENDER.png"
    },
    {
        "ticker": "XLM",
        "name": "Stellar",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/XLM.png"
    },
    {
        "ticker": "STX",
        "name": "Stacks",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/STX.png"
    },
    {
        "ticker": "OKB",
        "name": "OKB",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/OKB.png"
    },
    {
        "ticker": "IMX",
        "name": "Immutable",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/IMX.png"
    },
    {
        "ticker": "AAVE",
        "name": "Aave",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/AAVE.png"
    },
    {
        "ticker": "OP",
        "name": "Optimism",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/OP.png"
    },
    {
        "ticker": "FIL",
        "name": "Filecoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FIL.png"
    },
    {
        "ticker": "CRO",
        "name": "Cronos",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/CRO.png"
    },
    {
        "ticker": "INJ",
        "name": "Injective",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/INJ.png"
    },
    {
        "ticker": "MNT",
        "name": "Mantle",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/MNT.png"
    },
    {
        "ticker": "FTM",
        "name": "Fantom",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FTM.png"
    },
    {
        "ticker": "ARB",
        "name": "Arbitrum",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ARB.png"
    },
    {
        "ticker": "HBAR",
        "name": "Hedera",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/HBAR.png"
    },
    {
        "ticker": "VET",
        "name": "VeChain",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/VET.png"
    },
    {
        "ticker": "SEI",
        "name": "Sei",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/SEI.png"
    },
    {
        "ticker": "ATOM",
        "name": "Cosmos",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ATOM.png"
    },
    {
        "ticker": "RUNE",
        "name": "THORChain",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/RUNE.png"
    },
    {
        "ticker": "GRT",
        "name": "The Graph",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/GRT.png"
    },
    {
        "ticker": "BONK",
        "name": "Bonk",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BONK.png"
    },
    {
        "ticker": "BGB",
        "name": "Bitget Token",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BGB.png"
    },
    {
        "ticker": "POPCAT",
        "name": "Popcat (SOL)",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/POPCAT.png"
    },
    {
        "ticker": "FLOKI",
        "name": "FLOKI",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FLOKI.png"
    },
    {
        "ticker": "TIA",
        "name": "Celestia",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/TIA.png"
    },
    {
        "ticker": "THETA",
        "name": "Theta Network",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/THETA.png"
    },
    {
        "ticker": "AR",
        "name": "Arweave",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/AR.png"
    },
    {
        "ticker": "OM",
        "name": "MANTRA",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/OM.png"
    },
    {
        "ticker": "MKR",
        "name": "Maker",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/MKR.png"
    },
    {
        "ticker": "PYTH",
        "name": "Pyth Network",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/PYTH.png"
    },
    {
        "ticker": "HNT",
        "name": "Helium",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/HNT.png"
    },
    {
        "ticker": "JUP",
        "name": "Jupiter",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/JUP.png"
    },
    {
        "ticker": "WLD",
        "name": "Worldcoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/WLD.png"
    },
    {
        "ticker": "ALGO",
        "name": "Algorand",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ALGO.png"
    },
    {
        "ticker": "MATIC",
        "name": "Polygon",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/MATIC.png"
    },
    {
        "ticker": "KCS",
        "name": "KuCoin Token",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/KCS.png"
    },
    {
        "ticker": "ONDO",
        "name": "Ondo",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ONDO.png"
    },
    {
        "ticker": "BRETT",
        "name": "Brett (Based)",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BRETT.png"
    },
    {
        "ticker": "JASMY",
        "name": "JasmyCoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/JASMY.png"
    },
    {
        "ticker": "LDO",
        "name": "Lido DAO",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/LDO.png"
    },
    {
        "ticker": "ENA",
        "name": "Ethena",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ENA.png"
    },
    {
        "ticker": "BSV",
        "name": "Bitcoin SV",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BSV.png"
    },
    {
        "ticker": "BTT",
        "name": "BitTorrent [New]",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BTT.png"
    },
    {
        "ticker": "CORE",
        "name": "Core",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/CORE.png"
    },
    {
        "ticker": "FLOW",
        "name": "Flow",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FLOW.png"
    },
    {
        "ticker": "STRK",
        "name": "Starknet",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/STRK.png"
    },
    {
        "ticker": "NEIRO",
        "name": "First Neiro On Ethereum",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/NEIRO.png"
    },
    {
        "ticker": "GT",
        "name": "GateToken",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/GT.png"
    },
    {
        "ticker": "W",
        "name": "Wormhole",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/W.png"
    },
    {
        "ticker": "NOT",
        "name": "Notcoin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/NOT.png"
    },
    {
        "ticker": "QNT",
        "name": "Quant",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/QNT.png"
    },
    {
        "ticker": "CFX",
        "name": "Conflux",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/CFX.png"
    },
    {
        "ticker": "BEAM",
        "name": "Beam",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/BEAM.png"
    },
    {
        "ticker": "GALA",
        "name": "Gala",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/GALA.png"
    },
    {
        "ticker": "ORDI",
        "name": "ORDI",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/ORDI.png"
    },
    {
        "ticker": "USDD",
        "name": "USDD",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/USDD.png"
    },
    {
        "ticker": "EGLD",
        "name": "MultiversX",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/EGLD.png"
    },
    {
        "ticker": "MOG",
        "name": "Mog Coin",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/MOG.png"
    },
    {
        "ticker": "NEO",
        "name": "Neo",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/NEO.png"
    },
    {
        "ticker": "FLR",
        "name": "Flare",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FLR.png"
    },
    {
        "ticker": "EOS",
        "name": "EOS",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/EOS.png"
    },
    {
        "ticker": "AXS",
        "name": "Axie Infinity",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/AXS.png"
    },
    {
        "ticker": "CHZ",
        "name": "Chiliz",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/CHZ.png"
    },
    {
        "ticker": "XTZ",
        "name": "Tezos",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/XTZ.png"
    },
    {
        "ticker": "FTT",
        "name": "FTX Token",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/FTT.png"
    },
    {
        "ticker": "CKB",
        "name": "Nervos Network",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/CKB.png"
    },
    {
        "ticker": "XEC",
        "name": "eCash",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/XEC.png"
    },
    {
        "ticker": "MINA",
        "name": "Mina",
        "logo": config('BASE_URL')+"/static/images/crypto_logos/MINA.png"
    }
]

