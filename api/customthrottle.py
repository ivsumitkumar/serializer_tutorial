from rest_framework.throttling import UserRateThrottle

class EmployeeRateThrottle(UserRateThrottle):
    scope = 'employee'