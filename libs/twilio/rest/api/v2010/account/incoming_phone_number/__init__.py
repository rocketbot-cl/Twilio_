# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on import AssignedAddOnList
from twilio.rest.api.v2010.account.incoming_phone_number.local import LocalList
from twilio.rest.api.v2010.account.incoming_phone_number.mobile import MobileList
from twilio.rest.api.v2010.account.incoming_phone_number.toll_free import TollFreeList


class IncomingPhoneNumberList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the IncomingPhoneNumberList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberList
        """
        super(IncomingPhoneNumberList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/IncomingPhoneNumbers.json'.format(**self._solution)

        # Components
        self._local = None
        self._mobile = None
        self._toll_free = None

    def stream(self, beta=values.unset, friendly_name=values.unset,
               phone_number=values.unset, origin=values.unset, limit=None,
               page_size=None):
        """
        Streams IncomingPhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool beta: Whether to include new phone numbers
        :param unicode friendly_name: A string that identifies the IncomingPhoneNumber resources to read
        :param unicode phone_number: The phone numbers of the IncomingPhoneNumber resources to read
        :param unicode origin: Include phone numbers based on their origin. By default, phone numbers of all origin are included.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, origin=values.unset, limit=None,
             page_size=None):
        """
        Lists IncomingPhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool beta: Whether to include new phone numbers
        :param unicode friendly_name: A string that identifies the IncomingPhoneNumber resources to read
        :param unicode phone_number: The phone numbers of the IncomingPhoneNumber resources to read
        :param unicode origin: Include phone numbers based on their origin. By default, phone numbers of all origin are included.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance]
        """
        return list(self.stream(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, origin=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of IncomingPhoneNumberInstance records from the API.
        Request is executed immediately

        :param bool beta: Whether to include new phone numbers
        :param unicode friendly_name: A string that identifies the IncomingPhoneNumber resources to read
        :param unicode phone_number: The phone numbers of the IncomingPhoneNumber resources to read
        :param unicode origin: Include phone numbers based on their origin. By default, phone numbers of all origin are included.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        """
        params = values.of({
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'Origin': origin,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return IncomingPhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IncomingPhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return IncomingPhoneNumberPage(self._version, response, self._solution)

    def create(self, api_version=values.unset, friendly_name=values.unset,
               sms_application_sid=values.unset, sms_fallback_method=values.unset,
               sms_fallback_url=values.unset, sms_method=values.unset,
               sms_url=values.unset, status_callback=values.unset,
               status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset,
               emergency_status=values.unset, emergency_address_sid=values.unset,
               trunk_sid=values.unset, identity_sid=values.unset,
               address_sid=values.unset, voice_receive_mode=values.unset,
               phone_number=values.unset, area_code=values.unset):
        """
        Create a new IncomingPhoneNumberInstance

        :param unicode api_version: The API version to use for incoming calls made to the new phone number
        :param unicode friendly_name: A string to describe the new phone number
        :param unicode sms_application_sid: The SID of the application to handle SMS messages
        :param unicode sms_fallback_method: HTTP method used with sms_fallback_url
        :param unicode sms_fallback_url: The URL we call when an error occurs while executing TwiML
        :param unicode sms_method: The HTTP method to use with sms url
        :param unicode sms_url: The URL we should call when the new phone number receives an incoming SMS message
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: HTTP method we should use to call status_callback
        :param unicode voice_application_sid: The SID of the application to handle the new phone number
        :param bool voice_caller_id_lookup: Whether to lookup the caller's name
        :param unicode voice_fallback_method: The HTTP method used with voice_fallback_url
        :param unicode voice_fallback_url: The URL we will call when an error occurs in TwiML
        :param unicode voice_method: The HTTP method used with the voice_url
        :param unicode voice_url: The URL we should call when the phone number receives a call
        :param IncomingPhoneNumberInstance.EmergencyStatus emergency_status: Status determining whether the new phone number is enabled for emergency calling
        :param unicode emergency_address_sid: The emergency address configuration to use for emergency calling
        :param unicode trunk_sid: SID of the trunk to handle calls to the new phone number
        :param unicode identity_sid: The SID of the Identity resource to associate with the new phone number
        :param unicode address_sid: The SID of the Address resource associated with the phone number
        :param IncomingPhoneNumberInstance.VoiceReceiveMode voice_receive_mode: Incoming call type: fax or voice
        :param unicode phone_number: The phone number to purchase in E.164 format
        :param unicode area_code: The desired area code for the new phone number

        :returns: Newly created IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        data = values.of({
            'PhoneNumber': phone_number,
            'AreaCode': area_code,
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
            'EmergencyStatus': emergency_status,
            'EmergencyAddressSid': emergency_address_sid,
            'TrunkSid': trunk_sid,
            'IdentitySid': identity_sid,
            'AddressSid': address_sid,
            'VoiceReceiveMode': voice_receive_mode,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return IncomingPhoneNumberInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    @property
    def local(self):
        """
        Access the local

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.local.LocalList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.local.LocalList
        """
        if self._local is None:
            self._local = LocalList(self._version, account_sid=self._solution['account_sid'], )
        return self._local

    @property
    def mobile(self):
        """
        Access the mobile

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileList
        """
        if self._mobile is None:
            self._mobile = MobileList(self._version, account_sid=self._solution['account_sid'], )
        return self._mobile

    @property
    def toll_free(self):
        """
        Access the toll_free

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.toll_free.TollFreeList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.toll_free.TollFreeList
        """
        if self._toll_free is None:
            self._toll_free = TollFreeList(self._version, account_sid=self._solution['account_sid'], )
        return self._toll_free

    def get(self, sid):
        """
        Constructs a IncomingPhoneNumberContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        """
        return IncomingPhoneNumberContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a IncomingPhoneNumberContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        """
        return IncomingPhoneNumberContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IncomingPhoneNumberList>'


class IncomingPhoneNumberPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the IncomingPhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberPage
        """
        super(IncomingPhoneNumberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IncomingPhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        return IncomingPhoneNumberInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IncomingPhoneNumberPage>'


class IncomingPhoneNumberContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, sid):
        """
        Initialize the IncomingPhoneNumberContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        """
        super(IncomingPhoneNumberContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json'.format(**self._solution)

        # Dependents
        self._assigned_add_ons = None

    def update(self, account_sid=values.unset, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset,
               emergency_status=values.unset, emergency_address_sid=values.unset,
               trunk_sid=values.unset, voice_receive_mode=values.unset,
               identity_sid=values.unset, address_sid=values.unset):
        """
        Update the IncomingPhoneNumberInstance

        :param unicode account_sid: The SID of the Account that created the resource to update
        :param unicode api_version: The API version to use for incoming calls made to the phone number
        :param unicode friendly_name: A string to describe the resource
        :param unicode sms_application_sid: Unique string that identifies the application
        :param unicode sms_fallback_method: HTTP method used with sms_fallback_url
        :param unicode sms_fallback_url: The URL we call when an error occurs while executing TwiML
        :param unicode sms_method: The HTTP method to use with sms_url
        :param unicode sms_url: The URL we should call when the phone number receives an incoming SMS message
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: The HTTP method we should use to call status_callback
        :param unicode voice_application_sid: The SID of the application to handle the phone number
        :param bool voice_caller_id_lookup: Whether to lookup the caller's name
        :param unicode voice_fallback_method: The HTTP method used with fallback_url
        :param unicode voice_fallback_url: The URL we will call when an error occurs in TwiML
        :param unicode voice_method: The HTTP method used with the voice_url
        :param unicode voice_url: The URL we should call when the phone number receives a call
        :param IncomingPhoneNumberInstance.EmergencyStatus emergency_status: Whether the phone number is enabled for emergency calling
        :param unicode emergency_address_sid: The emergency address configuration to use for emergency calling
        :param unicode trunk_sid: SID of the trunk to handle phone calls to the phone number
        :param IncomingPhoneNumberInstance.VoiceReceiveMode voice_receive_mode: Incoming call type: fax or voice
        :param unicode identity_sid: Unique string that identifies the identity associated with number
        :param unicode address_sid: The SID of the Address resource associated with the phone number

        :returns: Updated IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        data = values.of({
            'AccountSid': account_sid,
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
            'EmergencyStatus': emergency_status,
            'EmergencyAddressSid': emergency_address_sid,
            'TrunkSid': trunk_sid,
            'VoiceReceiveMode': voice_receive_mode,
            'IdentitySid': identity_sid,
            'AddressSid': address_sid,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return IncomingPhoneNumberInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def fetch(self):
        """
        Fetch a IncomingPhoneNumberInstance

        :returns: Fetched IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return IncomingPhoneNumberInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the IncomingPhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def assigned_add_ons(self):
        """
        Access the assigned_add_ons

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnList
        """
        if self._assigned_add_ons is None:
            self._assigned_add_ons = AssignedAddOnList(
                self._version,
                account_sid=self._solution['account_sid'],
                resource_sid=self._solution['sid'],
            )
        return self._assigned_add_ons

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IncomingPhoneNumberContext {}>'.format(context)


class IncomingPhoneNumberInstance(InstanceResource):
    """  """

    class AddressRequirement(object):
        NONE = "none"
        ANY = "any"
        LOCAL = "local"
        FOREIGN = "foreign"

    class EmergencyStatus(object):
        ACTIVE = "Active"
        INACTIVE = "Inactive"

    class VoiceReceiveMode(object):
        VOICE = "voice"
        FAX = "fax"

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the IncomingPhoneNumberInstance

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        super(IncomingPhoneNumberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'address_sid': payload.get('address_sid'),
            'address_requirements': payload.get('address_requirements'),
            'api_version': payload.get('api_version'),
            'beta': payload.get('beta'),
            'capabilities': payload.get('capabilities'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'identity_sid': payload.get('identity_sid'),
            'phone_number': payload.get('phone_number'),
            'origin': payload.get('origin'),
            'sid': payload.get('sid'),
            'sms_application_sid': payload.get('sms_application_sid'),
            'sms_fallback_method': payload.get('sms_fallback_method'),
            'sms_fallback_url': payload.get('sms_fallback_url'),
            'sms_method': payload.get('sms_method'),
            'sms_url': payload.get('sms_url'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'trunk_sid': payload.get('trunk_sid'),
            'uri': payload.get('uri'),
            'voice_application_sid': payload.get('voice_application_sid'),
            'voice_caller_id_lookup': payload.get('voice_caller_id_lookup'),
            'voice_fallback_method': payload.get('voice_fallback_method'),
            'voice_fallback_url': payload.get('voice_fallback_url'),
            'voice_method': payload.get('voice_method'),
            'voice_url': payload.get('voice_url'),
            'emergency_status': payload.get('emergency_status'),
            'emergency_address_sid': payload.get('emergency_address_sid'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: IncomingPhoneNumberContext for this IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        """
        if self._context is None:
            self._context = IncomingPhoneNumberContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def address_sid(self):
        """
        :returns: The SID of the Address resource associated with the phone number
        :rtype: unicode
        """
        return self._properties['address_sid']

    @property
    def address_requirements(self):
        """
        :returns: Whether the phone number requires an Address registered with Twilio.
        :rtype: IncomingPhoneNumberInstance.AddressRequirement
        """
        return self._properties['address_requirements']

    @property
    def api_version(self):
        """
        :returns: The API version used to start a new TwiML session
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def beta(self):
        """
        :returns: Whether the phone number is new to the Twilio platform
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: Indicate if a phone can receive calls or messages
        :rtype: unicode
        """
        return self._properties['capabilities']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def identity_sid(self):
        """
        :returns: The SID of the Identity resource associated with number
        :rtype: unicode
        """
        return self._properties['identity_sid']

    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def origin(self):
        """
        :returns: The phone number's origin. Can be twilio or hosted.
        :rtype: unicode
        """
        return self._properties['origin']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sms_application_sid(self):
        """
        :returns: The SID of the application that handles SMS messages sent to the phone number
        :rtype: unicode
        """
        return self._properties['sms_application_sid']

    @property
    def sms_fallback_method(self):
        """
        :returns: The HTTP method used with sms_fallback_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: The URL that we call when an error occurs while retrieving or executing the TwiML
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: The HTTP method to use with sms_url
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: The URL we call when the phone number receives an incoming SMS message
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """
        :returns: The URL to send status information to your application
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we use to call status_callback
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def trunk_sid(self):
        """
        :returns: The SID of the Trunk that handles calls to the phone number
        :rtype: unicode
        """
        return self._properties['trunk_sid']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def voice_application_sid(self):
        """
        :returns: The SID of the application that handles calls to the phone number
        :rtype: unicode
        """
        return self._properties['voice_application_sid']

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: Whether to lookup the caller's name
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """
        :returns: The HTTP method used with voice_fallback_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: The URL we call when an error occurs in TwiML
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: The HTTP method used with the voice_url
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: The URL we call when the phone number receives a call
        :rtype: unicode
        """
        return self._properties['voice_url']

    @property
    def emergency_status(self):
        """
        :returns: Whether the phone number is enabled for emergency calling
        :rtype: IncomingPhoneNumberInstance.EmergencyStatus
        """
        return self._properties['emergency_status']

    @property
    def emergency_address_sid(self):
        """
        :returns: The emergency address configuration to use for emergency calling
        :rtype: unicode
        """
        return self._properties['emergency_address_sid']

    def update(self, account_sid=values.unset, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset,
               emergency_status=values.unset, emergency_address_sid=values.unset,
               trunk_sid=values.unset, voice_receive_mode=values.unset,
               identity_sid=values.unset, address_sid=values.unset):
        """
        Update the IncomingPhoneNumberInstance

        :param unicode account_sid: The SID of the Account that created the resource to update
        :param unicode api_version: The API version to use for incoming calls made to the phone number
        :param unicode friendly_name: A string to describe the resource
        :param unicode sms_application_sid: Unique string that identifies the application
        :param unicode sms_fallback_method: HTTP method used with sms_fallback_url
        :param unicode sms_fallback_url: The URL we call when an error occurs while executing TwiML
        :param unicode sms_method: The HTTP method to use with sms_url
        :param unicode sms_url: The URL we should call when the phone number receives an incoming SMS message
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: The HTTP method we should use to call status_callback
        :param unicode voice_application_sid: The SID of the application to handle the phone number
        :param bool voice_caller_id_lookup: Whether to lookup the caller's name
        :param unicode voice_fallback_method: The HTTP method used with fallback_url
        :param unicode voice_fallback_url: The URL we will call when an error occurs in TwiML
        :param unicode voice_method: The HTTP method used with the voice_url
        :param unicode voice_url: The URL we should call when the phone number receives a call
        :param IncomingPhoneNumberInstance.EmergencyStatus emergency_status: Whether the phone number is enabled for emergency calling
        :param unicode emergency_address_sid: The emergency address configuration to use for emergency calling
        :param unicode trunk_sid: SID of the trunk to handle phone calls to the phone number
        :param IncomingPhoneNumberInstance.VoiceReceiveMode voice_receive_mode: Incoming call type: fax or voice
        :param unicode identity_sid: Unique string that identifies the identity associated with number
        :param unicode address_sid: The SID of the Address resource associated with the phone number

        :returns: Updated IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        return self._proxy.update(
            account_sid=account_sid,
            api_version=api_version,
            friendly_name=friendly_name,
            sms_application_sid=sms_application_sid,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_application_sid=voice_application_sid,
            voice_caller_id_lookup=voice_caller_id_lookup,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            emergency_status=emergency_status,
            emergency_address_sid=emergency_address_sid,
            trunk_sid=trunk_sid,
            voice_receive_mode=voice_receive_mode,
            identity_sid=identity_sid,
            address_sid=address_sid,
        )

    def fetch(self):
        """
        Fetch a IncomingPhoneNumberInstance

        :returns: Fetched IncomingPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the IncomingPhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def assigned_add_ons(self):
        """
        Access the assigned_add_ons

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnList
        """
        return self._proxy.assigned_add_ons

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IncomingPhoneNumberInstance {}>'.format(context)
