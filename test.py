api_key = bsKcHqssAsb0tUXIeoa1xRiDmkZhgOvtpoR7SxVJ
secret_key = PKVBHTT8J52DSBBQMDV1
paper = True


trade_api_url = None
trade_api_wss = None
data_api_url = None
option_stream_data_wss = None

import os

if api_key is None:
    api_key = os.environ.get('ALPACA_API_KEY')

if secret_key is None:
    secret_key = os.environ.get('ALPACA_SECRET_KEY')


try:
    import alpaca
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "alpaca-py"])
    import alpaca

import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical.option import OptionHistoricalDataClient
from alpaca.trading.stream import TradingStream
from alpaca.data.live.option import OptionDataStream
from alpaca.data.requests import (
    OptionBarsRequest,
    OptionTradesRequest,
    OptionLatestQuoteRequest,
    OptionLatestTradeRequest,
    OptionSnapshotRequest,
    OptionChainRequest    
)
from alpaca.trading.requests import (
    GetOptionContractsRequest,
    GetAssetsRequest,
    MarketOrderRequest,
    GetOrdersRequest,
    ClosePositionRequest
)
from alpaca.trading.enums import (
    AssetStatus,
    ExerciseStyle,
    OrderSide,
    OrderType,
    TimeInForce,
    QueryOrderStatus 
)
from alpaca.common.exceptions import APIError
import nest_asyncio
nest_asyncio.apply()
alpaca.__version__