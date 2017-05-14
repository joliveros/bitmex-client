# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [Changelog](/app/apiChangelog)  ----  #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ----  ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: jose.oliveros.1983@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Margin(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account=None, currency=None, risk_limit=None, prev_state=None, state=None, action=None, amount=None, pending_credit=None, pending_debit=None, confirmed_debit=None, prev_realised_pnl=None, prev_unrealised_pnl=None, gross_comm=None, gross_open_cost=None, gross_open_premium=None, gross_exec_cost=None, gross_mark_value=None, risk_value=None, taxable_margin=None, init_margin=None, maint_margin=None, session_margin=None, target_excess_margin=None, var_margin=None, realised_pnl=None, unrealised_pnl=None, indicative_tax=None, unrealised_profit=None, synthetic_margin=None, wallet_balance=None, margin_balance=None, margin_balance_pcnt=0.0, margin_leverage=0.0, margin_used_pcnt=0.0, excess_margin=None, excess_margin_pcnt=0.0, available_margin=None, withdrawable_margin=None, timestamp=None, gross_last_value=None, commission=0.0):
        """
        Margin - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account': 'float',
            'currency': 'str',
            'risk_limit': 'float',
            'prev_state': 'str',
            'state': 'str',
            'action': 'str',
            'amount': 'float',
            'pending_credit': 'float',
            'pending_debit': 'float',
            'confirmed_debit': 'float',
            'prev_realised_pnl': 'float',
            'prev_unrealised_pnl': 'float',
            'gross_comm': 'float',
            'gross_open_cost': 'float',
            'gross_open_premium': 'float',
            'gross_exec_cost': 'float',
            'gross_mark_value': 'float',
            'risk_value': 'float',
            'taxable_margin': 'float',
            'init_margin': 'float',
            'maint_margin': 'float',
            'session_margin': 'float',
            'target_excess_margin': 'float',
            'var_margin': 'float',
            'realised_pnl': 'float',
            'unrealised_pnl': 'float',
            'indicative_tax': 'float',
            'unrealised_profit': 'float',
            'synthetic_margin': 'float',
            'wallet_balance': 'float',
            'margin_balance': 'float',
            'margin_balance_pcnt': 'float',
            'margin_leverage': 'float',
            'margin_used_pcnt': 'float',
            'excess_margin': 'float',
            'excess_margin_pcnt': 'float',
            'available_margin': 'float',
            'withdrawable_margin': 'float',
            'timestamp': 'datetime',
            'gross_last_value': 'float',
            'commission': 'float'
        }

        self.attribute_map = {
            'account': 'account',
            'currency': 'currency',
            'risk_limit': 'riskLimit',
            'prev_state': 'prevState',
            'state': 'state',
            'action': 'action',
            'amount': 'amount',
            'pending_credit': 'pendingCredit',
            'pending_debit': 'pendingDebit',
            'confirmed_debit': 'confirmedDebit',
            'prev_realised_pnl': 'prevRealisedPnl',
            'prev_unrealised_pnl': 'prevUnrealisedPnl',
            'gross_comm': 'grossComm',
            'gross_open_cost': 'grossOpenCost',
            'gross_open_premium': 'grossOpenPremium',
            'gross_exec_cost': 'grossExecCost',
            'gross_mark_value': 'grossMarkValue',
            'risk_value': 'riskValue',
            'taxable_margin': 'taxableMargin',
            'init_margin': 'initMargin',
            'maint_margin': 'maintMargin',
            'session_margin': 'sessionMargin',
            'target_excess_margin': 'targetExcessMargin',
            'var_margin': 'varMargin',
            'realised_pnl': 'realisedPnl',
            'unrealised_pnl': 'unrealisedPnl',
            'indicative_tax': 'indicativeTax',
            'unrealised_profit': 'unrealisedProfit',
            'synthetic_margin': 'syntheticMargin',
            'wallet_balance': 'walletBalance',
            'margin_balance': 'marginBalance',
            'margin_balance_pcnt': 'marginBalancePcnt',
            'margin_leverage': 'marginLeverage',
            'margin_used_pcnt': 'marginUsedPcnt',
            'excess_margin': 'excessMargin',
            'excess_margin_pcnt': 'excessMarginPcnt',
            'available_margin': 'availableMargin',
            'withdrawable_margin': 'withdrawableMargin',
            'timestamp': 'timestamp',
            'gross_last_value': 'grossLastValue',
            'commission': 'commission'
        }

        self._account = None
        self._currency = None
        self._risk_limit = None
        self._prev_state = None
        self._state = None
        self._action = None
        self._amount = None
        self._pending_credit = None
        self._pending_debit = None
        self._confirmed_debit = None
        self._prev_realised_pnl = None
        self._prev_unrealised_pnl = None
        self._gross_comm = None
        self._gross_open_cost = None
        self._gross_open_premium = None
        self._gross_exec_cost = None
        self._gross_mark_value = None
        self._risk_value = None
        self._taxable_margin = None
        self._init_margin = None
        self._maint_margin = None
        self._session_margin = None
        self._target_excess_margin = None
        self._var_margin = None
        self._realised_pnl = None
        self._unrealised_pnl = None
        self._indicative_tax = None
        self._unrealised_profit = None
        self._synthetic_margin = None
        self._wallet_balance = None
        self._margin_balance = None
        self._margin_balance_pcnt = None
        self._margin_leverage = None
        self._margin_used_pcnt = None
        self._excess_margin = None
        self._excess_margin_pcnt = None
        self._available_margin = None
        self._withdrawable_margin = None
        self._timestamp = None
        self._gross_last_value = None
        self._commission = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if account is not None:
          self.account = account
        if currency is not None:
          self.currency = currency
        if risk_limit is not None:
          self.risk_limit = risk_limit
        if prev_state is not None:
          self.prev_state = prev_state
        if state is not None:
          self.state = state
        if action is not None:
          self.action = action
        if amount is not None:
          self.amount = amount
        if pending_credit is not None:
          self.pending_credit = pending_credit
        if pending_debit is not None:
          self.pending_debit = pending_debit
        if confirmed_debit is not None:
          self.confirmed_debit = confirmed_debit
        if prev_realised_pnl is not None:
          self.prev_realised_pnl = prev_realised_pnl
        if prev_unrealised_pnl is not None:
          self.prev_unrealised_pnl = prev_unrealised_pnl
        if gross_comm is not None:
          self.gross_comm = gross_comm
        if gross_open_cost is not None:
          self.gross_open_cost = gross_open_cost
        if gross_open_premium is not None:
          self.gross_open_premium = gross_open_premium
        if gross_exec_cost is not None:
          self.gross_exec_cost = gross_exec_cost
        if gross_mark_value is not None:
          self.gross_mark_value = gross_mark_value
        if risk_value is not None:
          self.risk_value = risk_value
        if taxable_margin is not None:
          self.taxable_margin = taxable_margin
        if init_margin is not None:
          self.init_margin = init_margin
        if maint_margin is not None:
          self.maint_margin = maint_margin
        if session_margin is not None:
          self.session_margin = session_margin
        if target_excess_margin is not None:
          self.target_excess_margin = target_excess_margin
        if var_margin is not None:
          self.var_margin = var_margin
        if realised_pnl is not None:
          self.realised_pnl = realised_pnl
        if unrealised_pnl is not None:
          self.unrealised_pnl = unrealised_pnl
        if indicative_tax is not None:
          self.indicative_tax = indicative_tax
        if unrealised_profit is not None:
          self.unrealised_profit = unrealised_profit
        if synthetic_margin is not None:
          self.synthetic_margin = synthetic_margin
        if wallet_balance is not None:
          self.wallet_balance = wallet_balance
        if margin_balance is not None:
          self.margin_balance = margin_balance
        if margin_balance_pcnt is not None:
          self.margin_balance_pcnt = margin_balance_pcnt
        if margin_leverage is not None:
          self.margin_leverage = margin_leverage
        if margin_used_pcnt is not None:
          self.margin_used_pcnt = margin_used_pcnt
        if excess_margin is not None:
          self.excess_margin = excess_margin
        if excess_margin_pcnt is not None:
          self.excess_margin_pcnt = excess_margin_pcnt
        if available_margin is not None:
          self.available_margin = available_margin
        if withdrawable_margin is not None:
          self.withdrawable_margin = withdrawable_margin
        if timestamp is not None:
          self.timestamp = timestamp
        if gross_last_value is not None:
          self.gross_last_value = gross_last_value
        if commission is not None:
          self.commission = commission

    @property
    def account(self):
        """
        Gets the account of this Margin.

        :return: The account of this Margin.
        :rtype: float
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Margin.

        :param account: The account of this Margin.
        :type: float
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")

        self._account = account

    @property
    def currency(self):
        """
        Gets the currency of this Margin.

        :return: The currency of this Margin.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Margin.

        :param currency: The currency of this Margin.
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")

        self._currency = currency

    @property
    def risk_limit(self):
        """
        Gets the risk_limit of this Margin.

        :return: The risk_limit of this Margin.
        :rtype: float
        """
        return self._risk_limit

    @risk_limit.setter
    def risk_limit(self, risk_limit):
        """
        Sets the risk_limit of this Margin.

        :param risk_limit: The risk_limit of this Margin.
        :type: float
        """

        self._risk_limit = risk_limit

    @property
    def prev_state(self):
        """
        Gets the prev_state of this Margin.

        :return: The prev_state of this Margin.
        :rtype: str
        """
        return self._prev_state

    @prev_state.setter
    def prev_state(self, prev_state):
        """
        Sets the prev_state of this Margin.

        :param prev_state: The prev_state of this Margin.
        :type: str
        """

        self._prev_state = prev_state

    @property
    def state(self):
        """
        Gets the state of this Margin.

        :return: The state of this Margin.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Margin.

        :param state: The state of this Margin.
        :type: str
        """

        self._state = state

    @property
    def action(self):
        """
        Gets the action of this Margin.

        :return: The action of this Margin.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Margin.

        :param action: The action of this Margin.
        :type: str
        """

        self._action = action

    @property
    def amount(self):
        """
        Gets the amount of this Margin.

        :return: The amount of this Margin.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Margin.

        :param amount: The amount of this Margin.
        :type: float
        """

        self._amount = amount

    @property
    def pending_credit(self):
        """
        Gets the pending_credit of this Margin.

        :return: The pending_credit of this Margin.
        :rtype: float
        """
        return self._pending_credit

    @pending_credit.setter
    def pending_credit(self, pending_credit):
        """
        Sets the pending_credit of this Margin.

        :param pending_credit: The pending_credit of this Margin.
        :type: float
        """

        self._pending_credit = pending_credit

    @property
    def pending_debit(self):
        """
        Gets the pending_debit of this Margin.

        :return: The pending_debit of this Margin.
        :rtype: float
        """
        return self._pending_debit

    @pending_debit.setter
    def pending_debit(self, pending_debit):
        """
        Sets the pending_debit of this Margin.

        :param pending_debit: The pending_debit of this Margin.
        :type: float
        """

        self._pending_debit = pending_debit

    @property
    def confirmed_debit(self):
        """
        Gets the confirmed_debit of this Margin.

        :return: The confirmed_debit of this Margin.
        :rtype: float
        """
        return self._confirmed_debit

    @confirmed_debit.setter
    def confirmed_debit(self, confirmed_debit):
        """
        Sets the confirmed_debit of this Margin.

        :param confirmed_debit: The confirmed_debit of this Margin.
        :type: float
        """

        self._confirmed_debit = confirmed_debit

    @property
    def prev_realised_pnl(self):
        """
        Gets the prev_realised_pnl of this Margin.

        :return: The prev_realised_pnl of this Margin.
        :rtype: float
        """
        return self._prev_realised_pnl

    @prev_realised_pnl.setter
    def prev_realised_pnl(self, prev_realised_pnl):
        """
        Sets the prev_realised_pnl of this Margin.

        :param prev_realised_pnl: The prev_realised_pnl of this Margin.
        :type: float
        """

        self._prev_realised_pnl = prev_realised_pnl

    @property
    def prev_unrealised_pnl(self):
        """
        Gets the prev_unrealised_pnl of this Margin.

        :return: The prev_unrealised_pnl of this Margin.
        :rtype: float
        """
        return self._prev_unrealised_pnl

    @prev_unrealised_pnl.setter
    def prev_unrealised_pnl(self, prev_unrealised_pnl):
        """
        Sets the prev_unrealised_pnl of this Margin.

        :param prev_unrealised_pnl: The prev_unrealised_pnl of this Margin.
        :type: float
        """

        self._prev_unrealised_pnl = prev_unrealised_pnl

    @property
    def gross_comm(self):
        """
        Gets the gross_comm of this Margin.

        :return: The gross_comm of this Margin.
        :rtype: float
        """
        return self._gross_comm

    @gross_comm.setter
    def gross_comm(self, gross_comm):
        """
        Sets the gross_comm of this Margin.

        :param gross_comm: The gross_comm of this Margin.
        :type: float
        """

        self._gross_comm = gross_comm

    @property
    def gross_open_cost(self):
        """
        Gets the gross_open_cost of this Margin.

        :return: The gross_open_cost of this Margin.
        :rtype: float
        """
        return self._gross_open_cost

    @gross_open_cost.setter
    def gross_open_cost(self, gross_open_cost):
        """
        Sets the gross_open_cost of this Margin.

        :param gross_open_cost: The gross_open_cost of this Margin.
        :type: float
        """

        self._gross_open_cost = gross_open_cost

    @property
    def gross_open_premium(self):
        """
        Gets the gross_open_premium of this Margin.

        :return: The gross_open_premium of this Margin.
        :rtype: float
        """
        return self._gross_open_premium

    @gross_open_premium.setter
    def gross_open_premium(self, gross_open_premium):
        """
        Sets the gross_open_premium of this Margin.

        :param gross_open_premium: The gross_open_premium of this Margin.
        :type: float
        """

        self._gross_open_premium = gross_open_premium

    @property
    def gross_exec_cost(self):
        """
        Gets the gross_exec_cost of this Margin.

        :return: The gross_exec_cost of this Margin.
        :rtype: float
        """
        return self._gross_exec_cost

    @gross_exec_cost.setter
    def gross_exec_cost(self, gross_exec_cost):
        """
        Sets the gross_exec_cost of this Margin.

        :param gross_exec_cost: The gross_exec_cost of this Margin.
        :type: float
        """

        self._gross_exec_cost = gross_exec_cost

    @property
    def gross_mark_value(self):
        """
        Gets the gross_mark_value of this Margin.

        :return: The gross_mark_value of this Margin.
        :rtype: float
        """
        return self._gross_mark_value

    @gross_mark_value.setter
    def gross_mark_value(self, gross_mark_value):
        """
        Sets the gross_mark_value of this Margin.

        :param gross_mark_value: The gross_mark_value of this Margin.
        :type: float
        """

        self._gross_mark_value = gross_mark_value

    @property
    def risk_value(self):
        """
        Gets the risk_value of this Margin.

        :return: The risk_value of this Margin.
        :rtype: float
        """
        return self._risk_value

    @risk_value.setter
    def risk_value(self, risk_value):
        """
        Sets the risk_value of this Margin.

        :param risk_value: The risk_value of this Margin.
        :type: float
        """

        self._risk_value = risk_value

    @property
    def taxable_margin(self):
        """
        Gets the taxable_margin of this Margin.

        :return: The taxable_margin of this Margin.
        :rtype: float
        """
        return self._taxable_margin

    @taxable_margin.setter
    def taxable_margin(self, taxable_margin):
        """
        Sets the taxable_margin of this Margin.

        :param taxable_margin: The taxable_margin of this Margin.
        :type: float
        """

        self._taxable_margin = taxable_margin

    @property
    def init_margin(self):
        """
        Gets the init_margin of this Margin.

        :return: The init_margin of this Margin.
        :rtype: float
        """
        return self._init_margin

    @init_margin.setter
    def init_margin(self, init_margin):
        """
        Sets the init_margin of this Margin.

        :param init_margin: The init_margin of this Margin.
        :type: float
        """

        self._init_margin = init_margin

    @property
    def maint_margin(self):
        """
        Gets the maint_margin of this Margin.

        :return: The maint_margin of this Margin.
        :rtype: float
        """
        return self._maint_margin

    @maint_margin.setter
    def maint_margin(self, maint_margin):
        """
        Sets the maint_margin of this Margin.

        :param maint_margin: The maint_margin of this Margin.
        :type: float
        """

        self._maint_margin = maint_margin

    @property
    def session_margin(self):
        """
        Gets the session_margin of this Margin.

        :return: The session_margin of this Margin.
        :rtype: float
        """
        return self._session_margin

    @session_margin.setter
    def session_margin(self, session_margin):
        """
        Sets the session_margin of this Margin.

        :param session_margin: The session_margin of this Margin.
        :type: float
        """

        self._session_margin = session_margin

    @property
    def target_excess_margin(self):
        """
        Gets the target_excess_margin of this Margin.

        :return: The target_excess_margin of this Margin.
        :rtype: float
        """
        return self._target_excess_margin

    @target_excess_margin.setter
    def target_excess_margin(self, target_excess_margin):
        """
        Sets the target_excess_margin of this Margin.

        :param target_excess_margin: The target_excess_margin of this Margin.
        :type: float
        """

        self._target_excess_margin = target_excess_margin

    @property
    def var_margin(self):
        """
        Gets the var_margin of this Margin.

        :return: The var_margin of this Margin.
        :rtype: float
        """
        return self._var_margin

    @var_margin.setter
    def var_margin(self, var_margin):
        """
        Sets the var_margin of this Margin.

        :param var_margin: The var_margin of this Margin.
        :type: float
        """

        self._var_margin = var_margin

    @property
    def realised_pnl(self):
        """
        Gets the realised_pnl of this Margin.

        :return: The realised_pnl of this Margin.
        :rtype: float
        """
        return self._realised_pnl

    @realised_pnl.setter
    def realised_pnl(self, realised_pnl):
        """
        Sets the realised_pnl of this Margin.

        :param realised_pnl: The realised_pnl of this Margin.
        :type: float
        """

        self._realised_pnl = realised_pnl

    @property
    def unrealised_pnl(self):
        """
        Gets the unrealised_pnl of this Margin.

        :return: The unrealised_pnl of this Margin.
        :rtype: float
        """
        return self._unrealised_pnl

    @unrealised_pnl.setter
    def unrealised_pnl(self, unrealised_pnl):
        """
        Sets the unrealised_pnl of this Margin.

        :param unrealised_pnl: The unrealised_pnl of this Margin.
        :type: float
        """

        self._unrealised_pnl = unrealised_pnl

    @property
    def indicative_tax(self):
        """
        Gets the indicative_tax of this Margin.

        :return: The indicative_tax of this Margin.
        :rtype: float
        """
        return self._indicative_tax

    @indicative_tax.setter
    def indicative_tax(self, indicative_tax):
        """
        Sets the indicative_tax of this Margin.

        :param indicative_tax: The indicative_tax of this Margin.
        :type: float
        """

        self._indicative_tax = indicative_tax

    @property
    def unrealised_profit(self):
        """
        Gets the unrealised_profit of this Margin.

        :return: The unrealised_profit of this Margin.
        :rtype: float
        """
        return self._unrealised_profit

    @unrealised_profit.setter
    def unrealised_profit(self, unrealised_profit):
        """
        Sets the unrealised_profit of this Margin.

        :param unrealised_profit: The unrealised_profit of this Margin.
        :type: float
        """

        self._unrealised_profit = unrealised_profit

    @property
    def synthetic_margin(self):
        """
        Gets the synthetic_margin of this Margin.

        :return: The synthetic_margin of this Margin.
        :rtype: float
        """
        return self._synthetic_margin

    @synthetic_margin.setter
    def synthetic_margin(self, synthetic_margin):
        """
        Sets the synthetic_margin of this Margin.

        :param synthetic_margin: The synthetic_margin of this Margin.
        :type: float
        """

        self._synthetic_margin = synthetic_margin

    @property
    def wallet_balance(self):
        """
        Gets the wallet_balance of this Margin.

        :return: The wallet_balance of this Margin.
        :rtype: float
        """
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wallet_balance):
        """
        Sets the wallet_balance of this Margin.

        :param wallet_balance: The wallet_balance of this Margin.
        :type: float
        """

        self._wallet_balance = wallet_balance

    @property
    def margin_balance(self):
        """
        Gets the margin_balance of this Margin.

        :return: The margin_balance of this Margin.
        :rtype: float
        """
        return self._margin_balance

    @margin_balance.setter
    def margin_balance(self, margin_balance):
        """
        Sets the margin_balance of this Margin.

        :param margin_balance: The margin_balance of this Margin.
        :type: float
        """

        self._margin_balance = margin_balance

    @property
    def margin_balance_pcnt(self):
        """
        Gets the margin_balance_pcnt of this Margin.

        :return: The margin_balance_pcnt of this Margin.
        :rtype: float
        """
        return self._margin_balance_pcnt

    @margin_balance_pcnt.setter
    def margin_balance_pcnt(self, margin_balance_pcnt):
        """
        Sets the margin_balance_pcnt of this Margin.

        :param margin_balance_pcnt: The margin_balance_pcnt of this Margin.
        :type: float
        """

        self._margin_balance_pcnt = margin_balance_pcnt

    @property
    def margin_leverage(self):
        """
        Gets the margin_leverage of this Margin.

        :return: The margin_leverage of this Margin.
        :rtype: float
        """
        return self._margin_leverage

    @margin_leverage.setter
    def margin_leverage(self, margin_leverage):
        """
        Sets the margin_leverage of this Margin.

        :param margin_leverage: The margin_leverage of this Margin.
        :type: float
        """

        self._margin_leverage = margin_leverage

    @property
    def margin_used_pcnt(self):
        """
        Gets the margin_used_pcnt of this Margin.

        :return: The margin_used_pcnt of this Margin.
        :rtype: float
        """
        return self._margin_used_pcnt

    @margin_used_pcnt.setter
    def margin_used_pcnt(self, margin_used_pcnt):
        """
        Sets the margin_used_pcnt of this Margin.

        :param margin_used_pcnt: The margin_used_pcnt of this Margin.
        :type: float
        """

        self._margin_used_pcnt = margin_used_pcnt

    @property
    def excess_margin(self):
        """
        Gets the excess_margin of this Margin.

        :return: The excess_margin of this Margin.
        :rtype: float
        """
        return self._excess_margin

    @excess_margin.setter
    def excess_margin(self, excess_margin):
        """
        Sets the excess_margin of this Margin.

        :param excess_margin: The excess_margin of this Margin.
        :type: float
        """

        self._excess_margin = excess_margin

    @property
    def excess_margin_pcnt(self):
        """
        Gets the excess_margin_pcnt of this Margin.

        :return: The excess_margin_pcnt of this Margin.
        :rtype: float
        """
        return self._excess_margin_pcnt

    @excess_margin_pcnt.setter
    def excess_margin_pcnt(self, excess_margin_pcnt):
        """
        Sets the excess_margin_pcnt of this Margin.

        :param excess_margin_pcnt: The excess_margin_pcnt of this Margin.
        :type: float
        """

        self._excess_margin_pcnt = excess_margin_pcnt

    @property
    def available_margin(self):
        """
        Gets the available_margin of this Margin.

        :return: The available_margin of this Margin.
        :rtype: float
        """
        return self._available_margin

    @available_margin.setter
    def available_margin(self, available_margin):
        """
        Sets the available_margin of this Margin.

        :param available_margin: The available_margin of this Margin.
        :type: float
        """

        self._available_margin = available_margin

    @property
    def withdrawable_margin(self):
        """
        Gets the withdrawable_margin of this Margin.

        :return: The withdrawable_margin of this Margin.
        :rtype: float
        """
        return self._withdrawable_margin

    @withdrawable_margin.setter
    def withdrawable_margin(self, withdrawable_margin):
        """
        Sets the withdrawable_margin of this Margin.

        :param withdrawable_margin: The withdrawable_margin of this Margin.
        :type: float
        """

        self._withdrawable_margin = withdrawable_margin

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Margin.

        :return: The timestamp of this Margin.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Margin.

        :param timestamp: The timestamp of this Margin.
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def gross_last_value(self):
        """
        Gets the gross_last_value of this Margin.

        :return: The gross_last_value of this Margin.
        :rtype: float
        """
        return self._gross_last_value

    @gross_last_value.setter
    def gross_last_value(self, gross_last_value):
        """
        Sets the gross_last_value of this Margin.

        :param gross_last_value: The gross_last_value of this Margin.
        :type: float
        """

        self._gross_last_value = gross_last_value

    @property
    def commission(self):
        """
        Gets the commission of this Margin.

        :return: The commission of this Margin.
        :rtype: float
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """
        Sets the commission of this Margin.

        :param commission: The commission of this Margin.
        :type: float
        """

        self._commission = commission

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Margin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
