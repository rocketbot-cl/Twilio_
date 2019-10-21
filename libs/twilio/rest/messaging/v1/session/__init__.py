# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.messaging.v1.session.message import MessageList
from twilio.rest.messaging.v1.session.participant import ParticipantList
from twilio.rest.messaging.v1.session.webhook import WebhookList


class SessionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the SessionList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.session.SessionList
        :rtype: twilio.rest.messaging.v1.session.SessionList
        """
        super(SessionList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Sessions'.format(**self._solution)

    def create(self, messaging_service_sid, friendly_name=values.unset,
               attributes=values.unset, date_created=values.unset,
               date_updated=values.unset, created_by=values.unset):
        """
        Create a new SessionInstance

        :param unicode messaging_service_sid: The SID of the SMS Service the session belongs to
        :param unicode friendly_name: A string to describe the resource
        :param unicode attributes: A JSON string that stores application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode created_by: The Identity of the session's creator

        :returns: Newly created SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionInstance
        """
        data = values.of({
            'MessagingServiceSid': messaging_service_sid,
            'FriendlyName': friendly_name,
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'CreatedBy': created_by,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return SessionInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams SessionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.session.SessionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SessionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.session.SessionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SessionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SessionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SessionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SessionPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SessionContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.session.SessionContext
        :rtype: twilio.rest.messaging.v1.session.SessionContext
        """
        return SessionContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a SessionContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.session.SessionContext
        :rtype: twilio.rest.messaging.v1.session.SessionContext
        """
        return SessionContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.SessionList>'


class SessionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the SessionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.session.SessionPage
        :rtype: twilio.rest.messaging.v1.session.SessionPage
        """
        super(SessionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SessionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.session.SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionInstance
        """
        return SessionInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.SessionPage>'


class SessionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the SessionContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.session.SessionContext
        :rtype: twilio.rest.messaging.v1.session.SessionContext
        """
        super(SessionContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Sessions/{sid}'.format(**self._solution)

        # Dependents
        self._participants = None
        self._messages = None
        self._webhooks = None

    def fetch(self):
        """
        Fetch a SessionInstance

        :returns: Fetched SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SessionInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the SessionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, friendly_name=values.unset, attributes=values.unset,
               date_created=values.unset, date_updated=values.unset,
               created_by=values.unset):
        """
        Update the SessionInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode attributes: A JSON string that stores application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode created_by: The Identity of the session's creator

        :returns: Updated SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'CreatedBy': created_by,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SessionInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantList
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(self._version, session_sid=self._solution['sid'], )
        return self._participants

    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.messaging.v1.session.message.MessageList
        :rtype: twilio.rest.messaging.v1.session.message.MessageList
        """
        if self._messages is None:
            self._messages = MessageList(self._version, session_sid=self._solution['sid'], )
        return self._messages

    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.messaging.v1.session.webhook.WebhookList
        :rtype: twilio.rest.messaging.v1.session.webhook.WebhookList
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(self._version, session_sid=self._solution['sid'], )
        return self._webhooks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.SessionContext {}>'.format(context)


class SessionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the SessionInstance

        :returns: twilio.rest.messaging.v1.session.SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionInstance
        """
        super(SessionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'attributes': payload.get('attributes'),
            'created_by': payload.get('created_by'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SessionContext for this SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionContext
        """
        if self._context is None:
            self._context = SessionContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def messaging_service_sid(self):
        """
        :returns: The SID of the SMS Service the session belongs to
        :rtype: unicode
        """
        return self._properties['messaging_service_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def created_by(self):
        """
        :returns: The Identity of the session's creator
        :rtype: unicode
        """
        return self._properties['created_by']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the session
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The absolute URLs of the Participants, Interactions, and Messages for the Session
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a SessionInstance

        :returns: Fetched SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SessionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset, attributes=values.unset,
               date_created=values.unset, date_updated=values.unset,
               created_by=values.unset):
        """
        Update the SessionInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode attributes: A JSON string that stores application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode created_by: The Identity of the session's creator

        :returns: Updated SessionInstance
        :rtype: twilio.rest.messaging.v1.session.SessionInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
            created_by=created_by,
        )

    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantList
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantList
        """
        return self._proxy.participants

    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.messaging.v1.session.message.MessageList
        :rtype: twilio.rest.messaging.v1.session.message.MessageList
        """
        return self._proxy.messages

    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.messaging.v1.session.webhook.WebhookList
        :rtype: twilio.rest.messaging.v1.session.webhook.WebhookList
        """
        return self._proxy.webhooks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.SessionInstance {}>'.format(context)
