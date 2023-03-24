from rest_framework import serializers
from .models import Alerts

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = ['id','ticketid','description' ,'status' ,'date' ,'assignedTo' ,'category' ,'createdDateTime' ,'severity' ,'alertstatus','incidentid' 
                  ,'classification' ,'serviceSource' ,'detectionSource' ,'alertWebURL' ,'incidentWebURL' ,'threatDisplayName','resolvedDateTime','firstActivityDateTime' ,'lastActivityDateTime' ,'devicednsName' ,'osPlatform' ,'rbacGroupName','loggedOnUser', 
'processCommandLine','logonLocation' ,'title','threatFamilyName','lastUpdateDateTime','defenderAvStatus','processStatus', 
'recipientEmailAddress' ,'deliveryAction' ,'emailSender','publicIpAddress']
