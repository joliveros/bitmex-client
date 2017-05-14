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


class APIKey(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, secret=None, name=None, nonce=None, cidr=None, permissions=None, enabled=False, user_id=None, created=None):
        """
        APIKey - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'secret': 'str',
            'name': 'str',
            'nonce': 'float',
            'cidr': 'str',
            'permissions': 'list[XAny]',
            'enabled': 'bool',
            'user_id': 'float',
            'created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'secret': 'secret',
            'name': 'name',
            'nonce': 'nonce',
            'cidr': 'cidr',
            'permissions': 'permissions',
            'enabled': 'enabled',
            'user_id': 'userId',
            'created': 'created'
        }

        self._id = None
        self._secret = None
        self._name = None
        self._nonce = None
        self._cidr = None
        self._permissions = None
        self._enabled = None
        self._user_id = None
        self._created = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if id is not None:
          self.id = id
        if secret is not None:
          self.secret = secret
        if name is not None:
          self.name = name
        if nonce is not None:
          self.nonce = nonce
        if cidr is not None:
          self.cidr = cidr
        if permissions is not None:
          self.permissions = permissions
        if enabled is not None:
          self.enabled = enabled
        if user_id is not None:
          self.user_id = user_id
        if created is not None:
          self.created = created

    @property
    def id(self):
        """
        Gets the id of this APIKey.

        :return: The id of this APIKey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this APIKey.

        :param id: The id of this APIKey.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if id is not None and len(id) > 24:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `24`")

        self._id = id

    @property
    def secret(self):
        """
        Gets the secret of this APIKey.

        :return: The secret of this APIKey.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this APIKey.

        :param secret: The secret of this APIKey.
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")
        if secret is not None and len(secret) > 48:
            raise ValueError("Invalid value for `secret`, length must be less than or equal to `48`")

        self._secret = secret

    @property
    def name(self):
        """
        Gets the name of this APIKey.

        :return: The name of this APIKey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this APIKey.

        :param name: The name of this APIKey.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")

        self._name = name

    @property
    def nonce(self):
        """
        Gets the nonce of this APIKey.

        :return: The nonce of this APIKey.
        :rtype: float
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """
        Sets the nonce of this APIKey.

        :param nonce: The nonce of this APIKey.
        :type: float
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")

        self._nonce = nonce

    @property
    def cidr(self):
        """
        Gets the cidr of this APIKey.

        :return: The cidr of this APIKey.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """
        Sets the cidr of this APIKey.

        :param cidr: The cidr of this APIKey.
        :type: str
        """
        if cidr is not None and len(cidr) > 18:
            raise ValueError("Invalid value for `cidr`, length must be less than or equal to `18`")

        self._cidr = cidr

    @property
    def permissions(self):
        """
        Gets the permissions of this APIKey.

        :return: The permissions of this APIKey.
        :rtype: list[XAny]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this APIKey.

        :param permissions: The permissions of this APIKey.
        :type: list[XAny]
        """

        self._permissions = permissions

    @property
    def enabled(self):
        """
        Gets the enabled of this APIKey.

        :return: The enabled of this APIKey.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this APIKey.

        :param enabled: The enabled of this APIKey.
        :type: bool
        """

        self._enabled = enabled

    @property
    def user_id(self):
        """
        Gets the user_id of this APIKey.

        :return: The user_id of this APIKey.
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this APIKey.

        :param user_id: The user_id of this APIKey.
        :type: float
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id

    @property
    def created(self):
        """
        Gets the created of this APIKey.

        :return: The created of this APIKey.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this APIKey.

        :param created: The created of this APIKey.
        :type: datetime
        """

        self._created = created

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
        if not isinstance(other, APIKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
