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


class TaskQueueRealTimeStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueRealTimeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace that contains the TaskQueue
        :param task_queue_sid: The SID of the TaskQueue from which these statistics were calculated

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsList
        """
        super(TaskQueueRealTimeStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }

    def get(self):
        """
        Constructs a TaskQueueRealTimeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        return TaskQueueRealTimeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __call__(self):
        """
        Constructs a TaskQueueRealTimeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        return TaskQueueRealTimeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsList>'


class TaskQueueRealTimeStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the TaskQueueRealTimeStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The SID of the Workspace that contains the TaskQueue
        :param task_queue_sid: The SID of the TaskQueue from which these statistics were calculated

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsPage
        """
        super(TaskQueueRealTimeStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskQueueRealTimeStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        return TaskQueueRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsPage>'


class TaskQueueRealTimeStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueRealTimeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch
        :param task_queue_sid: The SID of the TaskQueue for which to fetch statistics

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        super(TaskQueueRealTimeStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/RealTimeStatistics'.format(**self._solution)

    def fetch(self, task_channel=values.unset):
        """
        Fetch a TaskQueueRealTimeStatisticsInstance

        :param unicode task_channel: The TaskChannel for which to fetch statistics

        :returns: Fetched TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        params = values.of({'TaskChannel': task_channel, })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return TaskQueueRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsContext {}>'.format(context)


class TaskQueueRealTimeStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueRealTimeStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        super(TaskQueueRealTimeStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'activity_statistics': payload.get('activity_statistics'),
            'longest_task_waiting_age': deserialize.integer(payload.get('longest_task_waiting_age')),
            'longest_task_waiting_sid': payload.get('longest_task_waiting_sid'),
            'task_queue_sid': payload.get('task_queue_sid'),
            'tasks_by_priority': payload.get('tasks_by_priority'),
            'tasks_by_status': payload.get('tasks_by_status'),
            'total_available_workers': deserialize.integer(payload.get('total_available_workers')),
            'total_eligible_workers': deserialize.integer(payload.get('total_eligible_workers')),
            'total_tasks': deserialize.integer(payload.get('total_tasks')),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: TaskQueueRealTimeStatisticsContext for this TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        if self._context is None:
            self._context = TaskQueueRealTimeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                task_queue_sid=self._solution['task_queue_sid'],
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
    def activity_statistics(self):
        """
        :returns: The number of current Workers by Activity
        :rtype: dict
        """
        return self._properties['activity_statistics']

    @property
    def longest_task_waiting_age(self):
        """
        :returns: The age of the longest waiting Task
        :rtype: unicode
        """
        return self._properties['longest_task_waiting_age']

    @property
    def longest_task_waiting_sid(self):
        """
        :returns: The SID of the longest waiting Task
        :rtype: unicode
        """
        return self._properties['longest_task_waiting_sid']

    @property
    def task_queue_sid(self):
        """
        :returns: The SID of the TaskQueue from which these statistics were calculated
        :rtype: unicode
        """
        return self._properties['task_queue_sid']

    @property
    def tasks_by_priority(self):
        """
        :returns: The number of Tasks by priority
        :rtype: dict
        """
        return self._properties['tasks_by_priority']

    @property
    def tasks_by_status(self):
        """
        :returns: The number of Tasks by their current status
        :rtype: dict
        """
        return self._properties['tasks_by_status']

    @property
    def total_available_workers(self):
        """
        :returns: The total number of Workers available for Tasks in the TaskQueue
        :rtype: unicode
        """
        return self._properties['total_available_workers']

    @property
    def total_eligible_workers(self):
        """
        :returns: The total number of Workers eligible for Tasks in the TaskQueue, independent of their Activity state
        :rtype: unicode
        """
        return self._properties['total_eligible_workers']

    @property
    def total_tasks(self):
        """
        :returns: The total number of Tasks
        :rtype: unicode
        """
        return self._properties['total_tasks']

    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the TaskQueue
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL of the TaskQueue statistics resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, task_channel=values.unset):
        """
        Fetch a TaskQueueRealTimeStatisticsInstance

        :param unicode task_channel: The TaskChannel for which to fetch statistics

        :returns: Fetched TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        return self._proxy.fetch(task_channel=task_channel, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsInstance {}>'.format(context)