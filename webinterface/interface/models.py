from django.db import models

# Create your models here.


class Alerts(models.Model):
    id = models.AutoField(primary_key=True)
    ticketid = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=500)
    assignedTo   = models.CharField(max_length=500)
    category     = models.CharField(max_length=500)
    createdDateTime = models.DateTimeField(auto_now_add=False)
    severity     = models.CharField(max_length=500)
    alertstatus  = models.CharField(max_length=500)
    incidentid   = models.CharField(max_length=500)
    classification= models.CharField(max_length=500)
    serviceSource = models.CharField(max_length=500)
    detectionSource = models.CharField(max_length=500)
    alertWebURL = models.CharField(max_length=500)
    incidentWebURL = models.CharField(max_length=500)
    threatDisplayName = models.CharField(max_length=500)
    resolvedDateTime = models.DateTimeField(auto_now_add=False)
    firstActivityDateTime = models.DateTimeField(auto_now_add=False)
    lastActivityDateTime = models.DateTimeField(auto_now_add=False)
    devicednsName = models.CharField(max_length=500)
    osPlatform = models.CharField(max_length=500)
    rbacGroupName = models.CharField(max_length=500)
    loggedOnUser = models.CharField(max_length=500)
    processCommandLine = models.CharField(max_length=5000)
    logonLocation = models.CharField(max_length=500)
    title = models.CharField(max_length=5000)
    threatFamilyName = models.CharField(max_length=500)
    lastUpdateDateTime = models.DateTimeField(auto_now_add=False)
    defenderAvStatus = models.CharField(max_length=500)
    processStatus = models.CharField(max_length=500)
    recipientEmailAddress = models.CharField(max_length=500)
    deliveryAction = models.CharField(max_length=500)
    emailSender = models.CharField(max_length=500)
    publicIpAddress = models.CharField(max_length=500)


    def __str__(self):
        return self.name