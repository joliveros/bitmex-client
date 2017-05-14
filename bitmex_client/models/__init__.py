# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [Changelog](/app/apiChangelog)  ----  #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ----  ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: jose.oliveros.1983@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .api_key import APIKey
from .access_token import AccessToken
from .affiliate import Affiliate
from .announcement import Announcement
from .chat import Chat
from .chat_channel import ChatChannel
from .connected_users import ConnectedUsers
from .error import Error
from .error_error import ErrorError
from .execution import Execution
from .funding import Funding
from .index_composite import IndexComposite
from .inline_response_200 import InlineResponse200
from .instrument import Instrument
from .instrument_interval import InstrumentInterval
from .insurance import Insurance
from .leaderboard import Leaderboard
from .liquidation import Liquidation
from .margin import Margin
from .notification import Notification
from .order import Order
from .order_book import OrderBook
from .order_book_l2 import OrderBookL2
from .position import Position
from .quote import Quote
from .settlement import Settlement
from .stats import Stats
from .stats_history import StatsHistory
from .trade import Trade
from .trade_bin import TradeBin
from .transaction import Transaction
from .user import User
from .user_commission import UserCommission
from .user_preferences import UserPreferences
from .wallet import Wallet
from .x_any import XAny
